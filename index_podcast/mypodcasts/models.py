from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/podcast_{1}/img/{2}'.format(instance.owner.id, instance.id, filename)


class Podcast(models.Model):
    owner = models.ForeignKey('myauth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title