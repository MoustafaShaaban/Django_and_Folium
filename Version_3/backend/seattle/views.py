import folium
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib import messages

from tablib import Dataset

from .models import Hospital, School, Library
from .resources import HospitalResource, SchoolResource, LibraryResource


class HomePage(generic.TemplateView):
    """ Class used for displaying website's main page. """
    template_name = 'index.html'


def index(request):

    # Create folium basemap
    map = folium.Map(
        location=[47.6062100, -122.3320700],
        tiles='cartodbpositron',
        zoom_start=11,
        attr= 'Public Schools in Seattle'
    )

    # Add a second TileLayer to the basemap
    folium.TileLayer('cartodbdark_matter').add_to(map)

    
    # Add Schools Data
    schools = School.objects.all()

    schools_simple_markers = folium.FeatureGroup(name='Schools Simple Markers').add_to(map)

    for school in schools:
        locations = [school.latitude, school.longitude]
        folium.Marker(
            locations,
            icon=folium.Icon(icon = "graduation-cap", prefix='fa'),
            tooltip="School Name: " + str(school.name),
            popup="School Address :" + school.address,
    ).add_to(schools_simple_markers)

    schools_marker_cluster = folium.FeatureGroup(name='Schools Marker Cluster', show=False).add_to(map)

    marker_cluster = MarkerCluster()

    for school in schools:
        locations = [school.latitude, school.longitude]
        marker_cluster.add_child(
            folium.Marker(
                locations,
                icon=folium.Icon(icon = "graduation-cap", prefix='fa'),
                tooltip="School Name: " + str(school.name),
                popup="School Address :" + school.address,
            )
        ).add_to(schools_marker_cluster)
    
    ##################################################################################################

    # Add Libraries data:
    libraries = Library.objects.all()

    libraries_simple_markers = folium.FeatureGroup(name='Libraries Simple Markers', show=False).add_to(map)

    for library in libraries:
        locations = [library.latitude, library.longitude]
        folium.Marker(
            locations,
            icon=folium.Icon(icon = "book", prefix='fa'),
            tooltip="Library Name: " + str(library.name),
            popup="Library Address :" + library.address,
        ).add_to(libraries_simple_markers)

    libraries_marker_cluster = folium.FeatureGroup(name='Libraries Marker Cluster', show=False).add_to(map)

    marker_cluster = MarkerCluster()

    for library in libraries:
        locations = [library.latitude, library.longitude]
        marker_cluster.add_child(
            folium.Marker(
                locations,
                icon=folium.Icon(icon = "book", prefix='fa'),
                tooltip="Library Name: " + str(library.name),
                popup="Library Address :" + library.address,
            )
        ).add_to(libraries_marker_cluster)
    
    ##################################################################################################

    # Add Hospitals data
    hospitals = Hospital.objects.all()

    hospitals_simple_markers = folium.FeatureGroup(name='Hospitals Simple Markers', show=False).add_to(map)

    for hospital in hospitals:
        locations = [hospital.latitude, hospital.longitude]
        folium.Marker(
            locations,
            icon=folium.Icon(icon_color = "red", icon = "h-square", prefix='fa'),
            tooltip="Hospital Name: " + str(hospital.facility),
            popup="Hospital Address :" + hospital.address,
        ).add_to(hospitals_simple_markers)

    hospitals_marker_cluster = folium.FeatureGroup(name='Hospitals Marker Cluster', show=False).add_to(map)

    marker_cluster = MarkerCluster()

    for hospital in hospitals:
        locations = [hospital.latitude, hospital.longitude]
        marker_cluster.add_child(
            folium.Marker(
                locations,
                icon=folium.Icon(icon_color = "red", icon = "h-square", prefix='fa'),
                tooltip="Hospital Name: " + str(hospital.facility),
                popup="Hospital Address :" + hospital.address,
            )
        ).add_to(hospitals_marker_cluster)
    ##################################################################################################

    folium.LayerControl(position='bottomright').add_to(map)
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    map = map._repr_html_()

    context = {
        'map': map
    }

    return render(request, 'map.html', context)

########################################################################################################


def import_hospitals_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        hospital_resource = HospitalResource()
        dataset = Dataset()
        new_hospitals = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_hospitals.read().decode('utf-8'),format='csv')
            result = hospital_resource.import_data(dataset, dry_run=True)                                                                
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_hospitals.read().decode('utf-8'),format='json')
            # Testing data import
            result = hospital_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            hospital_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Data Imported Successfully.')

    return render(request, 'seattle/data/import_hospitals_data.html')



def export_hospitals_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        hospital_resource = HospitalResource()
        dataset = hospital_resource.export()

        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/hospitals.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/hospitals.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/hospitals.xls"'
            return response
        
    return render(request, 'seattle/data/export_hospitals_data.html')


def import_schools_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        school_resource = SchoolResource()
        dataset = Dataset()
        new_schools = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_schools.read().decode('utf-8'),format='csv')
            result = school_resource.import_data(dataset, dry_run=True)                                                                
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_schools.read().decode('utf-8'),format='json')
            # Testing data import
            result = school_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            school_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Data Imported Successfully.')

    return render(request, 'seattle/data/import_schools_data.html')



def export_schools_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        school_resource = SchoolResource()
        dataset = school_resource.export()

        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/schools.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/schools.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/schools.xls"'
            return response
        
    return render(request, 'seattle/data/export_schools_data.html')



def import_libraries_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        library_resource = LibraryResource()
        dataset = Dataset()
        new_libraries = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_libraries.read().decode('utf-8'),format='csv')
            result = library_resource.import_data(dataset, dry_run=True)                                                                
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_libraries.read().decode('utf-8'),format='json')
            # Testing data import
            result = library_resource.import_data(dataset, dry_run=True)


        if not result.has_errors():
            # Import now
            library_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Data Imported Successfully.')


    return render(request, 'seattle/data/import_library_data.html')



def export_libraries_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        library_resource = LibraryResource()
        dataset = library_resource.export()

        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/libraries.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/libraries.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="seattle/data/libraries.xls"'
            return response
        
    return render(request, 'seattle/data/export_library_data.html')