import folium
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder

from django.shortcuts import render
from django.views import generic

from .models import Hospital, School, Library


class HomePage(generic.TemplateView):
    """ Class used for displaying website's main page. """
    template_name = 'index.html'



def schools_simple_markers(request):
    """Function returns simple markers using Folium."""
    schools = School.objects.all()

    map = folium.Map(
        location=[47.6062100, -122.3320700],
        tiles='cartodbpositron',
        zoom_start=11,
        attr= 'Public Schools in Seattle'
    )

    # Add Full screen functionality to the map
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    # Loop through each data row in the database table:
    for school in schools:
        locations = [school.latitude, school.longitude]
        folium.Marker(
            locations,
            icon=folium.Icon(icon = "book", prefix='fa'),
            tooltip="School Name: " + str(school.name),
            popup="School Address :" + school.address,
        ).add_to(map)

    map = map._repr_html_()

    context = {
        'map': map
    }

    return render(request, 'seattle/schools/simple_markers.html', context)


def schools_marker_cluster(request):
    """Function returns marker cluster using Folium."""
    schools = School.objects.all()

    map = folium.Map(
        location=[47.6062100, -122.3320700],
        tiles='cartodbpositron',
        zoom_start=11,
        attr='Public Schools in Seattle'
    )

    marker_cluster = MarkerCluster()

    for school in schools:
        locations = [school.latitude, school.longitude]
        marker_cluster.add_child(
            folium.Marker(
                locations,
                tooltip="School Name: " + str(school.name),
                popup="School Address :" + school.address,
            )
        )

    map.add_child(marker_cluster)
    
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    map = map._repr_html_()

    context = {'map': map}

    return render(request, 'seattle/schools/marker_cluster.html', context)


def hospitals_simple_markers(request):
    """Function returns simple markers using Folium."""
    hospitals = Hospital.objects.all()

    map = folium.Map(
        location=[47.6062100, -122.3320700],
        tiles='cartodbpositron',
        zoom_start=11,
        attr= 'Public Schools in Seattle'
    )

    # Add Full screen functionality to the map
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    # Loop through each data row in the database table:
    for hospital in hospitals:
        locations = [hospital.latitude, hospital.longitude]
        folium.Marker(
            locations,
            icon=folium.Icon(icon_color = "red", icon = "h-square", prefix='fa'),
            tooltip="Hospital Name: " + str(hospital.facility),
            popup="Hospital Address :" + hospital.address,
        ).add_to(map)


    map = map._repr_html_()

    context = {
        'map': map
    }

    return render(request, 'seattle/hospitals/simple_markers.html', context)


def hospitals_marker_cluster(request):
    """Function returns marker cluster using Folium."""
    hospitals = Hospital.objects.all()

    map = folium.Map(
        location=[47.6062100, -122.3320700],
        tiles='cartodbpositron',
        zoom_start=11,
        attr='Public Schools in Seattle'
    )

    marker_cluster = MarkerCluster()

    for hospital in hospitals:
        locations = [hospital.latitude, hospital.longitude]
        marker_cluster.add_child(
            folium.Marker(
                locations,
                tooltip="Hospital Name: " + str(hospital.facility),
                popup="Hospital Address :" + hospital.address,
            )
        )

    map.add_child(marker_cluster)

    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    map = map._repr_html_()

    context = {'map': map}

    return render(request, 'seattle/hospitals/marker_cluster.html', context)


def libraries_simple_markers(request):
    """Function returns simple markers using Folium."""
    libraries = Library.objects.all()

    map = folium.Map(
        location=[47.6062100, -122.3320700],
        tiles='cartodbpositron',
        zoom_start=11,
        attr= 'Public Schools in Seattle'
    )

    # Add Full screen functionality to the map
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    # Loop through each data row in the database table:
    for library in libraries:
        locations = [library.latitude, library.longitude]
        folium.Marker(
            locations,
            icon=folium.Icon(icon = "book", prefix='fa'),
            tooltip="Library Name: " + str(library.name),
            popup="Library Address :" + library.address,
        ).add_to(map)


    map = map._repr_html_()

    context = {
        'map': map
    }

    return render(request, 'seattle/schools/simple_markers.html', context)


def libraries_marker_cluster(request):
    """Function returns marker cluster using Folium."""
    libraries = Library.objects.all()

    map = folium.Map(
        location=[47.6062100, -122.3320700],
        tiles='cartodbpositron',
        zoom_start=11,
        attr='Public Schools in Seattle'
    )

    marker_cluster = MarkerCluster()

    for library in libraries:
        locations = [library.latitude, library.longitude]
        marker_cluster.add_child(
            folium.Marker(
                locations,
                tooltip="Library Name: " + str(library.name),
                popup="Library Address :" + library.address,
            )
        )

    map.add_child(marker_cluster)

    # Add Some Folium plugins to the map
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    map = map._repr_html_()

    context = {'map': map}

    return render(request, 'seattle/libraries/marker_cluster.html', context)