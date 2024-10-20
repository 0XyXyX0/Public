from django.shortcuts import render

def ip_adress_processor(request):
    return {"ip_adress": request.META['REMOTE_ADDR']}

def index(request):
    return render(request, 'index.html', ip_adress_processor(request))

def user_info(request):
    context = {
        'username': 'levani',
        'email': 'lburdiladze7@gmail.com',
        'password': 'rame',
        'height': 185
    }
    return render(request, 'user.html', context=context)