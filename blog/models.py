from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
#este ultimo es para poder trabajar con el modelo de usuarios que trae el panel admin de django


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    #Para cuando se imprima un objeto, salga como string
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    subtitle = models.CharField(max_length=150, verbose_name="Subtitle")
    content = RichTextField(max_length=1000, verbose_name="Content")
    image = models.ImageField(default = "null", verbose_name="Image", upload_to="movies")
    public = models.BooleanField(verbose_name="Public?")
    user = models.ForeignKey(User, editable=False, verbose_name="User", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Edited at")

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title


class TvShow(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    subtitle = models.CharField(max_length=150, verbose_name="Subtitle")
    content = RichTextField(max_length=1000, verbose_name="Content")
    image = models.ImageField(default = "null", verbose_name="Image", upload_to="tvshows")
    public = models.BooleanField(verbose_name="Public?")
    user = models.ForeignKey(User, editable=False, verbose_name="User", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Edited at")

    class Meta:
        verbose_name = "Tv Show"
        verbose_name_plural = "Tv Shows"

    def __str__(self):
        return self.title
