from django.http import HttpResponse,JsonResponse,QueryDict
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import recordsSeralizer
from .models import records

# Create your views here.
@csrf_exempt
def records(request):
	if(request.method=='GET'):
		s=records.objects.all().values()
		slist=list(s)
		return HttpResponse(slist)
	else:
		return HttpResponse('Invalid Request Method : Valid Option is GET')

@csrf_exempt
def addRecordtudent(request):
	if(request.method=='POST'):
		data = JSONParser().parse(request)
		serializer = recordsSeralizer(data=data)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse("Record Updated Successfully")
		return HttpResponse('Record Saved')
	else:
		return HttpResponse('Invalid Request Method : Valid Option is POST')    