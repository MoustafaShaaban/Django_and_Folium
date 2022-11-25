# django_and_folium


###  Project Goals

* Use the power of Folium to visualize data generated from Django Database on a Leaflet JS map.

* Use Django Admin Site to Import and Export data into and from the database.

* Visualize data using Folium's Simple Markers and Marker Cluster.


### Data Sources

The data used in this project is downloaded from the [Seattle City Open Data](https://data-seattlecitygis.opendata.arcgis.com/) website, The following Datasets are used:

* [Hospitals](https://data-seattlecitygis.opendata.arcgis.com/datasets/hospitals/explore)

* [Public Schools](https://data-seattlecitygis.opendata.arcgis.com/datasets/public-schools/explore)

* [Public Libraries](https://data-seattlecitygis.opendata.arcgis.com/datasets/seattle-public-libraries/explore)


### Project Preview

* [Youtube](https://www.youtube.com/watch?v=r08MujfgjoM)


### Libraries and Packages used

* [Django Web Framework](https://www.djangoproject.com/)

* [django-import-export](https://django-import-export.readthedocs.io/en/latest/) package

* [Folium](https://python-visualization.github.io/folium/)


### To get started with this project

* Clone the repository: git clone 'https://github.com/MoustafaShaaban/Django_and_Folium.git'

* Change directory to Version_1 ``` cd Version_1 ```

* Open the terminal or CMD to create a virtual environment like Python virtual environment (venv) or pipenv and activate it.

    * ``` python -m venv venv ```           *Create the venv*

    * ``` source venv/bin/activate ```      *On Linux*

    * ``` venv/Scripts/activate ```         *On Windows*

    * ``` sourcs venv/Scripts/activate ```  *Git Bash on Windows*

* Install requirements.txt: ``` python -m pip install -r requirements.txt ```

* Create the database and super user by running the following commands:
``` python manage.py migrate ```
``` python manage.py makemigrations seattle ```
``` python manage.py migrate seattle ```
``` python manage.py createsuperuser ```

* Create a superuser: ``` python manage.py createsuperuser ```

* Run the project: ``` python manage.py runserver ```