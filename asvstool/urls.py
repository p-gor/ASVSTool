from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='tool-home'),
    path('about/', views.about, name='tool-about'),
    path('project/', include([
        path('', views.project, name='tool-project'),
        path('<int:id>', views.details_project, name='tool-details'),
        ])),
    path('details_req/<int:id>/<int:id_state>', views.details_project_req, name='tool-details_req'),
    path('subsection/<pk>', views.subsection, name='tool-subsection'),
    path('tests/<pk>', views.tests, name='tool-test'),
]