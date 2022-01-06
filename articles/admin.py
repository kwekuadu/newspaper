from django.contrib import admin
from .models import Article , Comment
# Register your models here.
 
class CommentInline(admin.TabularInline):  #admin.StackedInline
    model = Comment
    #extra = 2   #number of comments displayed at a time
    
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)