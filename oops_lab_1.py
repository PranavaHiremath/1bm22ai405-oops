# -*- coding: utf-8 -*-
"""oops_lab_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jMcXXmx3X__6tp4ejJXGp-xSvkiYpzor
"""

def max(list1):
  max = list1[0]

  for x in list1:
    if x > max:
      max = x

  return max


list1 = [10, 30, 40, 56, 13]
print("largest element in the list is :", max(list1))

import math

def hexagon_area(length):
  area = (3* math.sqrt(3)* (length** 2)) /2
  return area

side = 5
result = hexagon_area(side)
print(f'the area of the regular hexagon with side length {side } is {result}')

import re

def is_valid_email(email):
  pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

  if re.match(pattern, email):
        return True
  else:
        return False

email_address = "email@email.com"
result = is_valid_email(email_address)

if result:
    print(f"The email '{email_address}' is valid.")
else:
    print(f"The email '{email_address}' is not valid.")