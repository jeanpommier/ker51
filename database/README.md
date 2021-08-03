PostGIS config for the ker51 django project

Environment variables:
- this image is derived from postgres official image, so you can use all customizations from postres
- additionnally, you are expected to provide the password for the `django` user, using the `DJANGO_PASSWORD` environment 
variable, or better, use secrets with `DJANGO_PASSWORD_FILE` variable