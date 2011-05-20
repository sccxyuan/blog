#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response,HttpResponseRedirect
import time,datetime
from mysite.image import common,models
#from mysite.image.common import cate,caption,tag,
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.db import connection
import pdb
import settings


def zhuye(request):
    captions = common.caption()
    categories = common.cate()
    for i in categories:
                        i.count = models.Article.objects.filter(cate = i.id).count()
     
    return render_to_response('2.html',locals())


def zhu(request):
     categories = common.cate()
     tagValues = common.tag()
     captions = common.caption()
#     id = int(request.GET.get('action'))
     category = request.GET.get('category')
     keywords = request.GET.get('keywords')
     tags = request.GET.get('tags')
   #  pdb.set_trace()
     if category:
     	category = int(category)
     	articles = models.Article.objects.order_by('-id').filter(cate__id = category).values(
     				'times','cate__cateName','hoter','id','content','title')
     	action = '&category=%d'%category
     elif keywords:
     	articles = models.Article.objects.order_by('-id').filter(Q(content__icontains
     			= keywords) | Q(caption__icontains = keywords) | Q(times__icontains =
     			keywords)).values('times','title','id','content','hoter','blog','cate','tags')
     	action = '&keywords='+keywords
     elif tags:
         #Tags
     	articles = models.Article.objects.order_by('-id').filter(Q(tags__icontains = tags) | Q(content__icontains = tags)).values('times','cate__cateName','title','id','content')
     	action = '&tags='+tags
     else:
     	articles = models.Article.objects.order_by('-id').values('times','cate__cateName',
     				'hoter','id','content','title','tags')
                    
     
     for i in categories:
                        i.count = models.Article.objects.filter(cate = i.id).count()
     
     after_range_num = 2
     before_range_num = 9
     try:
     	page = int(request.GET.get('page',1))
     	if page < 1:
     		page = 1
     except ValueError:
     			page = 1
     paginator = Paginator(articles,6)
     try:
     	articleList = paginator.page(page)
     except(EmptyPage,InvalidPage,PageNotAnInteger):
     	articleList = paginator.page(1)
     if page >= after_range_num:
     	page_range = paginator.page_range[page-after_range_num:page + before_range_num]
     else:
     	page_range = paginator.page_range[0:int(page) + before_range_num]
     return render_to_response('index.html',locals())

def action(request):
    captions = common.caption()
    tagValues = common.tag()
    id = int(request.GET.get('action'))
    article = models.Article.objects.filter(id = id).values('times','cate__cateName',
     				'hoter','title','content','tags')
    title_one = article[0]['title']
    tag_one=article[0]['tags']
    cate_one = article[0]['cate__cateName']
    hoter_one = article[0]['hoter']
    hoterGo = int(hoter_one) + 1
    models.Article.objects.filter(id = id).update(hoter = hoterGo)

    times = article[0]['times']
#    times = time.strftime('%Y-%m-%d',time.localtime(article[0]['times']))
    content_one = article[0]['content']
     	
    next = models.Article.objects.order_by('id').filter(id__gt = id).values('id',
     				'title')[:1]
    if next:
     	next_id = next[0]['id']
     	next_caption = next[0]['title']
     
    previous = models.Article.objects.order_by('-id').filter(id__lt = id).values('id',
     				'title')[:1]
    if previous:
     	previous_id =  previous[0]['id']
     	previous_caption = previous[0]['title']
    return render_to_response('article.html',locals())

