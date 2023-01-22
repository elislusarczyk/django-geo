# L3Task

## References

* https://docs.djangoproject.com/en/4.1/ref/contrib/gis/tutorial/#introduction
* https://www.django-rest-framework.org/
* https://stackoverflow.com/questions/17408231/how-to-use-geodjango-with-haystack
* https://en.wikipedia.org/wiki/Spatial_reference_system
* https://epsg.org/crs_4326/WGS-84.html

## Usage

```
# Run postgres db
docker run -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -e PGDATA=/var/lib/postgresql/data/pgdata -v $(pwd)/data:/var/lib/postgresql/data -p 5432:5432 postgis/postgis
```

```
# Startup
python manage.py migrate
python manage.py runscript scripts.load_data
python manage.py runserver
http://localhost:8000/airports/?point=-4.123576,52.811744&radius=50000
```