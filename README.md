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

```
https://pypi.org/project/django-multiselectfield/
```



### DjangoTaggit

```
https://pypi.org/project/django-taggit/
```



### Django Hit-count

```
https://pypi.org/project/django-hitcount/
```



