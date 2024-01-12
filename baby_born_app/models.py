from django.db import models


class Smen(models.Model):
    time_part = models.CharField(max_length=50, verbose_name="Işleýän wagty")


    def __str__(self):
        return str(f'{self.time_part}')


class Gender(models.Model):
    gender_type = models.CharField(max_length=10, verbose_name="Jyns ady")


    def __str__(self):
        return str(f'{self.gender_type}')


class Carousel(models.Model):
    image = models.ImageField(upload_to="Carousel_images", verbose_name = "Karusel suraty")
    title = models.CharField(max_length=50, verbose_name="Karusel tema ady")
    about = models.CharField(max_length=100, verbose_name="Karusel beýany")


    def __str__(self):
        return str(f'{self.title}')


class Doctor(models.Model):
    fullname = models.CharField(max_length=50, verbose_name = "Ady we famaliýasy")
    avatar = models.ImageField(upload_to="doctors_images", verbose_name = "Lukmanyň şahsy suraty")
    work_time = models.ForeignKey(Smen, on_delete=models.CASCADE)
    about = models.TextField(max_length=500, verbose_name="Lukman barada")


    def __str__(self):
        return str(f'{self.fullname}')


    class Meta:
        verbose_name_plural = 'Lukmanlar'


class Baby(models.Model):
    surname = models.CharField(max_length=25, verbose_name="Maşgala familiýasy")
    avatar = models.ImageField(upload_to="babies_images", verbose_name="Suraty")
    born_time = models.DateTimeField(verbose_name="Dogulan wagty")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name="Jynsy")
    weight = models.FloatField(verbose_name="Agramy")
    babydoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Lukmany")
    is_alive = models.BooleanField(default=True, verbose_name="Ýaşaýşa dowam")


    def __str__(self):
        return str(f'{self.surname}')