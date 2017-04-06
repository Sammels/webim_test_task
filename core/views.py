from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from core.vk_api import vk_auth, get_access_token, get_info


def auth(request):
    return HttpResponseRedirect(vk_auth())


def get_token(request):
    if 'code' in request.GET:
        code = request.GET.get('code')
        tokens = get_access_token(code)
        access_token = tokens.get('access_token')
        user_id = tokens.get('user_id')
        user, friends = get_info(access_token, user_id)
        return render(request, 'webim_test.html', {'user': user, 'friends': friends})