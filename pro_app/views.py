from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')

def contacts(request):

    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        #print(name)
        email = request.POST['email']
        subject = request.POST['subject']

        return render(request,'contact.html',{'name':name})

    else:
        return render(request,'contact.html')
