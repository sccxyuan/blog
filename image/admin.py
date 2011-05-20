from django.contrib import admin
from mysite.image.models import Article,Comment,User,Categories,MyProfile
class UserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','tel','mobile','address','website','birthday','gender','blog','QQ','MSN','IM','position','country',)
    search_fields=('username','first_name','last_name','email',)

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title',)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=('cateName',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(MyProfile)