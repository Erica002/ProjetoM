from django.contrib import admin
from main.models import Aluno, Disciplina, Aluno_Disciplina
# Register your models here.

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Aluno_Disciplina)

