#! /usr/bin/env python
#coding=utf-8
from mysite.image import models

def cate():
    categories = models.Categories.objects.order_by('id').all()
    return categories
#文章标题
def caption():
    caption = models.Article.objects.order_by('-id').values('id','title')[:10]
    return caption

#标签
def tag():
    tags = models.Article.objects.order_by('-id').values('tags','title')
    info = []
    for  tagsValues in tags:
        if tagsValues['tags']:
            tag = tagsValues['tags']
            info.append(tag)
    str = ','.join(info)
    str = str.split(',')
    return set(str)