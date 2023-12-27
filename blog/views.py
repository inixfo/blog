from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, render


def home (request):
    return HttpResponseRedirect(reverse('app_blog:blog_list'))

