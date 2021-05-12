# Django novels.website

> Creado el 11-05-2021



Proyecto en construcción...



## Instalación

```bash
# Git bash
mkdir user.auth
git clone https://github.com/Estasleyendoesto/django.auth.git .
rm -rf .git

# Windows console
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
cd mysite
py manage.py runserver
```





## Notas de desarrollo

### Alternativa al shell de Django

Vincula en `urls.py` esta vista y en su navegador instalar algún plugin o addon para visualizar JSON.

```python
from django.http import HttpResponse
from django.core import serializers

def test(request):
    queryset = MyModel.objects.all()
    data   = serializers.serialize('json', queryset)
    return HttpResponse(data, content_type='application/json')
```



### Sistema de likes
Para habilitar los likes en un modelo, primero implementar la relación dentro de este
```python
from django.contrib.contenttypes.fields import GenericRelation
from ..likes.models import Like

class MyModel(...):
    ...
    likes = GenericRelation(Like, related_query_name='myModel') # Minúscula
```


Las operaciones que podemos realizar están detalladas aquí:

> https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/#reverse-generic-relations



Antes que un usuario de like a un objeto, primero debemos comprobar si este usuario ya ha dado like para negarlo
> Barajando la posibilidad de crear un mixin ClassView que se encargue automáticamente de hacer la comprobación e insertar los likes dentro del template

```python
from django.http import HttpResponse
from .models import Novel

def myView(request):
    user = request.user
    novel = Novel.objects.get(pk=1)

    if novel.likes.filter(user=user).first():
        return HttpResponse('Ya has dado like')
    
    novel.likes.create(user=user, like=False)
    return HttpResponse('Like completado')

```





## Librerías necesarias

### Pillow

This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

```
https://pypi.org/project/Pillow/
```



### Django Simple Captcha

Django Simple Captcha is an extremely simple, yet highly customizable Django application to add captcha images to any Django form.

```
https://pypi.org/project/django-simple-captcha/
```



### Google reCaptcha

reCAPTCHA uses an advanced risk analysis engine and adaptive challenges to keep malicious software from engaging in abusive activities on your website. Meanwhile, legitimate users will be able to login, make purchases, view pages, or create accounts and fake users will be blocked.

El primer millón al mes es gratis, luego se abona 1€ por 1000 visitas.

```
https://www.google.com/recaptcha/admin/create
https://developers.google.com/recaptcha/docs/v3
```



### Django Cleanup

Automatically deletes files for `FileField`, `ImageField` and subclasses. When a `FileField`’s value is changed and the model is saved, the old file is deleted. When a model that has a `FileField` is deleted, the file is also deleted. A file that is set as the `FileField`’s default value will not be deleted.

```
https://pypi.org/project/django-cleanup/
```



### Django Multiselectfield

A new model field and form field. With this you can get a multiple select from a choices. Stores to the database as a CharField of comma-separated values.

```
https://pypi.org/project/django-multiselectfield/
```



### DjangoTaggit

django-taggit a simpler approach to tagging with Django. Add "taggit" to your INSTALLED_APPS then just add a TaggableManager to your model and go

```
https://pypi.org/project/django-taggit/
```



### Django Hit-count

Basic app that allows you to track the number of hits/views for a particular object.

```
https://pypi.org/project/django-hitcount/
```



