#!/bin/bash

# remove files older than 5 days
find /backups/* -mtime +5 -exec rm {} \;
# run the backup
pg_dump -Fc -h localhost -U postgres -f /backups/geodjango-$(date +"%Y%m%d-%H%M").dump geodjango