from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, WebSite, Staff
from django.db.models import F
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from web_index import utils


def index_pagination(request):
    _type = request.GET.get('type')
    order_by = request.GET.get('order_by')
    page_number = request.GET.get('page')
    order_by = 'favorite' if order_by is None else order_by
    page_number = '0' if page_number is None else page_number

    # sites
    if _type == 'site':
        request.session['site_page'] = page_number
        site_page_number = page_number
    else:
        site_page_number = request.session.get('site_page', 0)
    sites_list = WebSite.objects.all().order_by('-'+order_by)
    paginator = Paginator(sites_list, 12)
    page_obj = paginator.get_page(site_page_number)

    # posts
    if _type == 'post':
        request.session['post_page'] = page_number
        post_page_number = page_number
    else:
        post_page_number = request.session.get('post_page', 0)
    posts_list = Post.objects.all().order_by('-'+order_by)
    posts_paginator = Paginator(posts_list, 2)
    posts_page_obj = posts_paginator.get_page(post_page_number)

    staff_list = Staff.objects.all().order_by('-level')

    client_ip = utils.get_ip_address(request)
    return render(request, 'index/sites_list.html', {
        'page_obj': page_obj,
        'posts_page_obj': posts_page_obj,
        'staff_list': staff_list,
        'is_internal_ip': utils.is_internal_ip(client_ip),
        'ip': client_ip})


@require_POST
def site_favorite(request, id):
    check_session = request.session.get('site_favorite')
    if check_session:
        return JsonResponse({
            'code': '-1',
            'msg': 'favorited'
        })
    resp = {
        'code': '0',
        'msg': 'success'
    }
    try:
        WebSite.objects.all().filter(id=id).update(favorite=F('favorite') + 1)
        request.session['site_favorite'] = True
    except Exception as e:
        resp['code'] = '1001'
        resp['msg'] = 'fail'
        resp['detail'] = str(e)

    return JsonResponse(resp)


@require_POST
def post_favorite(request, id):
    check_session = request.session.get('post_favorite')
    if check_session:
        return JsonResponse({
            'code': '-1',
            'msg': 'favorited'
        })
    resp = {
        'code': '0',
        'msg': 'success'
    }
    try:
        Post.objects.all().filter(id=id).update(favorite=F('favorite') + 1)
        request.session['post_favorite'] = True
    except Exception as e:
        resp['code'] = '1001'
        resp['msg'] = 'fail'
        resp['detail'] = str(e)

    return JsonResponse(resp)
