# Generated by Django 2.0.4 on 2018-04-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoDjango', '0007_auto_20180412_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModalidadeTransporte',
            fields=[
                ('id', models.IntegerField(auto_created=True, help_text='Deixe em branco', primary_key=True, serialize=False, verbose_name='Código')),
                ('descricao', models.CharField(max_length=100, verbose_name='Modalidade Transporte')),
            ],
        ),
    ]
