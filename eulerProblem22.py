'''
    Using names.txt. a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
    Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 
    938th name in the list. So, COLIN would obtain a score of 
    938 * 53 = 49714.

    What is the total of all the name scores in the file?
'''
#Imports
from string import ascii_uppercase

names = [
   word.replace('"', '') 
    for line in open("names.txt") 
    for word in line.split(",")
]

names.sort()

alphabets = list(ascii_uppercase)

final_sum = 0
for idx, name in enumerate(names):
   name_sum = 0
   for char in name:
      name_sum = name_sum + alphabets.index(char) + 1
   final_sum = final_sum + ((idx + 1) * name_sum)

if __name__ == "__main__":
   print(final_sum)
