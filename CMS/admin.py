from django.contrib import admin
from .models import *

# Register your models here.
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/js/editor/kindeditor/kindeditor-all.js',
            '/static/js/editor/kindeditor/lang/zh_CN.js',
            '/static/js/editor/kindeditor/config.js',
        )


admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
