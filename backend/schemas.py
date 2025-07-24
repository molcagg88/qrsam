from pydantic import BaseModel
from typing import Dict, List, Optional


class MenuItemBase(BaseModel):
    price: float
    image: Optional[str]
    category: str
    prep_time: Optional[str]
    available: Optional[bool] = True

    name_translations: Dict[str, str]
    description_translations: Optional[Dict[str, str]] = None
    ingredients_translations: Optional[Dict[str, str]] = None
    tags: Optional[List[str]] = None


class MenuItemCreate(MenuItemBase):
    restaurant_id: int


class MenuItem(MenuItemBase):
    id: int
    restaurant_id: int

    class Config:
        orm_mode = True


class RestaurantBase(BaseModel):
    name: str
    location: Optional[str]


class RestaurantCreate(RestaurantBase):
    pass


class Restaurant(RestaurantBase):
    id: int
    menu_items: List[MenuItem] = []

    class Config:
        orm_mode = True
