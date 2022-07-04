# Generated by Django 4.0.5 on 2022-07-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_author_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='grade',
        ),
        migrations.AddField(
            model_name='book',
            name='grade',
            field=models.CharField(blank=True, choices=[('1', 'Grade 1'), ('2', 'Grade 2'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('5', 'Grade 5'), ('6', 'Grade 6')], default='2', help_text='Grade Level', max_length=1),
        ),
    ]
