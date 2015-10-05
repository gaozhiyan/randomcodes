import csv
import random
from random import shuffle

#objectives
#1.6 groups, select 1 stimulus from each group for 18 trials
#2.for each trial, select 2 more stimuli from the 6 groups, in addition to the previously selected 6 stimuli 
    # the 2 stimuli should come from two different groups
    # no 2 pairs contain the same stimuli 
#3.in addition to the 8 target stimuli, for each trial, there are 2 fillers 
    #(? the given filler list contain only 24 stimuli. there should be 36 to guarantee no rep)

#strategies
#before looping, divide stimuli into 6 groups (stim1-stim6).
#1. divide each group into two parts: 1) 18 stimuli(fstim1-6) for obj#1 2) 6 stimuli for obj#2
#2. pair up part 2) of all 6 groups (36 stimuli in total)
    #each pair does not contain two stimuli from the same group. 
        #if group combinations are balanced, we will get C(6,2)=15 pairs (2*15=30 stimuli used)
    #the rest 6 stimuli each represent 1 group, randomly select 2 for 2 times to get 3 more pairs
    #we get 15+3=18 pairs
    #creat list of all pairs twoMoreStim
#3. 18 loops, each loop#1 stimuli from each group (6 in total)___
                       #1 pair from twoMoreStim (2 in total)_____|__
                       #2 filler stimuli (2 in total)_______________|___10 stimuli for each loop
             #end of each loop:a) each group removes the 1 selected stimuli 
                              #b) pairs are selected by list index (i.e.twoMoreStim[i]), no need to be removed
                              #c) items within the combined list (twoMoreStim+fstim1-6 +fillers) is randomized
                                    #making sure that properties (i.e. target, filler, group) of each stimulus do not relate to its index in the combined list
                              #d) write each combined list to a csv file
                              #e) feed each csv conditonFile to the trialList argument in the TrialHandeler function
                                    #if looping does not work, then generate 18 conditionFiles first, create 18 routines.

#remaining questions: 1) location of of all wav files, 2) filler list with 36 stimuli 

#prepare lists
fillerlist=list(csv.reader(open('filler.csv','rU')))
stimulilist=list(csv.reader(open('stim.csv',"rU")))
carrierone=[]
carriertwo=[]
carrierthree=[]
carrierfour=[]
carrierfive=[]
carriersix=[]
filler=[]
#get stimuli by condition
for i in range (25):
    carrierone.append(stimulilist[i][2])
    carriertwo.append(stimulilist[i][6])
    carrierthree.append(stimulilist[i][10])
    carrierfour.append(stimulilist[i][14])
    carrierfive.append(stimulilist[i][18])
    carriersix.append(stimulilist[i][22])

for i in range(25):
    filler.append(fillerlist[i][2])
    filler1=filler[1:25]
for i in range(12):
    filler1.append(filler1[i])

stim1=carrierone[1:len(carrierone)]
stim2=carriertwo[1:len(carriertwo)]
stim3=carrierthree[1:len(carrierthree)]
stim4=carrierfour[1:len(carrierfour)]
stim5=carrierfive[1:len(carrierfive)]
stim6=carriersix[1:len(carriersix)]
#break each group into two parts:18+6, fstim1-6 (each contain 18 stimuli) stim1-6(each contain 6 stimuli)
fstim1=random.sample(stim1,18)
for i in range(len(fstim1)):
    stim1.remove(fstim1[i])

fstim2=random.sample(stim2,18)
for i in range(len(fstim2)):
    stim2.remove(fstim2[i])
fstim3=random.sample(stim3,18)
for i in range(len(fstim3)):
    stim3.remove(fstim3[i])
fstim4=random.sample(stim4,18)
for i in range(len(fstim4)):
    stim4.remove(fstim4[i])
fstim5=random.sample(stim5,18)
for i in range(len(fstim5)):
    stim5.remove(fstim5[i])
fstim6=random.sample(stim6,18)
for i in range(len(fstim6)):
    stim6.remove(fstim6[i])
#at this point, each group is divided into two parts.
#the second part (each group has 6 stimuli)
#objective:get 18 non-repeated lists,each contains 2 stimuli from 2 groups. e.g. listA=[group1,group2], listB=[group2,group3]
#there are 36 stimuli,6 groups each contain 6 stimuli, construct 18 pairs
#first 5 group1+2,3,4,5,6

pair1=random.sample(stim1,1)+random.sample(stim2,1) #g1,g2
stim1=list(set(stim1)-set(pair1))
pair2=random.sample(list(set(stim1)-set(pair1)),1)+random.sample(stim3,1)#g1,g3
stim1=list(set(stim1)-set(pair2))
pair3=random.sample(list(set(stim1)-set(pair1)-set(pair2)),1)+random.sample(stim4,1)#g1,g4
stim1=list(set(stim1)-set(pair3))
pair4=random.sample(list(set(stim1)-set(pair1)-set(pair2)-set(pair3)),1)+random.sample(stim5,1)#g1,g5
pair5=random.sample(list(set(stim1)-set(pair1)-set(pair2)-set(pair3)-set(pair4)),1)+random.sample(stim6,1)#g1,g6
stim1=list(set(stim1)-set(pair5)-set(pair4))


pair6=random.sample(list(set(stim2)-set(pair1)),1)+random.sample(list(set(stim3)-set(pair2)),1)#g2,g3
pair7=random.sample(list(set(stim2)-set(pair1)-set(pair6)),1)+random.sample(list(set(stim4)-set(pair3)),1)#g2,g4
pair8=random.sample(list(set(stim2)-set(pair1)-set(pair6)-set(pair7)),1)+random.sample(list(set(stim5)-set(pair4)),1)#g2,g5
pair9=random.sample(list(set(stim2)-set(pair1)-set(pair6)-set(pair7)-set(pair8)),1)+random.sample(list(set(stim6)-set(pair5)),1)#g2,g6
stim2=list(set(stim2)-set(pair6)-set(pair7)-set(pair8)-set(pair9)-set(pair1))
stim3=list(set(stim3)-set(pair2)-set(pair6))
stim4=list(set(stim4)-set(pair3)-set(pair7))
stim5=list(set(stim5)-set(pair4)-set(pair8))
stim6=list(set(stim6)-set(pair5)-set(pair9))

pair10=random.sample(stim3,1)+random.sample(stim4,1)#g3,g4
pair11=random.sample(list(set(stim3)-set(pair10)),1)+random.sample(stim5,1)#g3,g5
pair12=random.sample(list(set(stim3)-set(pair10)-set(pair11)),1)+random.sample(stim6,1)#g3,g6
stim3=list(set(stim3)-set(pair10)-set(pair11)-set(pair12))
stim4=list(set(stim4)-set(pair10))
stim5=list(set(stim5)-set(pair11))
stim6=list(set(stim6)-set(pair12))

pair13=random.sample(stim4,1)+random.sample(stim5,1)#g4,g5
pair14=random.sample(list(set(stim4)-set(pair13)),1)+random.sample(stim6,1)#g4,g6
stim4=list(set(stim4)-set(pair13)-set(pair14))
stim5=list(set(stim5)-set(pair13))
stim6=list(set(stim6)-set(pair14))

pair15=random.sample(stim5,1)+random.sample(stim6,1)#g5,g6
stim5=list(set(stim5)-set(pair15))
stim6=list(set(stim6)-set(pair15))

lastStim=stim1+stim2+stim3+stim4+stim5+stim6

pair16=random.sample(lastStim,2)
pair17=random.sample(list(set(lastStim)-set(pair16)),2)
pair18=list(set(lastStim)-set(pair16)-set(pair17))

#twoMoreStim
twoMoreStim=[pair1,pair2,pair3,pair4,pair5,pair6,pair7,pair8,pair9,pair10,pair11,pair12,pair13,pair14,pair15,pair16,pair17,pair18]
twoMoreStim=random.sample(twoMoreStim,18)


#randomly choose 1 stimulus from each condition, 2 from fillers
#the first part (each group has 18 stimuli) select 1 from each group, loop 18 times
for i in range (18):
    newStim1=random.sample(fstim1,1)
    newStim2=random.sample(fstim2,1)
    newStim3=random.sample(fstim3,1)
    newStim4=random.sample(fstim4,1)
    newStim5=random.sample(fstim5,1)
    newStim6=random.sample(fstim6,1)
    fillers=random.sample(filler1,2)
    list=twoMoreStim[i]+newStim1+newStim2+newStim3+newStim4+newStim5+newStim6+fillers
    listRandom=random.sample(list,len(list))
    listRandom.insert(0,'stim')#add header 'stim', for .setSound() function
    
    #remove all stimuli from fstim1-6
    fstim1.remove(newStim1[0])
    fstim2.remove(newStim2[0])
    fstim3.remove(newStim3[0])
    fstim4.remove(newStim4[0])
    fstim5.remove(newStim5[0])
    fstim6.remove(newStim6[0])
    for i in range (len(fillers)):
        filler1.remove(fillers[i])
    #write to csv file as condtionFile
    print len(filler1)
    conditionFile='conditionFile'+str(i+1)+'.csv'
    with open(conditionFile,'wb') as f:
        writer=csv.writer(f,delimiter=',')
        for name in listRandom:
            writer.writerow([name])
    #embed 'conditionFile 1-18' to trialList in TrialHandeler 
