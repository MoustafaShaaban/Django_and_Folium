import folium
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder, Search

from .models import Feature


def basemap(request):
    map = folium.Map(
        tiles='cartodbdark_matter',
        attr= 'Public Schools in Seattle'
    )

    features = Feature.objects.all()

    features_layer = folium.FeatureGroup(name='Features Layer').add_to(map)

    for feature in features:
        locations = [feature.latitude, feature.longitude]
        folium.Marker(
            locations,
            tooltip= str(feature.name) + ", " + str(feature.type),
            popup= feature.description
        ).add_to(features_layer)

    folium.TileLayer('cartodbpositron').add_to(map)

    folium.LayerControl(position='bottomright').add_to(map)
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    

    map = map._repr_html_()

    context = {
        'map': map
    }

    return context