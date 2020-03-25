from django.db import models

class categorias(models.TextChoices):
    Montanhas = 'MO', 'Montanhas'
    Escaladas = 'ES', 'Escaladas'
    Expedições = 'EX', 'Expedições'
    Artigos = 'AR', 'Lyric Artigos'

class Work(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=categorias.choices,
        default=categorias.Montanhas,
    )
    imagem = models.ImageField(upload_to='work', null=True, blank=True)

class Frase(models.Model):
    description = models.TextField()
    text = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name