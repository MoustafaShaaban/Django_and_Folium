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

* Create a super user: ``` python manage.py createsuperuser ```

* Login to the admin site with your super user and add the data in 'seattle/data' folder using the import functionality in each model.

* Run the project: ``` python manage.py runserver ```

------------------------------------------------------------------------------------------------------------

# Version 2:

In this version I improved the code by combining all the data in one Django Function View to show it in one map.

Added Layer Control functionality to switch between different data layers.

Changed the default style of the Markers and used font awesome icons:

    * ` h-square ` icon for Hospitals Layer.
    * ` graduation-cap ` icon for Public Schools Layer.
    * ` book ` icon for Public Libraries Layer.


### Version 2 Preview

* [Youtube](https://www.youtube.com/watch?v=eU8r5l9-6JE)