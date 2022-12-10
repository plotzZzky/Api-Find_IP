import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .ip import get_ip_data, find_ips_from_txt, find_ips_from_json


def home(request):
    return redirect(request, '/ip')


@csrf_exempt
def show_ip(request):
    if request.method == 'GET':
        data = False
        return render(request, 'ip.html', {'data': data})
    else:
        ip = request.POST['ip']
        data = get_ip_data(ip)
        return render(request, 'ip.html', {'data': data})


def show_ips(request):
    if request.method == 'GET':
        return render(request, 'ips.html', {'data': None})
    else:
        file = request.FILES['file']
        data = find_ips_from_txt(file)
        return render(request, 'ips.html', {'data': data})


@csrf_exempt
def show_ip_args(request, ip):
    data = get_ip_data(ip)
    return JsonResponse(data)


@csrf_exempt
def show_ips_args(request):
    query = json.loads(request.body)
    ips = query['ips']
    data = find_ips_from_json(ips)
    return JsonResponse(data, safe=False)


def about(request):
    return render(request, 'about.html')


# Errors

def error_400(request, exception=None):
    return render(request, 'errors/400.html', {})


def error_403(request, exception=None):
    return render(request, 'errors/403.html', {})


def error_404(request, exception):
    return render(request, 'errors/404.html', {})


def error_405(request):
    return render(request, 'errors/405.html', {})


def error_500(request, exception=None):
    return render(request, 'errors/500.html', {})
