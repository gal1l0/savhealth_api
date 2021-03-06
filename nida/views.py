from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonSerializer,InsuranceSerializer,MedicalHistorySerializer,CurrentStatusSerializer
from .models import person,insurance_dt,medical_history,hospitals,current_status
#import json
# Create your views here.
class PersonView(APIView):
    def get(self,request,fPd):
        persons = get_object_or_404(person.objects.all(), fprint_data=fPd)
        # specify that persons can be many using the "many" param
        
        serializer = PersonSerializer(persons)

        return Response({"persons":serializer.data})

    def post(self,request):
        persons = person.objects.all()

        serializer = PersonSerializer(data=persons)
        if serializer.is_valid(raise_exception=True):
           person_save = persons.save()
        return Response({"sucess" : "person '{}' Saved".format(person_save.first_name)}
    )     


class InsuranceView(APIView):
    def get(self,request,fPd):
        insurances = get_object_or_404(insurance_dt.objects.all(), nid=fPd)
        # specify that persons can be many using the "many" param
        
        serializer = InsuranceSerializer(insurances)

        return Response({"insurances":serializer.data})

class MedicalHistoryView(APIView):
    def get (self,request,fPd):
        med = get_object_or_404(medical_history.objects.all(), nid=fPd)
        serializer = MedicalHistorySerializer(med)
        return Response({"Medical Records":serializer.data})

# class HospitalView(APIView):
#     def get(self, request, availabil):
#         med = get_object_or_404(hospitals.objects.all(),)

# class  HospitalView(APIView):
#     def post (self, request):

class currentStatusView(APIView):
    def post (self,request):
        cs = request.data.get('cs')
        cs_serializer = CurrentStatusSerializer(data=cs)
        if cs_serializer.is_valid(raise_exception=True):
            cs_saved = cs_serializer.save()

            return Response({"Sucess":"Current Status for '{}' sent success fully ".format(cs_saved.nid)})

    def get(self,request,fPd):
        cs = get_object_or_404(current_status.objects.all(), nid=fPd)
        # specify that persons can be many using the "many" param
        serializer = CurrentStatusSerializer(cs)
        return Response({"current status ":serializer.data})
        