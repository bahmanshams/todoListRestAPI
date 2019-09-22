# Generated by Django 2.2.5 on 2019-09-22 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subset',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todo.Todo')),
                ('todo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='todo.Todo')),
            ],
            bases=('todo.todo',),
        ),
    ]
