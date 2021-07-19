from pydantic import BaseModel


class QuintoAndarSchema(BaseModel):
    """Schema of homepage block of characters of some building.
    """
    street_name: str = ""
    state_name: str = ""
    district_name: str = ""
    type_building: str = ""
    number_rooms: int = 0
    size_building: int = 0
    rent_price: float = 0
    total_rent_price: float = 0
    link_apartment: str = ""
