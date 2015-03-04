#coding:utf-8
from django.http import HttpResponse#这个函数用来处理返回
from django.shortcuts import render_to_response
from .models import Text,tImage,company,Image
import datetime
from django.forms.models import modelform_factory
from django.template import RequestContext
def upload(request):
	image_form=modelform_factory(Image)
	a=image_form(request.POST,request.FILES)
	if a.is_valid():
		img=a.save()
		return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('/media/%s').closest('.mce-window').find('.mce-primary').click();</script>" % img.img)
	return HttpResponse("")
def time(request):
	return HttpResponse(str(datetime.datetime.now()))
def home(request):
	a=Text.objects.get(id=1)
	b=tImage.objects.get(id=1)
	c=company.objects.all()[:8]
	all_img=tImage.objects.all()

	d={"a":a,"b":b,"c":c}
	for i in all_img:
		d[i.name]=i.img
	return render_to_response('index.html',d,context_instance=RequestContext(request))
def lc(request):
	return render_to_response('lc.html')
def fd(request):
	all_img=tImage.objects.all()
	d={}
	for i in all_img:
		d[i.name]=i.img
	return render_to_response('fd.html',d)