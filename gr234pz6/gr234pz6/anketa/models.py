from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professions(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Professions._meta.fields]

class Skills(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Skills._meta.fields]

class Questions(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    Score = models.PositiveIntegerField()
    Skills = models.ForeignKey(Skills, on_delete=models.PROTECT, verbose_name="Навык")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Questions._meta.fields]


class Model_prof(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    Professions = models.ForeignKey(Professions, on_delete=models.PROTECT, verbose_name="Профессия")
    Skills = models.ForeignKey(Skills, on_delete=models.PROTECT, verbose_name="Навык")
    Score = models.PositiveIntegerField()

    class Meta:
        ordering = ["-title"]
        verbose_name = "Модельная профессия"
        verbose_name_plural = "Модельные профессии"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Model_prof._meta.fields]
    
class Blank(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    image_full = models.ImageField(upload_to='blank/%Y/%m/%d', blank=True)
    image_one= models.ImageField(upload_to='blank/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ["-title"]
        verbose_name = "Бланк"
        verbose_name_plural = "Бланки"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Blank._meta.fields]
    
class Human(User):
    title = models.TextField(max_length=50, verbose_name="Название")
    avatar = models.ImageField(upload_to='human/%Y/%m/%d', blank=True)
    phone = models.CharField(max_length=15)

    class Meta:
        ordering = ["-title"]
        verbose_name = "Человек"
        verbose_name_plural = "Человечки"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Blank._meta.fields]
       
