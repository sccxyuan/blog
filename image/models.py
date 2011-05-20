#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin 



class ProfileBase(type):  
    def __new__(cls, name, bases, attrs):  
        module = attrs.pop('__module__')  
        parents = [b for b in bases if isinstance(b, ProfileBase)]  
        if parents:  
            fields = []  
            for obj_name, obj in attrs.items():  
                if isinstance(obj, models.Field): fields.append(obj_name)  
                User.add_to_class(obj_name, obj)  
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)  
            UserAdmin.fieldsets.append((name, {'fields': fields}))  
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)  
          
class Profile(object):  
    __metaclass__ = ProfileBase

  
GENDER_CHOICES = (
                  ('M', '男'),
                  ('F', '女'),
)
'''  
class MyProfile(Profile):  
    name=models.CharField(max_length=30,blank=True)
    tel=models.CharField('电话',max_length=20, blank=True, null=True)
    mobile = models.CharField('移动电话',max_length=20, blank=True, null=True)
    address = models.CharField( '家庭地址',max_length=100, blank=True, null=True)
    website = models.URLField( '个人主页',blank=True, null=True)
    birthday = models.DateField('生日',blank=True,null=True)
    gender = models.CharField('性别',max_length=1, choices=GENDER_CHOICES, blank=True)
    blog = models.URLField( blank=True, null=True)
    QQ = models.CharField('QQ',max_length=50, blank=True, null=True)
    MSN = models.CharField(max_length=50, blank=True, null=True)
    IM = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField('所在地',max_length=200, blank=True, null=True)
    country = models.CharField('国家',max_length=50, blank=True, null=True, default='中国')  
'''  
class MyProfile(models.Model):
    user = models.ForeignKey(User, unique=True, verbose_name='用户的额外信息')  
    name=models.CharField(max_length=30,blank=True)
    tel=models.CharField('电话',max_length=20, blank=True, null=True)
    mobile = models.CharField('移动电话',max_length=20, blank=True, null=True)
    address = models.CharField( '家庭地址',max_length=100, blank=True, null=True)
    website = models.URLField( '个人主页',blank=True, null=True)
    birthday = models.DateField('生日',blank=True,null=True)
    gender = models.CharField('性别',max_length=1, choices=GENDER_CHOICES, blank=True)
    blog = models.URLField( blank=True, null=True)
    QQ = models.CharField('QQ',max_length=50, blank=True, null=True)
    MSN = models.CharField(max_length=50, blank=True, null=True)
    IM = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField('所在地',max_length=200, blank=True, null=True)
    country = models.CharField('国家',max_length=50, blank=True, null=True, default='中国')  

    def serialize_fields(self):
        return [
                    'id',
                    'username',
                    'password',
                    'first_name',
                    'last_name',
                    'email',
                    'tel',
                    'mobile',
                    'address',
                    'website',
                    'birthday',
                    'gender',
                    'blog',
                    'QQ',
                    'MSN',
                    'IM',
                    'position',
                    'country',
                ]  
    def __unicode__(self):
        return '%s'%(self.user)
    def is_today_birthday(self):  
        return self.birthday.date() == datetime.date.today()

class Categories(models.Model):
    #orderId = models.IntegerField()
    cateName = models.CharField(max_length = 50)

    class Meta:
        db_table = 'categories'
        
    #def __str__(self): 输入中文不成功
    def __unicode__(self):
        return '%s'%(self.cateName)
        #return '%s %s' % (self.orderId,self.cateName)
     


class Article(models.Model):
    #blog=models.ManyToManyField(MyProfile)
    blog=models.ForeignKey(MyProfile)
    cate = models.ForeignKey(Categories)
    title=models.CharField(max_length=30)
    tags = models.CharField('标签',max_length=50)
    times = models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    hoter=models.IntegerField(blank=True,default=0)
    
    class Meta:
        db_table='Article'
    def __unicode__(self):
        return '%s'%(self.title)
    
 

class Comment(models.Model):
    name=models.CharField(max_length=30)
    content=models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s '%(self.name)