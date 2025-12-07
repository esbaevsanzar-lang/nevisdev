from django.db import models

class Kurs(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    data = models.DateTimeField(null=True, blank=True)
    create = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Sertificat(models.Model):
    title = models.CharField(max_length=20)
    desk= models.CharField(max_length=20)
    img = models.ImageField(upload_to="img/")


class Students(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    age = models.IntegerField(null=True)
    study_start = models.DateField(null=True)
    study_finish = models.DateField(null=True)
    category = models.ForeignKey(Kurs, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class WorkerCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    age = models.IntegerField(null=True)
    category = models.ForeignKey(WorkerCategory, on_delete=models.CASCADE, null=True, blank=True)
    start_work = models.DateTimeField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class StudyRequest(models.Model):
    full_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class JobRequest(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    position = models.CharField(max_length=255)
    salary_expectation = models.CharField(max_length=100)

    def str(self):
        return self.full_name

class Contacts(models.Model):
    email = models.EmailField()
    social = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=60)
    logo_comp = models.ImageField(upload_to='logo_comp/')

    def __str__(self):
        return self.email