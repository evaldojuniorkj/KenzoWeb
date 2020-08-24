from django.db import models
from datetime import datetime

# Create your models here.
class Pessoa(models.Model):
    UF_CHOICES = (
        ('AC', 'Acre'), 
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )
    TIPO_CHOICES = (
        ('FISICA', 'Física'),
        ('JURIDICA', 'Jurídica')
    )

    nome = models.CharField(max_length=200)
    celular = models.CharField(max_length=30, null= True)
    nome_fantasia = models.CharField(max_length=200, null=True)
    cpf_cnpj = models.CharField(max_length=30, null=True)
    rg_ie = models.CharField(max_length=30, null=True)
    whatsApp = models.CharField(max_length=30, null= True)
    email = models.EmailField(max_length=200, null=True)
    tipo_cliente = models.CharField(choices=TIPO_CHOICES, max_length=10, default=TIPO_CHOICES[0])
    
    cep = models.CharField(max_length=15, null=True)
    uf = models.CharField(max_length=2, choices=UF_CHOICES, default='RR')
    codigo_ibge = models.IntegerField(null=True)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    bairro = models.CharField(max_length=60)
    referencia = models.TextField(null=True)
    release_date = models.DateTimeField('Data de Cadastro', auto_now=True)
    
    def __str__(self):
        return self.nome