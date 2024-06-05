from fastapi import FastAPI, HTTPException
from database import init_db
from schemas import HomeCreate, TariffCreate
from crud import create_home, create_tariff, get_home_details, get_all_homes, calculate_rent, get_tariff
from utils import to_json

app = FastAPI()
init_db()

@app.post("/tariffs/")
async def add_tariff(tariff: TariffCreate):
    tariff_obj = create_tariff(tariff.name, tariff.price)
    return to_json(tariff_obj)

@app.get("/tariffs/{name}")
async def get_tariff_endpoint(name: str):
    tariff = get_tariff(name)
    if not tariff:
        raise HTTPException(status_code=404, detail="Tariff not found")
    return to_json(tariff)

@app.post("/homes/")
async def add_home(home: HomeCreate):
    home_data = home.dict()
    home_obj = create_home(home_data)
    return to_json(home_obj)

@app.get("/homes/{home_id}")
async def get_home(home_id: str):
    home = get_home_details(home_id)
    if not home:
        raise HTTPException(status_code=404, detail="Home not found")
    return to_json(home)

@app.get("/homes/")
async def list_homes():
    homes = get_all_homes()
    return [to_json(home) for home in homes]

@app.post("/homes/{home_id}/calculate_rent")
async def calculate_home_rent(home_id: str):
    try:
        home = calculate_rent(home_id)
        return to_json(home)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/homes/{home_id}/apartments/rent")
async def get_apartment_rents(home_id: str):
    home = get_home_details(home_id)
    if not home:
        raise HTTPException(status_code=404, detail="Home not found")
    return [to_json(apartment) for apartment in home.apartments]
