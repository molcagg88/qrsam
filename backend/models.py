from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)

    menu_items = relationship("MenuItem", back_populates="restaurant")


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)

    price = Column(Float, nullable=False)
    image = Column(String)
    category = Column(String)
    prep_time = Column(String)
    available = Column(Boolean, default=True)

    name_translations = Column(JSONB, nullable=False)           # {"en": "...", "am": "..."}
    description_translations = Column(JSONB, nullable=True)
    ingredients_translations = Column(JSONB, nullable=True)
    tags = Column(JSONB, nullable=True)                         # ["spicy", "halal"]

    restaurant = relationship("Restaurant", back_populates="menu_items")
