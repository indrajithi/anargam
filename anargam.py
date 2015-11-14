"""
Copyright 2015 Indrajith Indraprastham.
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

Program to find anargam from a given input

"""

def is_anargam(word1, word2):
    """Returns True if anargam is found. Else return False."""
    count = 0
    word1, word2 = list(word1), list(word2)
    if len(word1) == len(word2):     
          for i in word1:
                   if i in word2:
                    word2.remove(i)
                    count += 1               
          if count == len(word1):
               return True
    return False
  

file = open('words.txt')
wd_in = raw_input("enter a jumbled word: ")
found = 0

for line in file:
     if is_anargam(wd_in,line.strip()):
          found += 1
          if found == 1:
               print "The possible anargams are:"
          print line.strip()
          
if found == 0: 
     print "No possible mathch"
else: 
     print "Found %d match." % found
