from django.shortcuts import render, HttpResponse


# Create your views here.
def indexPage(request):
    return render(request, 'index.html')



def aboutUs(request):
    return HttpResponse("เกี่ยวกับฉัน")


def contactUs(request):
    return HttpResponse("ติดต่อฉัน")