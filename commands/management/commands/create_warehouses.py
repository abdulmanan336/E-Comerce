from django.core.management.base import BaseCommand
from apps.services.retail.warehouses.models import Warehouse
import random

class Command(BaseCommand):
    help = 'Create 10 warehouse instances'

    def handle(self, *args, **kwargs):
        warehouse_names = [f'Warehouse {i}' for i in range(1, 11)]

        for name in warehouse_names:
            warehouse = Warehouse.objects.create(
                name=name,
                manager_name=f'Manager {name}',
                manager_email=f'{name.lower().replace(" ", "")}@example.com',
                phone_number=f'+1234567890{id}',
                insurance_information=f'Insurance info for {name}',
                warehouse_type=random.choice(['Type A', 'Type B', 'Type C']),
                total_products=random.randint(100, 1000),
                security_measures='Standard security measures',
                inventory_management_system='IMS v1.0',
                capacity=random.randint(500, 5000),
                available_space=random.randint(100, 1000),
                address_line1='123 Main St',
                address_line2='Suite 100',
                city='City Name',
                state='State Name',
                country='Country Name',
                postal_code='12345',
                location=f'{name} location',
                shipping_carrier_integration='Carrier Integration v1.0',
                safety_certifications='ISO 9001',
                barcode_integration=True,
                stock_alert_threshold=10,
                inventory_valuation_method='FIFO',
                warehouse_transfer_supported=True,
                reporting_and_analytics_supported=True,
                supplier_management_supported=True,
                quality_control_inspection_supported=True,
                returns_management_supported=True,
                warehouse_security_features='CCTV, Guards, Alarms',
                external_system_integration='ERP, CRM',
                active=True
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created {warehouse.name}'))
