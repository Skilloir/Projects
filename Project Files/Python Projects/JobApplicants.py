import json 
import random 
import requests

jobExperience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

currentRating = {}

with open('jobnameList.json') as data_file:
   name = dict.itertools.chain.from_iterable(json.load(data_file).values())



print(name)
def importApplicant(rating):
   jobExperienceGenerator = random.choice(jobExperience)
   JobExperienceAdd = input("This applicant has" + jobExperienceGenerator + " years of experience. \n")
   layoutAllInfo = input("Would you like to lay out all information about this applicant? \n")
   if layoutAllInfo == 'yes':
      print(jobExperienceGenerator )


   




rating = input("On a scale of 1-3, what is \nthe likelyhood of \nthis individual getting accepted?")

