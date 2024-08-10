from django.db import models
from django.urls import reverse
from django.utils import timezone
from slugify import slugify as py_slugify


class InExCludeModel(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название тура')
    slug = models.SlugField(max_length=250, verbose_name='Slug "автозаволнение"', unique=True)
    about = models.TextField(verbose_name='Информация про тура')
    prise = models.IntegerField(verbose_name='Цена тура')
    days = models.IntegerField(verbose_name='Продолжительность тура')
    addres = models.CharField(max_length=150, verbose_name='Адрес гостиницы')
    image = models.ImageField(verbose_name='Фото для тура')
    exclude = models.ManyToManyField("InExCludeModel", related_name='exclude')
    include = models.ManyToManyField("InExCludeModel", related_name='include')
    publish_time = models.DateField(default=timezone.now, verbose_name='Это поля автоматическая не трогать')
    start_date = models.DateField(default=timezone.now, verbose_name='Дата старта тура')
    end_date = models.DateField(default=timezone.now, verbose_name='Дата конца тура')
    country = models.CharField(max_length=150, verbose_name='Государство где тур будет проходить')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tour_detail_page", args=[self.slug])

    def generate_slug(self):
        return py_slugify(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)



class BuyModel(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    tour = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} - {self.tour}"



class ContactModel(models.Model):

    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    subject = models.CharField(max_length=50)
    your_comment = models.TextField()

    def __str__(self):
        return self.full_name
    
    