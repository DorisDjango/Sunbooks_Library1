# Generated by Django 4.0.5 on 2022-07-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_remove_bookinstance_grade_book_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]