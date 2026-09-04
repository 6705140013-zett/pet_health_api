from datetime import date
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class VaccinationBase(BaseModel):
    vaccine_name: str
    administered_date: date
    next_due_date: date
    veterinarian: str


class VaccinationCreate(VaccinationBase):
    pass


class VaccinationResponse(VaccinationBase):
    id: int
    pet_id: int
    is_overdue: bool

    model_config = ConfigDict(from_attributes=True)


class PetBase(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    date_of_birth: date
    microchip_id: Optional[str] = None


class PetCreate(PetBase):
    pass


class PetResponse(PetBase):
    id: int
    vaccinations: List[VaccinationResponse] = []

    model_config = ConfigDict(from_attributes=True)