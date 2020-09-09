# Generated by Django 3.1.1 on 2020-09-09 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200, verbose_name='Course Title')),
                ('course_slug', models.SlugField(verbose_name='Course Slug')),
                ('course_description', models.TextField(blank=True, null=True, verbose_name='Course Description')),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='courses/')),
                ('course_is_active', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=50, verbose_name='Is Active?')),
                ('course_is_featured', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=50, verbose_name='Is Featured?')),
                ('course_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('course_updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('seo_course_title', models.CharField(blank=True, max_length=60, null=True, verbose_name='SEO Course Title (60 Characters Long)')),
                ('seo_course_keywords', models.TextField(blank=True, null=True, verbose_name='SEO for Course Keywords, Separated by Commas')),
                ('seo_course_description', models.TextField(blank=True, null=True, verbose_name='SEO Course Description (160 Characters Long)')),
                ('course_topic', models.ManyToManyField(to='courses.Topic', verbose_name='Course Topic')),
            ],
        ),
    ]
