from pydantic import BaseModel


class QuintoAndarSchema(BaseModel):
    """Schema of homepage block of characters of some building."""

    street_name: str = ""
    state_name: str = ""
    district_name: str = ""
    type_building: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    number_parking_space: int = 0
    size_residence: int = 0
    rent_price_without_tax: int = 0
    total_rent_price: int = 0
    condominium_tax: int = 0
    house_tax: int = 0
    fire_insurance: int = 0
    service_tax: int = 0
    link_apartment: str = ""
    pet_flag: bool = False
    metro_flag: bool = False
    furniture_flag: bool = False
    residence_id: int = 0
