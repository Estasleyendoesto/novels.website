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


### Rutas con slug
Se va a cambiar el buscador por id a uno por slug (en el caso de las novelas y usermane).
Debemos primero poner que el username o el título de la novela sea único y un max_length
```python
>>> from django.template.defaultfilters import slugify
>>> slugify("b b b b")
u'b-b-b-b'
>>>
```

Podemos adherirlo directamente al modelo interceptando el método save()
```python
class Test(models.Model):
    q = models.CharField(max_length=30)
    s = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.s = slugify(self.q)
        super(Test, self).save(*args, **kwargs)
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
#### Nota del desarrollador:

Actualmente se ha creado un mixin llamado LikesMixin que hace precisamente este trabajo. Devuelve al contexto un contador de Likes y Dislikes y evalúa una votación del usuario para actualizar su estado o crear un nuevo registro. Para activarlo, una vista **DetailView** debe hederarlo antes que nada.
> No funciona con TemplateView o cualquier otra vista basada en clases

> El contexto devuelve: `likes`, `dislikes` como integers para el template

> Cuando el usuario haga like / dislike devolverá un Json con una respuesta (Debemos usar AJAX en este caso)
```python
from ..likes.mixins import LikesMixin

class MyView(LikesMixin, DetailView):
    pass
```



### Sistema contador de visitas

Implementado un sistema para contar las visitas de cualquier objeto con `DetailView` o `UpdateView` mediante un mixin `HitsMixin`. Es necesario habilitar la funcionalidad añadiendo al modelo una relación genérica.

```python
from django.contrib.contenttypes.fields import GenericRelation
from ..hits.models import Hit

class MyModel(...):
    ...
    hits = GenericRelation(Hit, related_query_name='myModel') # Minúscula
```



La vista que implemente el mixin tiene que heredad de `HitsMixin` y puede combinarse junto a cualquier otro mixin.

> `HitsMixin` añade al contexto un contador de visitas totales `hits`
>
> Con el atributo `self.hit` podemos acceder al contador de visitas que apunta al objeto 

```python
from django.views.generic.detail import DetailView

from .models import Novel
from ..hits.mixins import HitsMixin
from ..likes.mixins import LikesMixin

class NovelView(HitsMixin, LikesMixin, DetailView):
    template_name = 'novels/novel.html'
    context_object_name = 'novel'
    model = Novel
```



Mediante `manage.py` podemos limpiar todos los registros en  `HitsLog` pasado x tiempo. Por defecto limpiará todos los registros con una antigüedad superior a 30 días. Para cambiar la antigüedad debemos añadir en `settings.py` la variable:

```python
KEEP_HITSLOGS_IN_DB = {'days': 30}
```

> Estamos usando `datetime.timedelta` para definir el tiempo por lo que podemos definir segundos, horas, meses, etc. Mirar en la documentación de `timedelta`



El comando que usaremos para limpiar los registros es:

```python
py manage.py clean_hits
```

> Se intenta conseguir que con **`cronjobs`** se automatice la limpieza periódica. Por el momento no hay solución.
#### Notas del desarrollador
Es un coñazo implementar crons porque todos los repositorios están anticuados y la única alternativa a esto sería usar Celerys junto con RabbitMQ y es otro coñazo de instalación peor que el anterior. Así que, e ideando alternativas creativas, se ha añadido dentro del panel administrador de Django en el modelo de HitsLog una acción para eliminar todos los registros que extrae de `settings.py`. Eso sí, primero hay que seleccionar todos los registros antes de ejecutar la acción que ya viene seleccionada por defecto.

> Celerys y RabbitMQ su uso principal es cuando queramos implementar un chat para los usuarios en tiempo real o algo similar ya que usa un servidor aparte instalado en la máquina que gestiona demonios ejecutándose concurrentemente. RabbitMQ es ese servidor y Celerys lo conecta con nuestras vistas en Django.






## Librerías necesarias
### Django Compressor
Comprime css en un solo bundle con un hash y lo mismo para los scripts. Debemos habilitar la compresión offline para que se almacene en caché y así no se tenga que comprimir cada vez que un usuario haga un request. Otra gran virtud que tiene es la de compilar JS y comprimirlo, además de compilar SASS o LESS y comprimirlo.
Tiene soporte por si insertarmos dentro de los scripts datos desde Django como `{{ name }}`.
```
https://github.com/django-compressor/django-compressor/
```
> Ver lo demás en la documentación

### Django node assets
Si no tengo entendido mal (además de ser muy sencillo su configuración interna, genial para mantenerlo si el autor deja de hacerlo), esta librería nos permite
importar los assets que descargamos desde node para ser usados por Django como si importáramos cualquier otra librería estática. Podría ser posible usarlo con
el Django Compressor, faltaría experimentar.
> https://github.com/whitespy/django-node-assets


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



