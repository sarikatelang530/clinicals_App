from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientListView.as_view(),name='index'),
    path('create/', views.PatientCreateView.as_view()),
    path('update/<int:pk>/', views.PatientUpdateView.as_view()),
    path('delete/<int:pk>/', views.PatientDeleteView.as_view()),
    path('addData/<int:pk>/', views.addData),
    path('analyse/<int:pk>/', views.analyse),

]

