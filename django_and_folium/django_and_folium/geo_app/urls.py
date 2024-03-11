from django.urls import path

from . import views


app_name = 'geoapp'


urlpatterns = [
    path('', views.index, name='index'),
    path('create-feature/', views.CreateFeature.as_view(), name='create-feature'),
    path('import-data/', views.import_data, name='import-data'),
    path('export-data/', views.export_data, name='export-data'),
]