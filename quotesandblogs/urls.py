from django.urls import path
from .import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="index"),
    
    path("quotes/<slug:quotesCategory>",views.QuoteCategoryView.as_view(),name="quote-category"),
    path("quote/<slug:quoteDetail>",views.QuoteDetail.as_view(),name="quote-details"),

    path("articles/<slug:blogsCategory>",views.BlogCategoryView.as_view(),name="blog-category"),
    path("<slug:blogDetail>",views.BlogDetail.as_view(),name="blog-details"),


    path("motivativequotes/contact/",views.ContactView.as_view(),name="contact"),
    path("motivativequotes/error/",views.errorPage,name="error"),
    path("motivativequotes/quote-maker/",views.QuoteMaker.as_view(),name="quote-maker"),
]
