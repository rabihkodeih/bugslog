# Create your views here.
from django.http import HttpResponse

def testpage(request):
    return HttpResponse('this is the test page of bugslog.com')