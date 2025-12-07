from django.shortcuts import render
from rest_framework import generics
from .models import Kurs, Sertificat, Student, Worker, WorkerCategory, StudyRequest, JobRequest, Contacts
from .serializers import KursSerializer, SertificatSerializer, StudentSerializer, WorkerSerializer, WorkerCategorySerializer, StudyRequestSerializer, JobRequestSerializer, ContactsSerializer
from telegram_notify import send_telegram_message


class KursView(generics.ListCreateAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class SertificatView(generics.ListCreateAPIView):
    queryset = Sertificat.objects.all()
    serializer_class = SertificatSerializer

class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class WorkerCategoryView(generics.ListCreateAPIView):
    queryset = WorkerCategory.objects.all()
    serializer_class = WorkerCategorySerializer

class WorkerView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class StudyRequestCreate(generics.CreateAPIView):
    queryset = StudyRequest.objects.all()
    serializer_class = StudyRequestSerializer

class JobRequestCreate(generics.CreateAPIView):
    queryset = JobRequest.objects.all()
    serializer_class = JobRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        text = (
            f"Жаны жумушка отунмо келди! \n"
            f"ФИО: {instance.full_name}\n"
            f"Телефон: {instance.phone}\n"
            f"Email: {instance.email}\n"
            f"Кызматы: {instance.position}\n"
            f"Айлык Акы: {instance.salary_expectation}\n"
        )
        send_telegram_message(text)

class ContactsCreate(generics.CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer



