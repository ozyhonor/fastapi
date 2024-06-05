from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import StringField, FloatField, ListField, EmbeddedDocumentField, IntField, ReferenceField

class Tariff(Document):
    name = StringField(required=True)
    price = FloatField(required=True)

class WaterMeterReading(EmbeddedDocument):
    previous_reading = FloatField(required=True)
    current_reading = FloatField(required=True)

class WaterMeter(EmbeddedDocument):
    meter_id = IntField(required=True)
    tariff_name = StringField(required=True)
    tariff_price = FloatField(required=True)
    readings = EmbeddedDocumentField(WaterMeterReading)

class Apartment(EmbeddedDocument):
    apartment_number = IntField(required=True)
    area = IntField(required=True)
    water_meters = ListField(EmbeddedDocumentField(WaterMeter))
    total_rent = FloatField(default=0)

class Home(Document):
    address = StringField(required=True)
    apartments = ListField(EmbeddedDocumentField(Apartment))
