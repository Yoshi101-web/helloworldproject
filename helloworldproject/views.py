from django.http import HttpResponse

def helloworldfunction(request):
    returnobject = HttpResponse('hello world')
    return returnobject

class HelloWorldView(templateView):
    template_name = 'hello.html'