# Generated by Django 3.2.4 on 2021-06-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_rentbookk_rentbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCatelogy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='rentbook',
            name='rentDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rentbook',
            name='reterneddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
