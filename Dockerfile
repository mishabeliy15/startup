# start from an official image
FROM python:3.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV DJANGO_SETTINGS_MODULE "index_podcast/index_podcast.settings" #For development
# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
COPY requirements.txt /opt/services/djangoapp/src/
WORKDIR /opt/services/djangoapp/src
# install our two dependencies
RUN pip install -r requirements.txt
RUN pip install --upgrade youtube-dl
# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 80
EXPOSE 443

# define the default command to run when starting the container
#CMD ["gunicorn", "--chdir", "index_podcast", "--bind", ":8000", "index_podcast.wsgi:application"]