# Annuaire & carte Ker51

Ce projet vise à fournir une appli web pour constituer une carte des hivernants Ker51 et assimilés (conjoints, 
sympathisants etc).

Un formulaire permet de déclarer un nouvel "hivernant" (un foyer, en fait), avec coordonnées, et localisation 
géographique.
Ce formulaire est à accès restreint, il faut un identifiant & mot de passe.

Les infos sont stockées en base de données, et servent de base à 
* un annuaire (/hivernants/list),
* une carte (/hivernants/map).

L'ensemble est à accès restreint, pour protéger les infos personnelles.

## Structure du repo
* database: config docker pour la BD postgis utilisée par le projet.On compile l'image via docker-compose
* django: la config pour le code django
  * app: l'appli django proprement dite
  * docker: fichiers utilisés pour l'image docker, définie dans Dockerfile \
On compile l'image via docker-compose 
* secrets: les secrets docker utilisés pour la version de test/dev. En prod, il est attendu que vous changiez les 
valeurs pour les rendre secure

## Compiler les images docker
`docker-compose build`

## Config de dev
* Démarrer la base de données (`docker-compose -f docker-compose-dev.yml up`)
* Créer un environnement virtuel python (`python3 -m venv .venv`), l'activer (`source .venv/bin/activate`) et installer 
les dépendances (`pip install -r requiremetns.txt`)
* Lancer le serveur de dev (`python manage.py runserver`)
* Travaillez sur le code

## Config de production
* Configurer les secrets (ne pas utiliser ceux fournis dans le code, les valeurs sont versionnées, ce n'est absolument 
pas secure. Elles sont fournies à titre d'exemple)
* lancer la compo (`docker-compose up`)

Idéalement, le site ne devrait pas être directement accessible via nginx en port 80, il vaudrait mieux placer le tout 
derrière un point d'accès SSL avec SSL termination

Si vous fournissez `DJANGO_SUPERUSER_PASSWORD` (ou `DJANGO_SUPERUSER_PASSWORD_FILE` avec un secret), un superutilisateur 
django sera créé au démarrage (cf `django/docker/docker-entrypoint.d/050-create-superuser`).
Vous pouvez configurer le nom et le mail du superutilisateur ainsi créé via les variables d'environnement 
`DJANGO_SUPERUSER_NAME` et `DJANGO_SUPERUSER_EMAIL`