#Psychopy Tutorial
#Randomization codes

#These codes are for the purpose of illustration
#One needs to adjust the codes for their own data

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv
import random

#these randomization codes are for the situation when you have seperate csv files for each condtion.
#if you don't want to create seperate lists for each condtion, please scroll down to Part II
#Part I
#open english file lists
with open("english.csv","rU") as source:
    data = [line for line in source]

english = data[1:len(data)]
with open("mandarin.csv","rU") as source:
    data = [line for line in source]
#take 2

mandarin=data[1:len(data)]
with open("arabic.csv","rU") as source:
    data = [line for line in source]
#take 2

arabic=data[1:len(data)]

#we have 30 audio files, 10 for each language. 

#let's create 2 blocks, each block contain 15 files, 5 from each language group

#select english files for block 1 and block2
#for block1
english1=random.sample(english,5)
#for block2
english2=list(set(english)-set(english1))

#similar steps for arabic and mandarin files

arabic1=random.sample(arabic,5)
arabic2=list(set(arabic)-set(arabic1))

mandarin1=random.sample(mandarin,5)
mandarin2=list(set(mandarin)-set(mandarin1))


#combine lists
block1=english1+arabic1+mandarin1
block2=english2+arabic2+mandarin2

#randomize files in eachi block

block1random=random.sample(block1,15)
block2random=random.sample(block2,15)

#insert header
block1random.insert(0,data[0])
block2random.insert(0,data[0])

print english
#create condition files. We don't need to create condition files if we do everything in the coder view, but if we are using the 
#code component in the builder view, then we need to output the data, and then link the csv files to each trial loop.
with open("block1.csv","wb") as sink:
    sink.write("".join(block1random))
 
with open("block2.csv","wb") as sink:
    sink.write("".join(block2random))
 
#Part II
#!/usr/bin/env python2
# -*- coding: utf-8 -*-


#we first import the packages we need
#csv for dealing with csv files, random for randomization
import csv 
import random

# fist we load the file, and call it "data", you can all it anything you like.
# the following two lines is how python reads a csv file.
with open("conditionFile.csv","rU") as source:
    data = [line for line in source]



# now the data is loaded, our mission at this point is the seperate the data into 3 pieces
# we want seperate lists for english, arabic and mandarin files

# first we define some global variables. "english=[]" tells python that we want to create 
# a list called "english", and now is empty "[]" means the list does not contain anything.
# we will add stuff to the list later on
english=[]
mandarin=[]
arabic=[]

# first we select the english files
# the for loop tells python to look through the "data", and locate any element that has 
# the word "english" in it. if an element contains the word "english", than add it to the list "english"
# now we get a list that contains all the "english files"
for i in range(len(data)):
    if "english" in data[i]:
        english.append(data[i])


# similarly we can get the list for mandarin and arabic

for i in range(len(data)):
    if "mandarin" in data[i]:
        mandarin.append(data[i])


for i in range(len(data)):
    if "arabic" in data[i]:
        arabic.append(data[i])

######## the block creating techniques are the same as in Part I, but this time we only use a subset of the data. Not all the data.
######## this is useful if you have a large set of stimuli (say 1000 sound files), and you don't want each participant to listen to all the stimuli,
######## but only a subset of the sound files (e.g. 100)
# in our experiment, we want our listeners to listen to all the files at random
# but we want to make sure that the 3 types of files are equally distributed. 
# we don't want the listeners to listen to say 4 english files in a row
# so we want to create some blocks. 
# let's say we want the listeners to listen to only 12 files, 4 english, 4 mandarin, and 4 arabic
# we want to create 2 blocks, each block contain 6 files with 2 english files, 2 mandarin files and 2 arabic files.

# lets create the first block by randomly selecting 2 files from each language category

# first we randomly select 2 english files 
# we use function "random.sample()" to do that. 

english1=random.sample(english,2) # as you can see, we first enter the list name "english", than we enter the number of files we want
mandarin1=random.sample(mandarin,2)
arabic1=random.sample(arabic,2)

# now we combine the 6 files to create block 1

block1=english1+mandarin1+arabic1

#let's use print block1 to see want block1 actually contains
print block1 #we don't need to print the list. I do "print block1" here for the purpose of debugging 

#now lets randomize the order of files in block1

block1random=random.sample(block1,6)

#let's see the randomized block1
print block1random

#now let's create the second block
#we want another 2 english files, but we don't want the files we have already selected in block1
# so we exclude english1 from the english list

englishleft=list(set(english)-set(english1))
#take 2 files from what's left

english2=random.sample(englishleft,2)

#similarly we get arabic and mandarin files

arabicleft=list(set(arabic)-set(arabic1))
arabic2=random.sample(arabicleft,2)

mandarinleft=list(set(mandarin)-set(mandarin1))
mandarin2=random.sample(mandarinleft,2)

#now we can get block2

block2=english2+arabic2+mandarin2

block2random=random.sample(block2,6)

print block2random


#we can combine the two blocks by doing 

all=block1random+block2random

#and then create a new list

#insert header. 
all.insert(0,data[0]) #this tells python the insert the first row of our original data file

#now create a new list, which we will be use for our experiment.

with open("new.csv","wb") as sink:
    sink.write("".join(all))
   
  
#go back to your folder, you should see a new file called new.csv. this will be the condition file 


#if we want to have a break in between our experiments, than we could let people do block1 first 
# and the block2. in this case, we need to condition files.

#create a csv file for block1
#insert headers
block1random.insert(0,data[0])

with open("new1.csv","wb") as sink:
    sink.write("".join(block1random))

block2random.insert(0,data[0])

with open("new2.csv","wb") as sink:
    sink.write("".join(block2random))
   
  
#run the codes, you will see two more csv files, which can be used seperately 


#copy the codes in to the coder component at the begining of your experiment, link your condition file setting to

# the newly-created, randomized csv files.


#Challenge youself with this assignment

# create a third block containing another 6 sound files (2 from each category). Make sure that the files in the third block haven't been used in block1 and block2 
