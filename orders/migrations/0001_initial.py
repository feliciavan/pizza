# Generated by Django 2.0.3 on 2019-04-07 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=64)),
                ('kind', models.CharField(max_length=64)),
                ('num_toppings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kind_price', to='orders.Pizza')),
                ('num_toppings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='num_toppings_price', to='orders.Pizza')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size_price', to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_topping', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]
