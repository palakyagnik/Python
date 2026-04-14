# Create a Temperature class, Create 2 methods named convertFarenheit() and convertCelsius().

class Temperature:

    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius


t1 = Temperature()

print("Fahrenheit:", t1.convertFahrenheit(25))
print("Celsius:", t1.convertCelsius(77))
