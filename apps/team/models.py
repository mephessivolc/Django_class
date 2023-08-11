from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.utils import timezone

class Team(models.Model):
    
    name = models.CharField("Identificação", max_length=200)
    slug = models.SlugField("identificador", max_length=200, editable=False)

    created = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self) -> str:
        return f"{self.name}"
    
    def save(self, *args, **kwargs) -> None:
        slug = slugify(f"{timezone.now().year} {self.name}")
        if not self.slug or not slug == self.slug:
            self.slug = slug 

        return super(Team, self).save(*args, **kwargs)