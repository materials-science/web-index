from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import WebSite, Staff
from django.db.models import F
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def index_pagination(request):
    order_by = request.GET.get('order_by')
    page_number = request.GET.get('page')
    order_by = 'favorite' if order_by is None else order_by
    page_number = '0' if page_number is None else page_number
    
    sites_list = WebSite.objects.all().order_by('-'+order_by)
    paginator = Paginator(sites_list, 20)
    page_obj = paginator.get_page(page_number)

    staff_list = Staff.objects.all().order_by('-level')
    return render(request, 'index/sites_list.html', {'page_obj': page_obj, 'staff_list': staff_list})

@require_POST
def favorite(request, id):
    resp = {
        'code': '0',
        'msg': 'success'
    }
    try:
        WebSite.objects.all().filter(id=id).update(favorite=F('favorite') + 1)
    except Exception as e:
        resp['code'] = '1001'
        resp['msg'] = 'fail'
        resp['detail'] = str(e)
        
    return JsonResponse(resp)
