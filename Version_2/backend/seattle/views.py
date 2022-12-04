import folium
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder

from django.shortcuts import render
from django.views import generic

from .models import Hospital, School, Library


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

    for library in libraries:
        locations = [library.latitude, library.longitude]
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
