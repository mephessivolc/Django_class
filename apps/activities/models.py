from typing import Iterable, Optional
from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.utils import timezone

from apps.team.models import Team
from apps.students.models import Students

class Activities(models.Model):

    name = models.CharField("Identificação", max_length=100)
    slug = models.SlugField("Identificador", max_length=100, editable=False)
    team = models.ManyToManyField(Team, verbose_name="Turma")
    max_score = models.DecimalField("Pontuação Máxima", max_digits=5, decimal_places=2, default=0)

    created = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        ordering = ["created", 'slug']

    def __str__(self) -> str:
        return f"{self.name}"
    
    def save(self, *args, **kwargs) -> None:
        slug = slugify(f"{timezone.now().year} {self.name}")
        if not self.slug or not slug == self.slug:
            self.slug = slug 

        return super(Activities, self).save(*args, **kwargs)

class Score(models.Model):
    score = models.DecimalField(max_digits=5, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='scores')
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE, related_name='scores')
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='scores')
