from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),

    path('schools/simple-markers/', views.schools_simple_markers, name='schools-simple-markers'),
    path('schools/marker-cluster/', views.schools_marker_cluster, name='schools-marker-cluster'),

    path('hospitals/simple-markers/', views.hospitals_simple_markers, name='hospitals-simple-markers'),
    path('hospitals/marker-cluster/', views.hospitals_marker_cluster, name='hospitals-marker-cluster'),

    path('libraries/simple-markers/', views.libraries_simple_markers, name='libraries-simple-markers'),
    path('libraries/marker-cluster/', views.libraries_marker_cluster, name='libraries-marker-cluster'),
]
