FROM postgres:10

LABEL project="ker51"
LABEL org.opencontainers.image.authors="jeanpommier@pi-geosolutions.fr"

ENV DEBIAN_FRONTEND=noninteractive \
    POSTGRES_USER=postgres

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-10-postgis-3 \
        postgresql-10-postgis-3-scripts \
        postgresql-plpython-10 \
        python3-psycopg2 && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=postgres sql/[0-9][0-9]*  /docker-entrypoint-initdb.d/
COPY backupPGSQL.sh  /root/backupPGSQL.sh
RUN chmod +x /root/backupPGSQL.sh

HEALTHCHECK --interval=30s --timeout=30s \
  CMD pg_isready -U $POSTGRES_USER
