from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Chapter(models.Model):
    chapter_title = models.CharField(max_length=256, default=None)

    def __str__(self):
        return self.chapter_title


class Subsection(models.Model):
    chapter_nr = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    subsection_name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.subsection_name


class Requirement(models.Model):
    subsection_nr = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    requirement_name = models.CharField(max_length=256, default=None)
    nist = models.CharField(max_length=10, blank=True, null=True, default=None)
    cwe = models.CharField(max_length=10, blank=True, null=True, default=None)
    lvl1 = models.BooleanField(default=True)
    lvl2 = models.BooleanField(default=True)
    lvl3 = models.BooleanField(default=True)
    stand2 = models.IntegerField(default=2) #Brak dokumentacji 0 - odrzucony 1 - do przeprowadzenia 2 - nie dotyczy
    stand3 = models.IntegerField(default=2) #Możliwość logowania/tworzenia kont 0 - odrzucony 1 - do przeprowadzenia 2 - nie dotyczy
    stand4 = models.IntegerField(default=2) #Opcja przetwarzania plików 0 - odrzucony 1 - do przeprowadzenia 2 - nie dotyczy
    stand5 = models.IntegerField(default=2) #Mechanizm zarządzania sesją 0 - cookies 1 - token 2 - nie dotyczy
    stand6 = models.IntegerField(default=2) #Używanie kodu zarządzalnego 0 - odrzucony 1 - do przeprowadzenia 2 - nie dotyczy
    stand7 = models.IntegerField(default=4) #Typ usługi sieciowej 0 - SOAP 1 - REST 2 - GraphQL lub inna 4 - nie dotyczy

    def __str__(self):
        return self.requirement_name


class Project(models.Model):
    project_name = models.CharField(max_length=256, default=None)
    date_made = models.DateTimeField(verbose_name="data_utworzenia", auto_now_add=True)
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    requirements = models.ManyToManyField(Requirement, through='ReqsProject')
    lvl1_project = models.BooleanField(default=True)
    lvl2_project = models.BooleanField(default=True)
    lvl3_project = models.BooleanField(default=True)
    stand2_project = models.BooleanField(default=True)  # Brak dokumentacji 0 - Brak 1 - Jest dokumentacja
    stand3_project = models.BooleanField(default=True)  # Możliwość logowania/tworzenia kont 0 - Nie 1 - Tak
    stand4_project = models.BooleanField(default=True)  # Opcja przetwarzania plików 0 - Nie ma takiej opcji 1 - Jest taka opcja
    stand5_project = models.IntegerField(default=0)  # Mechanizm zarządzania sesją 0 - cookies 1 - token 2 - inny
    stand6_project = models.BooleanField(default=True)  # Używanie kodu zarządzalnego 0 - Używany kod zarzadzalny 1 - Używany kod nie zarządzalny
    stand7_project = models.IntegerField(default=4)  # Typ usługi sieciowej 0 - SOAP 1 - REST 2 - GraphQL lub inna 4 - nie dotyczy

    def __str__(self):
        return self.project_name


class ReqsProject(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=True, blank=True) #0 - Odrzucony  1 - Przyjęty
    result = models.BooleanField(default=True, blank=True) #0 - Wynik negatywny 1 - Wynik pozytywny

    class Meta:
        unique_together = [['project', 'requirement']]


