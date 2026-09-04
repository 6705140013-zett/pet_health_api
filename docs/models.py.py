from datetime import date
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=False)
    microchip_id = Column(String, nullable=True, unique=True)

    vaccinations = relationship(
        "Vaccination", back_populates="pet", cascade="all, delete-orphan"
    )


class Vaccination(Base):
    __tablename__ = "vaccinations"

    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    vaccine_name = Column(String, nullable=False)
    administered_date = Column(Date, nullable=False)
    next_due_date = Column(Date, nullable=False)
    veterinarian = Column(String, nullable=False)

    pet = relationship("Pet", back_populates="vaccinations")