from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    local_evento = models.CharField(max_length=150, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_criacao(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False

    def get_data_compare(self):
        return self.data_evento.strftime('%Y-%m-%d')

    def get_evento_dia(self):
        today = date.today().strftime('%Y-%m-%d')
        data = self.get_data_compare()
        if data == today:
            return True
        else:
            return False
