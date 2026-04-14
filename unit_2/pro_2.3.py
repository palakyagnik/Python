#Write a program to generate arithmetic exception and log the exception in system.

import logging

logging.basicConfig(
    filename="system.log",       
    level=logging.ERROR,        
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError as e:
        print("Error: Division by zero!")
        logging.error("Arithmetic Exception occurred: %s", e)


divide_numbers(10, 2)   
divide_numbers(10, 0)
