from django.urls import path
from .views import *

urlpatterns = [
    path("kurs/", KursView.as_view()),
    path("sertificat/", SertificatView.as_view()),
    path("student/", StudentView.as_view()),
    path("worker/", WorkerView.as_view()),
    path("workercategory/", WorkerCategoryView.as_view()),
    path("study/", StudyRequestCreate.as_view()),
    path("job/", JobRequestCreate.as_view()),
    path("contacts/", ContactsCreate.as_view()),
]