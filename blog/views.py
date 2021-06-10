from datetime import datetime
from typing import ContextManager
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.urls.resolvers import _PATH_PARAMETER_COMPONENT_RE
from .models import Post
from django.template import loader
from django.views.decorators.http import require_http_methods, require_GET, require_safe
# Create your views here.

@require_http_methods(['GET'])
def index(request):
    latest_post_list = Post.objects.order_by('-publish')[:5]
    #output = ' , \n'.join([p.slug for p in latest_post_list])
    template = loader.get_template('index.html')
    context = {'posts':latest_post_list,}
    return HttpResponse(template.render(context, request))

@require_safe
def detail(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    context ={'post':post,}
    return render(request, 'detail.html', context)

@require_GET
def archive_year(request, year):
    year_post = get_list_or_404(Post, publish__year=year)
    context = {
        'posts':year_post,
    }

    return render(request, 'archive.html', context)