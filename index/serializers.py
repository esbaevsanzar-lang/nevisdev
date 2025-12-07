from rest_framework import serializers
from .models import *

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = "__all__"

class SertificatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertificat
        fields = "__all__"

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class WorkerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerCategory
        fields = "__all__"

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"

class StudyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model =StudyRequest
        fields = "__all__"

class JobRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRequest
        fields = "__all__"

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"