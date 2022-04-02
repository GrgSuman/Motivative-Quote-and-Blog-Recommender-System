from turtle import pos
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views import View
from .models import Blog,QuotesCategory,Quote,Contact,SubscriberEmail,CustomUser
from django.core.paginator import Paginator
import random
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import ContactForm
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
import json





regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class HomeView(View):
    def get(self,request):
        myCategories = QuotesCategory.objects.all()
        recentBlogs = Blog.objects.filter(postStatus=True).order_by('-id')

        #recommender logic starts
        allquotes = Quote.objects.all().values().filter(postStatus=True)
        data = pd.DataFrame(list(allquotes))
        recommendedQuotes = {}
        recommendedQuotesQuerySet = []

        quoteTitle = ""
        userCopiedQUote = getSessionValue(request,'copiedQuoteByUser')
        userLikedQuote = getSessionValue(request,'likedQuoteByUser')
        userVisitedQuoteDetail = getSessionValue(request,'userVisitedDetail')
        userVisitedQuoteCategory = getSessionValue(request,'userVisitedQuoteCategory')

        #copied quote has high priority
        #copied > liked > visited detail of specific quote > visited category
        if userCopiedQUote:
            quoteTitle = userCopiedQUote
        elif userLikedQuote:
            quoteTitle = userLikedQuote
        elif userVisitedQuoteDetail:
            quoteTitle = userVisitedQuoteDetail
        elif userVisitedQuoteCategory:
            quoteTitle = userVisitedQuoteCategory
        
        if quoteTitle !="":
            recommendedQuotes = quote_recommender(quoteTitle,data).head(8).to_dict()
            for quote in recommendedQuotes:
                qt = Quote.objects.get(quote=recommendedQuotes[quote])
                recommendedQuotesQuerySet.append(qt)
        else:
            quoteList = []
            while len(quoteList) < 8:
                i = random.randint(0,len(allquotes))
                if Quote.objects.filter(id=i).exists():
                    qt = Quote.objects.get(id=i)
                    if not qt in quoteList:
                        quoteList.append(qt)
            recommendedQuotesQuerySet = quoteList

        context={
            "myCategories" : myCategories,
            'recentBlogs' : recentBlogs,
            'recommendedQuotes' : recommendedQuotesQuerySet
        }
        return render(request,'pages/index.html',context)
    
    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        
        if(name=='' or email ==''):
            messages.error(request,"Please enter both name and email")
            return redirect('index')
        else:
            if(re.fullmatch(regex, email)):
                subs = SubscriberEmail(email=email,name=name)
                messages.success(request,name+", thanks for subscribing Motivative Quotes")
                subs.save()
                return redirect('index')
            messages.error(request,"Please enter valid email")
            return redirect('index')
         


class QuoteCategoryView(View):
    def get(self,request,quotesCategory):
        try:
            category = QuotesCategory.objects.get(slug=quotesCategory)
            quotesWithThisCategory = category.quotescategory.all().filter(postStatus=True).order_by('-id')
            i = random.randint(0,len(quotesWithThisCategory))
            if Quote.objects.filter(id=i).exists():
                quote = Quote.objects.get(id=i)
                setSessionValue(request,'userVisitedQuoteCategory',quote.quote) 
            else:
                setSessionValue(request,'userVisitedQuoteCategory',quotesWithThisCategory[0].quote)

            context = {
                "allquotes" : quotesWithThisCategory,
                'category' : category
            }
            return render(request,"pages/category-wise-quotes.html",context)

        except:
            return redirect('index')


class BlogCategoryView(View):
    def get(self,request,blogsCategory):
        return render(request,"pages/category-wise-blogs.html")


class QuoteDetail(View):
    def get(self,request,quoteDetail):
        try:
            quote = Quote.objects.get(slug=quoteDetail)
            setSessionValue(request,'userVisitedDetail',quote.quote)

            context = {
                'quote' : quote
            }
            return render(request,"pages/quoteDetails.html",context)

        except:
            return redirect('index')


class BlogDetail(View):
    def get(self,request,blogDetail):
        blog = Blog.objects.get(slug=blogDetail)
        # print(blog.tags.all())

        blogList=[]
        #in my blog detail  related posts
        # blogs = Blog.objects.all().filter(postStatus=True).filter(mainCategory=blog.mainCategory)
        blogs = Blog.objects.all().filter(postStatus=True)
        for i in blogs:
            if len(blogList) < 4:
                i = random.randint(0,len(blogs))
                if Blog.objects.filter(id=i).exists():
                    blg = Blog.objects.get(id=i)
                    if not blg in blogList and not blg==blog:
                        blogList.append(blg)
        context={
            "blog":blog,
             "related":blogList,
        }
        return render(request,"pages/blogDetails.html",context)


class ContactView(SuccessMessageMixin,CreateView):
    model=Contact
    form_class=ContactForm
    template_name="pages/contact.html"
    # fields="__all__"
    success_url='/'
    success_message="Your message was sent successfully"


class QuoteMaker(View):
    def get(self,request):
        return render(request,"pages/quoteMaker.html")


def searchResults(request):
    blogs = Blog.objects.filter(title__icontains=request.GET['q'])
    context={
       "blogs":blogs,
        "total":len(blogs),
    }
    return render(request,"pages/search.html",context)


class QuoteOfTheDay(View):
    def get(self,request):
        quote = Quote.objects.filter(postStatus=True).filter(category=1)
        i = random.randint(0,len(quote))
        quoteOfTheDay = ""
        if Quote.objects.filter(id=i).exists():
            quoteOfTheDay = Quote.objects.get(id=i)
        else:
            quoteOfTheDay = quote[0]
        
        context = {
            'quote' : quoteOfTheDay.quote,
            'author' : quoteOfTheDay.author
        }
        return render(request,"pages/quoteOfTheDay.html",context)


def AllBlogs(request):
    blog = Blog.objects.all().filter(postStatus=True).order_by('-id')
    paginator = Paginator(blog, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
    "blogs":page_obj
}
    return render(request,'pages/blogs.html',context)


def error_404(request,exception):
        return render(request,'pages/404.html')


def errorPage(request):
        return render(request,'pages/404.html')


def LikeQuote(request,id):
    quote = Quote.objects.get(id=id)
    quote.likes += 1
    likes = quote.likes
    quote.save()
    setSessionValue(request,'likedQuoteByUser',quote.quote)
    return JsonResponse({'likes':likes})

def CopyQuoteToSession(request,id):
    quote = Quote.objects.get(id=id)
    setSessionValue(request,'copiedQuoteByUser',quote.quote)
    return JsonResponse({})

def ClapBlog(request,id):
    blog = Blog.objects.get(id=id)
    blog.claps += 1
    claps = blog.claps
    blog.save()
    return JsonResponse({'claps':claps})

def GiveMeQuote(request):
    quote = Quote.objects.filter(postStatus=True).filter(category=1)
    i = random.randint(0,len(quote))
    quoteOfTheDay = ""
    if Quote.objects.filter(id=i).exists():
        quoteOfTheDay = Quote.objects.get(id=i)
    else:
        quoteOfTheDay = quote[0]
    
    context = {
        'quote' : quoteOfTheDay.quote,
        'author' : quoteOfTheDay.author
    }
    return JsonResponse(context)

def getSessionValue(request,key):
    return request.session.get(key)

def setSessionValue(request,key,value):
    request.session[key] = value

def quote_recommender(quote,data):
    dataset = data
    dataset = dataset[['quote','keywords']]
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    matrix = tf.fit_transform(dataset['keywords'])
    cosine_similarities = linear_kernel(matrix,matrix)
    quote_title = dataset['quote']
    indices = pd.Series(dataset.index, index=dataset['quote'])
    idx = indices[quote]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:30]
    quote_indices = [i[0] for i in sim_scores]
    return quote_title.iloc[quote_indices]

def signup(request):
    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        data = {
            "username":post_data['username'],
            "password1":post_data['password'],
            "password2":post_data['password'],
        }
        fm = UserCreationForm(data)
        
        if fm.is_valid():
            fm.save()
            user = User.objects.get(username=post_data['username'])
            user.email=post_data['email']
            user.save()

            cuser = CustomUser()
            cuser.activation_key=1234
            cuser.user=user
            cuser.save()

            return JsonResponse({"status":"success"})
        else:
            return JsonResponse(fm.errors.as_json(),safe=False)
    return JsonResponse({"message":"hello k xa"})

def userLogin(request):
    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        user = authenticate(request, username=post_data['username'], password=post_data['password'])
        if user is not None:
            print("yooo")
            login(request, user)
            return JsonResponse({"status":"success"})
        else:
            return JsonResponse({"status":"Invalid username and password"})
    return JsonResponse({"message":"Hello K xa "})

def userLogout(request):
    logout(request)
    return redirect("/")
