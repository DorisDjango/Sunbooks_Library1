# Generated by Django 4.0.5 on 2022-06-18 04:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='imprint',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='grade',
            field=models.CharField(blank=True, choices=[('1', 'Grade 1'), ('2', 'Grade 2'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('5', 'Grade 5'), ('6', 'Grade 6')], default='2', help_text='Grade Level', max_length=1),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for book across the library', primary_key=True, serialize=False),
        ),
    ]