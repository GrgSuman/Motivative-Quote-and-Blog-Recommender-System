from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views import View
from .models import Blog,QuotesCategory,Quote,Contact,SubscriberEmail
from django.core.paginator import Paginator
import random
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import ContactForm
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'



class HomeView(View):
    def get(self,request):
        myCategories = QuotesCategory.objects.all()
        recentBlogs = Blog.objects.filter(postStatus=True).order_by('-id')
        print(recentBlogs)
        context={
            "myCategories" : myCategories,
            'recentBlogs' : recentBlogs
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
            context = {
                "allquotes" : category.quotescategory.all().filter(postStatus=True),
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
        # try:
            quote = Quote.objects.get(slug=quoteDetail)
            context = {
                'quote' : quote
            }
            return render(request,"pages/quoteDetails.html",context)

        # except:
        #     return redirect('index')


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
    return JsonResponse({'likes':likes})

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