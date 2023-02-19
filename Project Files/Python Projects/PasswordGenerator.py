import random


generatedPassword_List = []
othersymbols = "!#$%^&*()_+"
azLowerCase = "abcdefghijklmnopqrstuvwxyz"
azUpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(50):
   randomAZ_upper = random.sample(azUpperCase, 3)

for i in range(50):
   randomAZ_symbols = random.sample(azUpperCase, 3)

for i in range(50):
   randomAZ_lower = random.sample(azUpperCase, 3)

generatedPassword_List.append(randomAZ_upper + randomAZ_symbols + randomAZ_lower)
generatedPassword = generatedPassword_List
print(generatedPassword)

   