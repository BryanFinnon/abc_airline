# Generated by Django 5.2 on 2025-05-07 21:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('passport_number', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TravelClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled'), ('AMENDED', 'Amended')], default='CONFIRMED', max_length=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='flights.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='flights.passenger')),
                ('travel_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.travelclass')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('action_type', models.CharField(choices=[('MODIFY', 'Modify'), ('CANCEL', 'Cancel')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_actions', to='flights.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Luggage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luggage_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bag_count', models.PositiveIntegerField(default=1)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='luggages', to='flights.booking')),
            ],
        ),
        migrations.CreateModel(
            name='MealSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_selections', to='flights.booking')),
                ('meal_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.mealoption')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('card_number', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='flights.booking')),
            ],
        ),
        migrations.CreateModel(
            name='PickupDropService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('PICKUP', 'Pickup'), ('DROPOFF', 'Dropoff')], max_length=8)),
                ('address', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_services', to='flights.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='flights.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='flights.flight')),
                ('travel_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='flights.travelclass')),
            ],
            options={
                'unique_together': {('flight', 'travel_class')},
            },
        ),
    ]
