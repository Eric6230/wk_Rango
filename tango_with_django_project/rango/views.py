from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#request is a HttpRequest object
#each view should return a HttpResponse object
def index(request):
    # Note the key blodmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")
