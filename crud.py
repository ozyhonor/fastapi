from models import Home, Tariff
from bson import ObjectId

def create_tariff(name: str, price: float) -> Tariff:
    tariff = Tariff(name=name, price=price)
    tariff.save()
    return tariff

def get_tariff(name: str) -> Tariff:
    return Tariff.objects(name=name).first()

def create_home(home_data: dict) -> Home:
    home = Home(**home_data)
    home.save()
    return home

def get_home_details(home_id: str):
    return Home.objects(id=ObjectId(home_id)).first()

def get_all_homes():
    return Home.objects().all()

def calculate_rent(home_id: str):
    home = Home.objects(id=ObjectId(home_id)).first()
    if not home:
        raise ValueError("Home not found")
    
    for apartment in home.apartments:
        water_cost = 0
        area_cost = 0
        for meter in apartment.water_meters:
            consumption = meter.readings.current_reading - meter.readings.previous_reading
            water_cost += consumption * meter.tariff_price
        area_cost = apartment.area * meter.tariff_price
        apartment.total_rent = water_cost + area_cost
    
    home.save()
    return home
