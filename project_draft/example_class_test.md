```.py

#class_test.py
from datetime import datetime
from typing import List

class test:
    def __init__(self, name: str, id: int, super_id: float, email: str, birthyear: int):
        self.name = name
        self.id = id
        self.super_id = super_id
        self.email = email
        self.year = birthyear

    def get_name(self) -> str:
        return(self.name)
    
    def get_id(self) -> int:
        return(self.id)
    
    def get_super_id(self) -> float:
         return(self.super_id)
    
    def create_email(self) -> str:
        name = self.name.replace(' ', '.').lower()
        return f"{self.year}.{name}@gmail.com"
    
    def get_email(self) -> str:
        return(self.email)
    
    def get_birthyear(self) -> int:
        return(self.year)
    
    def get_age(self) -> int:
        return datetime.now().year - self.year
    
    def __repr__(self) -> str:
        return f"<{self.name} {self.id} {self.super_id} {self.email} {self.year}>"
    
    def __str__(self) -> str:
        return f"{self.name} {self.id} {self.super_id} {self.email} {self.year}"
    
#    def __eq__(self, other) -> bool:
#       return self.id == other.id

```
