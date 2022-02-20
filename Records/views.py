from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import Records
from .serializers import RecordSerializer


class RecordView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = RecordSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if(request.method == 'GET'):
            r = Records.objects.all().values().order_by('-timestamp')
            rlist = list(r)
            return HttpResponse(rlist)
        else:
            return HttpResponse('Invalid Request Method : Valid Option is GET')