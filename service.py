import requests
from pydantic import BaseModel


class GeoLocation(BaseModel):
    lat: str
    lng: str
    
class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str
    
    
class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoLocation

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: str
    address: Address
    website: str
    company: Company


database: dict[int, str] = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}


def get_user_from_db(user_id: int) -> str:
    return database.get(user_id, "No user found")


def get_users() -> list[User]:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    if response.status_code == 200:
        data = response.json()
        
        users = [User(**user) for user in data]
        
        return users
    
    raise requests.HTTPError
      