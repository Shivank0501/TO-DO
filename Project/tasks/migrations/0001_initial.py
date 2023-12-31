# Generated by Django 4.2.3 on 2023-07-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('todo', 'Open'), ('in_progress', 'Working'), ('completed', 'Done'), ('overdue', 'Overdue')], default='todo', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
