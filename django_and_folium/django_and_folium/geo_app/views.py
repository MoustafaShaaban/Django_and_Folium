import folium
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder
from tablib import Dataset

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from .resources import FeatureResource
from .models import Feature
from .utils import basemap


def index(request):
    map = basemap(request)
    return render(request, 'geoapp/map.html', map)


def map_features(request):
    map = folium.Map(
        tiles='cartodbdark_matter',
        attr= 'Public Schools in Seattle'
    )

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

    return render(request, 'geoapp/create_feature.html', context)


class CreateFeature(LoginRequiredMixin, generic.CreateView):
    model = Feature
    fields = ['name', 'type', 'description', 'latitude', 'longitude']
    template_name = 'geoapp/create_feature.html'
    success_url = reverse_lazy('geoapp:index')

    def get_context_data(self, **kwargs):
        map = folium.Map(
        tiles='cartodbdark_matter',
        attr= 'Geoapp built with Django and Folium'
    )

        folium.TileLayer('cartodbpositron').add_to(map)

        folium.LayerControl(position='bottomright').add_to(map)
        Fullscreen().add_to(map)
        LocateControl().add_to(map)
        Geocoder().add_to(map)
        folium.LatLngPopup().add_to(map)

        map = map._repr_html_()
        context = super().get_context_data(**kwargs)
        context['map'] = map
        return context



@login_required
def import_data(request):

    if request.method == 'POST':
        feature_resource = FeatureResource()
        dataset = Dataset()
        new_features = request.FILES.get('importData')

        imported_data = dataset.load(new_features.read().decode('latin1'))
        result = feature_resource.import_data(imported_data, dry_run=True)

        if not result.has_errors():
            # Import now
            feature_resource.import_data(imported_data, dry_run=False)
            messages.success(request, 'Data Imported Successfully.')

    return render(request, 'geoapp/import_data.html')


@login_required
def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST.get('file-format')
        feature_resource = FeatureResource()
        dataset = feature_resource.export()
        

        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported-data/data.csv"'
            return response
        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported-data/data.json"'
            return response
        
        elif file_format == 'XLS':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported-data/data.xls"'
            return response
    
    return render(request, 'geoapp/export_data.html')



