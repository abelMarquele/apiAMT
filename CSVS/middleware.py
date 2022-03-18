from .models import Log_event
from django.contrib.auth.models import User

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
    
        response = self.get_response(request)
    
        #print(request.user.username)
        # print(request.method)
        # print(request.META.get('HTTP_REFERER'))
        if request.META.get('PATH_INFO') != '/logout/' and request.META.get('PATH_INFO') != '/login/' and request.META.get('PATH_INFO') != '/admin/login/' and request.META.get('PATH_INFO') != '/admin/logout/':
            if request.user.is_authenticated:
                Log_event.objects.create(
                    user=  User.objects.get(id=int(request.user.id)),
                    event_type= request.method,
                    router= request.META.get('HTTP_REFERER')
                )
                # print('Dentro do If')
                # print(request.META.get('HTTP_REFERER'))
                # print(request.META.get('PATH_INFO'))
        # else:
        #     print('Dentro do Else')
        # # Add user data in db....
        if request.method == 'POST':
            request.POST
    
        # Code to be executed for each request/response after
        # the view is called.
    
        return response