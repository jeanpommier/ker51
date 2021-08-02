CREATE USER django PASSWORD 'dj_passwd';
CREATE DATABASE geodjango OWNER django;
\connect geodjango
CREATE EXTENSION postgis;