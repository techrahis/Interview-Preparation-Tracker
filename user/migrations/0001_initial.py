# Generated by Django 4.0.3 on 2022-07-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Attempted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(max_length=64)),
                ('attempted_question_qIdentifier', models.CharField(max_length=64)),
            ],
        ),
    ]