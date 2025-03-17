from abc import ABC, abstractmethod

# Vehicles Example
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car drives on the road."

class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedaled along the path."

class Boat(Vehicle):
    def move(self):
        return "The boat sails on the water."

# User Authentication Example
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass

class EmailAuth(UserAuthentication):
    def login(self):
        return "User authenticated using email and password."

class GoogleAuth(UserAuthentication):
    def login(self):
        return "User authenticated using Google OAuth."

class FingerprintAuth(UserAuthentication):
    def login(self):
        return "User authenticated using fingerprint scan."

# Testing polymorphism
vehicles = [Car(), Bicycle(), Boat()]
for v in vehicles:
    print(v.move())

auth_methods = [EmailAuth(), GoogleAuth(), FingerprintAuth()]
for auth in auth_methods:
    print(auth.login())
