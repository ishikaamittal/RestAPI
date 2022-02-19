from django.http import HttpResponse,JsonResponse,QueryDict
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import recordsSeralizer
from .models import records

# Create your views here.
@csrf_exempt
def recordsView(request):
	if(request.method=='GET'):
		r=records.objects.all()
		rlist=list(r)
		return HttpResponse(rlist)
	else:
		return HttpResponse('Invalid Request Method : Valid Option is GET')

@csrf_exempt
def addRecord(request):
	if(request.method=='POST'):
		data = JSONParser().parse(request)
		serializer = recordsSeralizer(data=data)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse("Record Updated Successfully")
		return HttpResponse('Record Saved')
	else:
		return HttpResponse('Invalid Request Method : Valid Option is POST')    