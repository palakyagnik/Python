# Write a program to create interface and utilize the same in other class.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with a self button")


c = Car()
b = Bike()

c.start()
b.start()
