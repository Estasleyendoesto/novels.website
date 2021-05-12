from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers


from .models import Novel
# from ..likes.models import Like
from ..users.models import User

def test(request):
    obj = Novel.objects.get(pk=1)
    qs = obj.likes.all()
    data = serializers.serialize('json', qs)

    print('--------------->', request.META.get('HTTP_USER_AGENT'))

    return HttpResponse(data, content_type='application/json')

def savetest(request):
    user = request.user
    novel = Novel.objects.get(pk=1)

    # novel.likes.clear()
    # n = novel.likes.filter(user=user).first()   # Coprueba si existe usuario

    # if n:
        # f = 'existe'
    # else:
        # f = 'no existe'

    # novel.likes.create(user=user, like=False)       # Crea likes
    # s = novel.likes.all()
    # print('-------------------->', f)
    msg = 'Todo ok'

    # msg = novel.likes.filter(user=user)


    return HttpResponse(msg)