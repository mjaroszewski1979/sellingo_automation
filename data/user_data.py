from dataclasses import dataclass
from faker import Faker
import random
import string

# Inicjalizacja generatora danych testowych w języku polskim
fake = Faker("pl_PL")

def generate_password(length=10):
    """
    Generuje losowe hasło o podanej długości.
    Składa się z liter (małych i wielkich) oraz cyfr.
    Domyślna długość hasła to 10 znaków.
    """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))  

@dataclass
class UserData:
    """
    Model danych użytkownika testowego.
    Zawiera adres e-mail i hasło, które mogą być użyte
    np. do wypełnienia formularza rejestracyjnego.
    """
    email: str
    password: str

def get_test_user() -> UserData:
    """
    Tworzy i zwraca obiekt `UserData` z losowym adresem e-mail
    (generowanym przez bibliotekę Faker) oraz losowym hasłem.
    """
    return UserData(email=fake.unique.email(), password=generate_password())
