from django.shortcuts import redirect, render
from django.views import View
from .models import Blog,QuotesCategory,Quote


class HomeView(View):
    def get(self,request):
        myCategories = QuotesCategory.objects.all()
        context={
            "myCategories":myCategories
        }
        return render(request,'pages/index.html',context)


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
        return render(request,"pages/quoteDetails.html")


class BlogDetail(View):
    def get(self,request,blogDetail):
        blog = Blog.objects.get(slug=blogDetail)
        print(blog.tags.all())
        context={
            "blog":blog,
        }
        return render(request,"pages/blogDetails.html",context)


class ContactView(View):
    def get(self,request):
        return render(request,"pages/contact.html")

class QuoteMaker(View):
    def get(self,request):
        return render(request,"pages/quoteMaker.html")

def error_404(request,exception):
        return render(request,'pages/404.html')

def errorPage(request):
        return render(request,'pages/404.html')