from django.http import JsonResponse

class LikesMixin:
    """
    Evalua si el usuario ha dado like o dislike para actualizar su votación o crear una nueva
    También añade al contexto un contador de likes y dislikes para el objeto
    El modelo que herede el mixin deberá integrar en urls.py dos path:
        '<int:pk>/', SameView.as_view()...
        '<int:pk>/<int:choice>/', SameView.as_view()...
    """
    
    def get(self, request, *args, **kwargs):
        # Debemos implementar un sistema que impida
        # Que los bots repitan este proceso indefinidamente y evitar un ataque DDos.
        choice = kwargs.get('choice', None)

        if choice is not None:
            if request.user.is_authenticated:
                choice = True if choice else False
                
                object = self.get_object()
                like_object = object.likes.filter(user=request.user).first()

                if like_object:
                    if like_object.like == choice:
                        choice = None
                        like_object.delete()
                    else: 
                        like_object.like = choice
                        like_object.save()
                else:
                    object.likes.create(user=request.user, like=choice)

                # Debemos usar AJAX para este return
                # If response == True (Like) else False (Dislike)
                return JsonResponse({'response': choice})

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes'] = self.get_object().likes.filter(like=True).count()
        context['dislikes'] = self.get_object().likes.filter(like=False).count()

        return context