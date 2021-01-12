from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tool-home'),
    path('about/', views.about, name='tool-about'),
    path('project/', views.project, name='tool-project'),
    path('subsection/<pk>', views.subsection, name='tool-subsection'),
    path('tests/<pk>', views.tests, name='tool-test'),
]