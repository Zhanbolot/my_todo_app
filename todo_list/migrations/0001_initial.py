# Generated by Django 2.2 on 2019-05-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('Status', models.CharField(choices=[('необходимо выполнить', 'необходимо выполнить'), ('сделано', 'сделано'), ('отменено', 'отменено')], default='необходимо выполнить', max_length=20)),
            ],
        ),
    ]