from .models import Log_event

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
    
        response = self.get_response(request)
    
        # print(response)
        print(request.user.username)
        print(request.method)
        print(request.META.get('HTTP_REFERER'))
        Log_event.objects.create(
	        user= request.user,
	        event_type= request.method,
	        router= request.META.get('HTTP_REFERER')
        )
        # Add user data in db....
        if request.method == 'POST':
            print(request.POST)
    
        # Code to be executed for each request/response after
        # the view is called.
    
        return response