from django.urls import path

from . import views


urlpatterns = [
    # HomePage
    path('', views.HomePage.as_view(), name='home'),

    # Main App Page
    path('seattle/', views.index, name='index'),

    # Importing Data
    path('import-hospitals-data', views.import_hospitals_data, name='import-hospitals-data'),
    path('import-schools-data', views.import_schools_data, name='import-schools-data'),
    path('import-libraries-data', views.import_libraries_data, name='import-libraries-data'),
    
    # Exporting Data
    path('export-hospitals-data', views.export_hospitals_data, name='export-hospitals-data'),
    path('export-schools-data', views.export_schools_data, name='export-schools-data'),
    path('export-libraries-data', views.export_libraries_data, name='export-libraries-data'),
    
]
