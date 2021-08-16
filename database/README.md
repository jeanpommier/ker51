PostGIS config for the ker51 django project

Environment variables:
- this image is derived from postgres official image, so you can use all customizations from postgres
- additionally, you are expected to provide the password for the `django` user, using the `DJANGO_PASSWORD` environment 
variable, or better, use secrets with `DJANGO_PASSWORD_FILE` variable

## Perform a backup
You can run the script /root/backupPGSQL.sh
It outputs the backups in /backups/ folder. You are expected to make it a volume and mount it in your container.