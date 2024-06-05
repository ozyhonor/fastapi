from pydantic import BaseModel, Field
from typing import List

class WaterMeterReadingCreate(BaseModel):
    previous_reading: float = Field(..., description="Показание счетчика за предыдущий месяц")
    current_reading: float = Field(..., description="Показание счетчика за текущий месяц")

class WaterMeterCreate(BaseModel):
    meter_id: int = Field(..., description="ID счетчика")
    tariff_name: str = Field(..., description="Название тарифа")
    tariff_price: float = Field(..., description="Цена тарифа")
    readings: WaterMeterReadingCreate = Field(..., description="Показания счетчика")

class ApartmentCreate(BaseModel):
    apartment_number: int = Field(..., description="Номер квартиры")
    area: int = Field(..., description="Площадь квартиры")
    water_meters: List[WaterMeterCreate] = Field(..., description="Список счетчиков воды в квартире")

class HomeCreate(BaseModel):
    address: str = Field(..., description="Адрес дома")
    apartments: List[ApartmentCreate] = Field(..., description="Список квартир в доме")

class TariffCreate(BaseModel):
    name: str = Field(..., description="Название тарифа")
    price: float = Field(..., description="Цена тарифа")
