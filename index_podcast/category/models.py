from django.db import models


class Category(models.Model):
    display = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.display


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    display = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.display

    class Meta:
        unique_together = ('category', 'name')
