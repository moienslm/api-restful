from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Author, Post
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('hi girlsssss!')

@csrf_exempt

def all_posts(request):
    all_posts = Post.objects.all()
    all_posts_serialized = serializers.serialize('json', all_posts)
    all_posts_json = json.loads(all_posts_serialized)
    data = json.dumps(all_posts_json)
    return HttpResponse(data)

@csrf_exempt
def insert_post(request):
    try:
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = Author.objects.get(pk=1)

        post_instance = Post()
        post_instance.title = title
        post_instance.description = description
        post_instance.author = author
        post_instance.save()

        return HttpResponse('200')
    except:
        return HttpResponse('not ok!')



@csrf_exempt
def update_post(request):
    try:
        id = request.POST.get('id')
        title = request.POST.get('title')
        description = request.POST.get('description')

        Post.objects.filter(id = id).update(title=title, description = description)
        return HttpResponse('200')
    except:
        return HttpResponse('not ok is!')


@csrf_exempt
def delete_post(request):
    try:
        id = request.POST.get('id')

        Post.objects.filter(id = id).delete()
        return HttpResponse('200')
    except:
        return HttpResponse('not ok is!')
