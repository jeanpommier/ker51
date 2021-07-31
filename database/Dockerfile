FROM postgres:11

LABEL project="ker51"
LABEL org.opencontainers.image.authors="jeanpommier@pi-geosolutions.fr"

ENV DEBIAN_FRONTEND=noninteractive \
    POSTGRES_USER=postgres

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-11-postgis-3 \
        postgresql-11-postgis-3-scripts \
        postgresql-plpython-11 \
        python3-psycopg2 && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=postgres sql/[0-9][0-9]*  license.txt /docker-entrypoint-initdb.d/

HEALTHCHECK --interval=30s --timeout=30s \
  CMD pg_isready -U $POSTGRES_USER
