import os
import sys
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, String, ForeignKey, Integer, Column, Text, DateTime, func
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(Text(250), nullable=False)
    suscription_date = Column(DateTime, server_default=func.now())
    favorite_relationship = relationship('Favorite', back_populates='user')

class People(Base):
    __tablename__='people'
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(250), nullable= False)
    eye_color = Column(String(250), nullable= False)
    films = Column(Integer, ForeignKey('films.id'), nullable= False)
    gender = Column(String(250), nullable= False)
    hair_color = Column(String(250), nullable= False)
    height = Column(Integer, nullable= False)
    homeworld = Column(Integer, ForeignKey('planets.id'), nullable= False)
    mass = Column(Integer, nullable= False)
    name = Column(String(250), nullable= False)
    skin_color = Column(String(250), nullable= False)
    created = Column(String(250), nullable= False)
    edited = Column(String(250), nullable= False)
    species = Column(Integer, ForeignKey('species.id'), nullable= False)
    sharships = Column(Integer, ForeignKey('starships.id'), nullable= False)
    url = Column(String(250), nullable= False)
    vehicles = Column(Integer, ForeignKey('vehicles.id'), nullable= False)
    planets_relation = relationship('Planets', back_populates='people')
    vehicles_relation = relationship('Vehicles', back_populates='people')
    starships_relation = relationship('Starships', back_populates='people')
    films_relationship = relationship('Films', back_populates='people')
    species_relationship = relationship('Species', back_populates='people')
    favorite_relationship = relationship('Favorite', back_populates='people')

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable= False)
    created = Column(String(250), nullable= False)
    diameter = Column(String(250), nullable= False)
    edited = Column(String(250), nullable= False)
    films = Column(Integer, ForeignKey('films.id'), nullable=False)
    gravity = Column(String(250), nullable= False)
    name = Column(String(250), nullable= False)
    orbital_period = Column(String(250), nullable= False)
    population = Column(String(250), nullable= False)
    residents = Column(Integer, ForeignKey('people.id'), nullable=False)
    rotation_period = Column(String(250), nullable= False)
    surface_water = Column(String(250), nullable= False)
    terrain = Column(String(250), nullable= False)
    url = Column(String(250), nullable= False)
    species_relationship = relationship('Species', back_populates='planets')
    films_relationship = relationship('Films', back_populates='planets')
    people_relationship = relationship('People', back_populates='planets')
    favorite_relationship = relationship('Favorite', back_populates='planets')

class Vehicles(Base):
    __tablename__='vehicles'
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer, nullable= False)
    consumables = Column(String(250), nullable= False)
    cost_in_credits = Column(Integer, nullable= False)
    created = Column(String(250), nullable= False)
    crew = Column(Integer, nullable= False)
    edited = Column(String(250), nullable= False)
    length = Column(String(250), nullable= False)
    manufacturer = Column(String(250), nullable= False)
    max_atmosphering_speed = Column(Integer, nullable= False)
    model = Column(String(250), nullable= False)
    name = Column(String(250), nullable= False)
    passengers = Column(Integer, nullable= False)
    pilots = Column(Integer, ForeignKey('people.id'), nullable=False)
    films = Column(Integer, ForeignKey('films.id'), nullable=False)
    url = Column(String(250), nullable= False)
    people_relationship = relationship('People', back_populates='vehicles')
    films_relationship = relationship('Films', back_populates='vehicles')
    favorite_relationship = relationship('Favorite', back_populates='vehicles')
    
class Films(Base):
    __tablename__='films'
    id = Column(Integer, primary_key=True)
    characters = Column(Integer, ForeignKey('people.id'), nullable=False)
    created = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String(250), nullable=False)
    planets = Column(Integer, ForeignKey('planets.id'), nullable=False)
    producer = Column(String(250), nullable=False)
    release_date = Column(String(250), nullable=False)
    species = Column(Integer, ForeignKey('species.id'), nullable=False)
    starships = Column(Integer, ForeignKey('starships.id'), nullable=False)
    title = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    vehicles = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    planets_relation = relationship('Planets', back_populates='films')
    vehicles_relation = relationship('Vehicles', back_populates='films')
    people_relation = relationship('People', back_populates='films')
    starships_relationship = relationship('Starships', back_populates='films')
    species_relationship = relationship('Species', back_populates='films')
    favorite_relationship = relationship('Favorite', back_populates='films')

class Starships(Base):
    __tablename__='sharships'
    id = Column(Integer, primary_key=True)
    MGLT = Column(String(250), nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    created = Column(String(250), nullable=False)
    crew = Column(Integer, nullable=False)
    edited = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    length = Column(Integer, nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)
    films = Column(Integer, ForeignKey('films.is'), nullable=False)
    pilots = Column(Integer, ForeignKey('people.id'), nullable=False)
    starship_class = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    people_relationship = relationship('People', back_populates='starships')
    films_relationship = relationship('Films', back_populates='starships')
    favorite_relationship = relationship('Favorite', back_populates='starships')

class Species(Base):
    __tablename__='species'
    id = Column(Integer, primary_key=True)
    average_height = Column(Integer, nullable=False)
    average_lifespan = Column(Integer, nullable=False)
    classification = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    eye_colors = Column(String(250), nullable=False)
    hair_colors = Column(String(250), nullable=False)
    homeworld = Column(Integer, ForeignKey('planets.id'), nullable=False)
    language = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    people = Column(Integer, ForeignKey('people.id'), nullable=False)
    films = Column(Integer, ForeignKey('films.id'), nullable=False)
    skin_colors = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    people_relationship = relationship('People', back_populates='species')
    films_relationship = relationship('Films', back_populates='species')
    favorite_relationship = relationship('Favorite', back_populates='species')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'), nullable=False)
    favorite_people = Column(Integer, ForeignKey('people.id'), nullable=False)
    favorite_planet = Column(Integer, ForeignKey('planets.id'), nullable=False)
    favorite_vehicle = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    favorite_film = Column(Integer, ForeignKey('films.id'), nullable=False)
    favorite_starship = Column(Integer, ForeignKey('starships.id'), nullable=False)
    favorite_specie = Column(Integer, ForeignKey('species.id'), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
