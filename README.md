# django_and_folium


###  Project Goals

* Use Django admin site to import data from different sources (CSV, JSON, ...) into the database.

* Use the power of Folium to visualize data generated from Django Database on a Leaflet JS map.

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

* [django-import-export](https://django-import-export.readthedocs.io/en/latest/)

* [Folium](https://python-visualization.github.io/folium/)


### To get started with this project

* Clone the repository: git clone https://github.com/MoustafaShaaban/Django_and_Folium.git

* Change directory to Version_1 ``` cd Version_1 ```

* Open the terminal or CMD to create a virtual environment like Python virtual environment (venv) or pipenv and activate it.

    * ``` python -m venv venv ```           *Create the venv*

    * ``` source venv/bin/activate ```      *On Linux*

    * ``` venv/Scripts/activate ```         *On Windows*

    * ``` source venv/Scripts/activate ```  *Git Bash on Windows*

* Install requirements.txt: ``` python -m pip install -r requirements.txt ```

* Create the database by running the following commands:
``` python manage.py makemigrations seattle ```
``` python manage.py migrate ```

* Create a super user: ``` python manage.py createsuperuser ```

* Login to the admin site with your super user and add the data in 'seattle/data' folder using the import functionality in each model.

* Run the project: ``` python manage.py runserver ```

------------------------------------------------------------------------------------------------------------

# Version 2:

In this version I improved the code by combining all the data in one Django Function View to show it in one map.

Added Layer Control functionality to switch between different layers.

Changed the default style of the Markers and used font awesome icons:

    * ` h-square ` Icon for Hospitals Layer.
    * ` graduation-cap ` Icon for Public Schools Layer.
    * ` book ` Icon for Public Libraries Layer.


### Version 2 Preview

* [Youtube](https://www.youtube.com/watch?v=eU8r5l9-6JE)

------------------------------------------------------------------------------------------------------------

# Version 3:

In this version I added the support of Importing and Exporting the data from the website directly (without using the Django Admin Site).



### Version 3 Preview

* [Youtube](https://www.youtube.com/watch?v=ZdYvfzODhZg)

* [GIF](./Version_3/Version_3.gif)



## References:

* [django-import-export](https://django-import-export.readthedocs.io/en/latest/)

* [django.how](https://django.how/admin/django-export-import-data/)

*[django-bootstrap-messages](https://ordinarycoders.com/blog/article/django-messages-framework)