from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello World</h1>")

# This view function returns a simple HTML response with "Hello World" when accessed.
# It is mapped to the root URL of the 'hello' app in the URL configuration.