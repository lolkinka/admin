# Generated by Django 4.0.5 on 2022-07-30 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тематика')),
            ],
            options={
                'verbose_name': 'РАЗДЕЛЫ',
                'verbose_name_plural': 'РАЗДЕЛЫ',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=True, verbose_name='ОСНОВНОЙ')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='articles.article')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='articles.scope', verbose_name='РАЗДЕЛ')),
            ],
            options={
                'verbose_name': 'ТЕМАТИКА',
                'verbose_name_plural': 'ТЕМАТИКИ СТАТЬИ',
            },
        ),
        migrations.AddField(
            model_name='scope',
            name='article',
            field=models.ManyToManyField(related_name='scopes', through='articles.Tag', to='articles.article'),
        ),
    ]