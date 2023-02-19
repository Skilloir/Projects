import random
import requests

list_input = input("What would you like to make a full list of? \n")
url = 'https://bin.bloom.host/'
list = []

azLowerCase = "abcdefghijklmnopqrstuvwxyz"
azUpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


if list_input == "alphabet":
   LowerUpper_input = input("What would you like to lower or upper? \n")
   if LowerUpper_input == "lower":
      for i in azLowerCase:
         list.append(i) 
   elif LowerUpper_input == "upper":
      for i in azLowerCase:
         list.append(i.upper()) 
print(list)   