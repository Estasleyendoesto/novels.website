# Django novels.website

> Creado el 01-05-2021



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

#### Pillow

<img src="https://warehouse-camo.ingress.cmh1.psfhosted.org/03c911d36c5cddd9da826125407e4f65a04de2e1/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f707974686f6e2d70696c6c6f772f70696c6c6f772d6c6f676f2f6d61737465722f70696c6c6f772d6c6f676f2d323438783235302e706e67" style="zoom: 50%;" />

This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

```
https://pypi.org/project/Pillow/
```



#### Django Simple Captcha

<img src="https://warehouse-camo.ingress.cmh1.psfhosted.org/6a9fc14c93906e0cc0bf2cd0ad3a9f9bd61aecda/687474703a2f2f646a616e676f2d73696d706c652d636170746368612e72656164746865646f63732e696f2f656e2f6c61746573742f5f696d616765732f63617074636861332e706e67" style="zoom: 80%;" />

Django Simple Captcha is an extremely simple, yet highly customizable Django application to add captcha images to any Django form.

```
https://pypi.org/project/django-simple-captcha/
```



### Google reCaptcha

<img src="https://www.google.com/recaptcha/about/images/reCAPTCHA-logo@2x.png" style="zoom:33%;" />

reCAPTCHA uses an advanced risk analysis engine and adaptive challenges to keep malicious software from engaging in abusive activities on your website. Meanwhile, legitimate users will be able to login, make purchases, view pages, or create accounts and fake users will be blocked.

El primer millón al mes es gratis, luego se abona 1€ por 1000 visitas.

```
https://www.google.com/recaptcha/admin/create
https://developers.google.com/recaptcha/docs/v3
```



#### Django Cleanup

Automatically deletes files for `FileField`, `ImageField` and subclasses. When a `FileField`’s value is changed and the model is saved, the old file is deleted. When a model that has a `FileField` is deleted, the file is also deleted. A file that is set as the `FileField`’s default value will not be deleted.

```
https://pypi.org/project/django-cleanup/
```



#### Django Multiselectfield

```
https://pypi.org/project/django-multiselectfield/
```



#### DjangoTaggit

```
https://pypi.org/project/django-taggit/
```



#### Django Hit-count

```
https://pypi.org/project/django-hitcount/
```



