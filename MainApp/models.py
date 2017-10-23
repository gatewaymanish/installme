
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# The header of every installation guide and will be one for number of steps
class SetupTemplate(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)
    productName = models.CharField(max_length=100, null=True, blank=True)
    platformType = models.CharField(max_length=100, null=True, blank=True)
    version = models.CharField(max_length=100, null=True, blank=True)
    minimumRequirement = models.TextField(max_length=300, null=True, blank=True)
    precautions = models.CharField(max_length=200, null=True, blank=True)
    approxTotalTimeReqd = models.IntegerField(default=0)
    refImage = models.ImageField(blank=True,null=True)
    creationTime = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    numOfUpdates = models.IntegerField(default=0)
    numOfViews = models.IntegerField(default=0)
    expertiseLevel = models.CharField(max_length=200,blank=True,null=True)
    downloadLink = models.CharField(max_length=200,blank=True, null=True)
    officialSite = models.CharField(max_length=200,blank=True, null=True)
    wikipage = models.CharField(max_length=200,blank=True, null=True)
    youtubeChannel = models.CharField(max_length=200,blank=True, null=True)
    stackoverflow = models.CharField(max_length=200,blank=True, null=True)
    githubRepo = models.CharField(max_length=200,blank=True, null=True)



    def __unicode__(self):
        return str(self.category) + ": " + str(self.productName) + " " + str(self.version) + " " + str(self.platformType)

    class Meta:
        ordering = ('productName',)


# The steps will me many for single SetupTemplate
class Steps(models.Model):
    stepNum = models.IntegerField(default=1)   # not primary key, for indexing only
    stepTitle = models.CharField(max_length=100,null=True,blank=True)
    codeSnip = models.CharField(max_length=500,null=True,blank=True)
    stepDesc = models.TextField(max_length=1000,null=True,blank=True)
    stepTimeReqd = models.IntegerField(default=0)
    stepImage = models.ImageField(default=None,null=True,blank=True)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    setup = models.ForeignKey(SetupTemplate,on_delete=models.CASCADE,default="")

    def __unicode__(self):
        return str(self.stepNum) +': ' + str(self.stepTitle)

    class Meta:
        ordering = ('stepNum',)



    # def get_sample_by_order(self):
    #     if self.setuptemplate_set.count():
    #         return self.setuptemplate_set.order_by('id')[0]

