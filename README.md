# Video2Cast
Indexing your youtube podcast videos in Google and Apple Podcasts
# Install
- docker-compose build (only init or when change Dockerfile)
- docker-compose run djangoapp index_podcast/manage.py migrate (every time when models is changed)
- docker-compose run djangoapp index_podcast/manage.py collectstatic (every time when static files is updated)
- docker-compose run djangoapp index_podcast/manage.py createsuperuser
- docker-compose up (startup application)
