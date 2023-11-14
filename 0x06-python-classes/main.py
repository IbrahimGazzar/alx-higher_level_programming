#!/usr/bin/python3
Square = __import__('6-square').Square
square = Square(size=5, position=(2, -2))

# Test the size setter
try:
    square.size = "not_an_integer"
except TypeError as e:
    print(f"TypeError: {e}")  # This should raise a TypeError

try:
    square.size = -1
except ValueError as e:
    print(f"ValueError: {e}")  # This should raise a ValueError

# Test the position setter
try:
    square.position = "not_a_tuple"
except TypeError as e:
    print(f"TypeError: {e}")  # This should raise a TypeError

try:
    square.position = (1, 2.5)
except TypeError as e:
    print(f"TypeError: {e}")  # This should raise a TypeError

try:
    square.position = (-1, 2)
except TypeError as e:
    print(f"TypeError: {e}") 
