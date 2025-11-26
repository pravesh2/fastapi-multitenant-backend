from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    users = relationship("User", back_populates="company")
    trips = relationship("Trip", back_populates="company")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="users")

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    start_location = Column(String)
    end_location = Column(String)

    company = relationship("Company", back_populates="trips")