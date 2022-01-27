from django.contrib import admin
from .models import QuotesCategory,BlogsCategory,Quote,Blog,SubscriberEmail,Contact

class QuotesCategoryAdmin(admin.ModelAdmin):
    model = QuotesCategory
    list_display = ['id','name']


class BlogsCategoryAdmin(admin.ModelAdmin):
    model = BlogsCategory
    list_display = ['id','name']


class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ['id','quote','likes','author',"postStatus"]


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ['id','title','mainCategory','claps','createdAt','author',"postStatus"]


class SubscriberEmailAdmin(admin.ModelAdmin):
    model = SubscriberEmail
    list_display = ['id','name','email',"subscriptionDate"]


class ContactModelAdmin(admin.ModelAdmin):
    list_display=('full_name','email','phone','message')


admin.site.register(QuotesCategory,QuotesCategoryAdmin)
admin.site.register(BlogsCategory,BlogsCategoryAdmin)
admin.site.register(Quote,QuoteAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(SubscriberEmail,SubscriberEmailAdmin)
admin.site.register(Contact,ContactModelAdmin)
