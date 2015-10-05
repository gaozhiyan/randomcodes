#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv
import random
from random import shuffle
import numpy as np

#open condition 1 list (same language same phrase)
with open("cond1.csv","rU") as source:
    lines = [line for line in source]
#take 40 pairs
cond1 = random.sample(lines,40)


#open condition 2 list (same language different phrase)
with open("cond2.csv","rU") as source:
    lines = [line for line in source]
#take 20 pairs
cond2 = random.sample(lines,20)

#open condition 3 list (different language same phrase)
with open("cond3.csv","rU") as source:
    lines = [line for line in source]
#take 40 pairs
cond3 = random.sample(lines,40)



#open condition 4 list (different language different phrase)
with open("cond4.csv","rU") as source:
    lines = [line for line in source]
#take 20 pairs
cond4 = random.sample(lines,20)

#combine lists
cond=cond1+cond2+cond3+cond4
#randomize pairs
stim=random.sample(cond,60)
stim2=list(set(cond)-set(stim))
#insert header
stim.insert(0,lines[0])
stim2.insert(0,lines[0])
with open("new.csv","wb") as sink:
    sink.write("".join(stim))
 
with open("new2.csv","wb") as sink:
    sink.write("".join(stim2))
 