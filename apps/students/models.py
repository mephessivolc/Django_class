from django.db import models

from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
from apps.team.models import Team

class Students(models.Model):

    name = models.CharField("Nome", max_length=200)
    slug = models.SlugField("Identificador", max_length=200, editable=False)

    created = models.DateTimeField("Criado em", auto_now_add=True)

    team = models.ManyToManyField(Team, verbose_name='Turma')

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural  = "Alunos"

    def __str__(self) -> str:
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        slug = f"{self.name}"

        if not self.slug or not slug == self.slug:
            self.slug = slug 

        return super(Students, self).save(*args, **kwargs)