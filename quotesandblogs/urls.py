from django.urls import path
from .import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="index"),

    path("signup",views.signup,name="signup"),
    path("login",views.userLogin,name="login"),
    path("logout",views.userLogout,name="logout"),
    
    path("quotes/<slug:quotesCategory>",views.QuoteCategoryView.as_view(),name="quote-category"),
    path("quote/<slug:quoteDetail>",views.QuoteDetail.as_view(),name="quote-details"),

    #like quote
    path("quote/like-quote/<int:id>",views.LikeQuote,name='like-quote'),

    #copied quote to session
    path("quote/copy/<int:id>",views.CopyQuoteToSession),

    #clap blog
    path("blog/clap-blog/<int:id>",views.ClapBlog,name='clap-blog'),

    path("articles/<slug:blogsCategory>",views.BlogCategoryView.as_view(),name="blog-category"),
    path("<slug:blogDetail>",views.BlogDetail.as_view(),name="blog-details"),
    
    path("motivativequotes/quote-of-the-day/",views.QuoteOfTheDay.as_view(),name="quote-of-the-day"),
    path("motivativequotes/give-me-quote/",views.GiveMeQuote,name="give-me-quote"),
    path("motivativequotes/blogs/",views.AllBlogs,name="all-blogs"),
    path("motivativequotes/contact/",views.ContactView.as_view(),name="contact"),
    path("motivativequotes/error/",views.errorPage,name="error"),
    path("motivativequotes/quote-maker/",views.QuoteMaker.as_view(),name="quote-maker"),
    path("motivativequotes/search/",views.searchResults,name="search"),

]
