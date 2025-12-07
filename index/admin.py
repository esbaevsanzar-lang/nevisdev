from django.contrib import admin
from .models import *

@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    model = Kurs

@admin.register(Sertificat)
class SertificatAdmin(admin.ModelAdmin):
    model = Sertificat

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    model = Worker

@admin.register(WorkerCategory)
class CategoryAdmin(admin.ModelAdmin):
    model = WorkerCategory

@admin.register(StudyRequest)
class StudyRequest(admin.ModelAdmin):
    model = StudyRequest

@admin.register(JobRequest)
class JobRequest(admin.ModelAdmin):
    model = JobRequest

@admin.register(Contacts)
class Contacts(admin.ModelAdmin):
    model = Contacts