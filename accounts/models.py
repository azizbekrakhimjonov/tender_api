from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Profil(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)




class FreightOrder(models.Model):
    cargo_description = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)

    weight_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    volume_m3 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    # Dates
    pickup_date = models.DateField()
    delivery_date = models.DateField()

    VEHICLE_TYPES = [
        ('standard', 'Standard Truck'),
        ('refrigerated', 'Refrigerated Truck'),
        ('flatbed', 'Flatbed Truck'),
        ('tanker', 'Tanker Truck'),
        ('container', 'Container Carrier'),
    ]
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)

    special_requirements = models.TextField(blank=True)

    INCOTERMS_CHOICES = [
        ('EXW', 'EXW (Ex Works)'),
        ('FCA', 'FCA (Free Carrier)'),
        ('FOB', 'FOB (Free On Board)'),
        ('CIF', 'CIF (Cost, Insurance and Freight)'),
        ('CFR', 'CFR (Cost and Freight)'),
        ('DAP', 'DAP (Delivered At Place)'),
        ('DPU', 'DPU (Delivered at Place Unloaded)'),
        ('DDP', 'DDP (Delivered Duty Paid)'),
    ]
    incoterms = models.CharField(max_length=3, choices=INCOTERMS_CHOICES)
    additional_notes = models.TextField(blank=True)

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('tendering', 'Tendering'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Freight Order #{self.id}: {self.origin} to {self.destination}"

    class Meta:
        ordering = ['-created_at']