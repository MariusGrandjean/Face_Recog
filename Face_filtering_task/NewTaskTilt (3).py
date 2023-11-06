# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:34:46 2023

@author: ln
"""


#A FAIRE : NE PAS FERMER LA FENÊTRE POUR LA LISTE D2ROULANTE MAIS LA R2DUIRE PUIS A R2AUGMERNTER POUR RN PAS AVOIR 0 RED2FINIR TOUS LES PARAMETRES WIN



#==============================
# Import modules and functions
#==============================

from psychopy import core, visual, gui, data, event, monitors, sound
import random
import os   
import pandas as pd
import pickle
import re
import copy
from RandomListFunction import AnswerscreenDict, DialogueActors, unlist, ActorsPos


#===========================================================
# Store info about the experiment session and set parameters
#===========================================================
 

Gpath = 'C:\\Users\\kurnaz\\Desktop\\Face_filtering_task'
datapath = 'data\\'                   # directory to save data in     
Cpath= 'Consignes\\'
Ppath = 'Prescreening\\'
Rpath = 'Reponses\\'
Spath= 'Stimulus\\'  # directory where images can be found
Mpath= 'Mask\\'


# Gpath = 'C:\Thèse\ProjetHeadTilt'
# datapath = 'data\\'                   # directory to save data in     
# Cpath= 'Consignes\\'
# Ppath = 'Prescreening\\'
# Rpath = 'Reponses\\'
# Spath= 'Stimulus\\'  # directory where images can be found
# Mpath= 'Mask\\'

   
# Get subject's info through a dialog box
exp_name = 'Face_Tilt_Task'
exp_info = {
    'participant': '',
    'session':'',
    }

dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)     #open a dialog box
if dlg.OK == False: # If 'Cancel' is pressed, quit
    core.quit()
        
# Get date and time
exp_info['date'] = data.getDateStr()
#exp_info['exp_name'] = exp_name

# Create a unique filename for the experiment data
if not os.path.isdir(datapath):
    os.makedirs(datapath)
data_fname = exp_info['participant']+ 'session'+ exp_info['session'] + '_' + exp_info['date'] + '.csv'
data_fname = os.path.join(datapath, data_fname)


mon = monitors.Monitor('mon1') #set the window
mon.setSizePix((1920, 1200))
mon.setWidth(49)
mon.setDistance(60)
win = visual.Window(monitor = mon, # Open a window
                    color='grey',
                    units='deg',
                    fullscr=False)
win.mouseVisible=False

Ans1 = visual.ImageStim(win, size =[16, 2.68])  #add mask parameter it will be automatically faded
Ans2 = visual.ImageStim(win, size =[16, 2.68]) 
Ans3 = visual.ImageStim(win, size =[16, 2.68]) 
Ans4 = visual.ImageStim(win, size =[16, 2.68]) 
Ans5 = visual.ImageStim(win, size =[16, 2.68]) 
Ans6 = visual.ImageStim(win, size =[16, 2.68]) 
Ans7 = visual.ImageStim(win, size =[16, 2.68]) 
Ans8 = visual.ImageStim(win, size =[16, 2.68]) 
Ans9 = visual.ImageStim(win, size =[16, 2.68]) 
Ans10 = visual.ImageStim(win, size =[16, 2.68]) 
StimMid = visual.ImageStim(win, size =[16, 2.68])
StimCons = visual.ImageStim(win)
StimIm = visual.ImageStim(win, size=[9, 10.4])
StimText = visual.TextStim(win, colorSpace='rgb255')
fixation = visual.Circle(win=win, radius=0.15, units='deg',fillColor=[-0,-0,-0], lineColor='darkgrey')


mouse= event.Mouse(visible = False, win = win)
logfile = open(data_fname, 'w')
logfile.write('Sujet,Trial,Condition,Filter,Imname,Actor0,Actor1,Actor2,Actor3,Actor4,Actor5,Actor6,Actor7,Actor8,Actor9,Answer,Accu,RT,Score,Scoreperc, \n')

t1 = 0.2
tm = 0.2
t2 = 0.2
trand = random.uniform(0.75,1.35) #I.T.I


# trand = random.uniform(1.25, 1.75)
# t1=0.7
# t2=0.4
# tm = 0.2

sizeNoMod = [9, 10.4]

timer = core.Clock()

#========================================
# Define variables
#========================================


# DictAnswer = AnswerscreenDict (os.path.join(Gpath, Ppath)) #function that makes a dictionnary, each entry for an image with the 5 possible answers names
# Actorn = list(DictAnswer.keys())

Actorn = [file for file in os.listdir(Ppath) if file.lower().endswith('.bmp')]

Actors = [i[6:-8].replace("_", " ") for i in Actorn]  # Extract IDs from filenames
Actors = list(set(Actors))  # Remove duplicates and convert to a list
Actors.sort()  # Sort the list
ActorsRank = ['1', '2', '3', '4', '5', '6', '7', '8']
List_Rand = random.sample(Actorn, len(Actorn))
List_pos = [(0, -7),(-12, -4), (12, -4), (-8, 5), (8, 5)]

ins = ['Diapositive1.bmp', 'Diapositive2.bmp', 'Diapositive3.bmp', 'Diapositive4.bmp', 
       'Diapositive5.bmp', 'Diapositive6.bmp', 'Diapositive7.bmp', 'Diapositive8.bmp', 
       'Diapositive9.bmp', 'Diapositive10.bmp', 'Diapositive11.bmp', 'Diapositive12.bmp', 
       'Diapositive13.bmp', 'Diapositive14.bmp', 'Diapositive15.bmp', 'Diapositive16.bmp', 'Diapositive17.bmp']                # instructions
mask = os.listdir(os.path.join(Gpath, Mpath))


actors_fname = exp_info['participant'] + '_' + 'actors' #define file name
actors_fname = os.path.join(datapath, actors_fname)



#=========================
# Begining of prescreening
#=========================

# showing all 4 images of each actor
# if 4 images are recognized then put the actors in a list and take 10 randomly ? 

if exp_info['session'] == '1':
    for i in ins[:4]:
        cons_imname=os.path.join(Gpath, Cpath + str(i))
        StimCons.setImage(cons_imname)
        StimCons.pos=(0, 0)
        StimCons.draw()
        win.flip() #fliping the screen to show images
        event.clearEvents()
        keys = event.waitKeys(keyList=['space', 'escape'])
        if 'escape' in keys:
            win.close()
            core.quit()
        elif 'space' in keys :
            continue
    win.flip(clearBuffer=True)
    core.wait(1)
    
    
    #Pretest-  I dont need that part it shows the subejct 4 pictures of the same identity, then if the subject can answer all of them correctly, it is taken as one of the stimulus

    foundIm = []
    

    Final_Rand = random.sample(Actors, 8)        
   # DEFINE FINAL_RAND HERE JUST UPLOAD STIMULI ALL OF IT.     

    with open(actors_fname, 'wb') as pickle_file:
        pickle.dump(Final_Rand, pickle_file)    

else:
    with open(actors_fname, 'rb') as pickle_file:
        Final_Rand=pickle.load(pickle_file)


# win = visual.Window(monitor = mon, # Open a window
#                     color='grey',
#                     units='deg',
#                     fullscr=False)
# win.mouseVisible=False
Ans1 = visual.ImageStim(win, size =[16, 2.68]) 
Ans2 = visual.ImageStim(win, size =[16, 2.68]) 
Ans3 = visual.ImageStim(win, size =[16, 2.68]) 
Ans4 = visual.ImageStim(win, size =[16, 2.68]) 
Ans5 = visual.ImageStim(win, size =[16, 2.68]) 
Ans6 = visual.ImageStim(win, size =[16, 2.68]) 
Ans7 = visual.ImageStim(win, size =[16, 2.68]) 
Ans8 = visual.ImageStim(win, size =[16, 2.68]) 
# Ans9 = visual.ImageStim(win, size =[16, 2.68]) 
# Ans10 = visual.ImageStim(win, size =[16, 2.68]) 
StimMid = visual.ImageStim(win, size =[16, 2.68])
StimCons = visual.ImageStim(win)
StimIm = visual.ImageStim(win, size=[9, 10.4])
StimText = visual.TextStim(win, colorSpace='rgb255')
# fixation = visual.Circle(win=win, radius=0.15, units='deg', fillColor='black')
fixation = visual.Circle(win=win, radius=0.15, units='deg',fillColor=[-0,-0,-0], lineColor='darkgrey')




#afficher les 4 images, what's shown here the all 4 image recognised actors-( finalrand) ?
win.mouseVisible=False 
cons_imname=os.path.join(Gpath, Cpath + 'Diapositive5.bmp')
StimCons.setImage(cons_imname)
StimCons.pos=(0, 0)
StimCons.draw()
win.flip() #fliping the screen to show images
event.clearEvents()
keys = event.waitKeys(keyList=['space', 'escape'])
if 'escape' in keys:
    win.close()
    core.quit()
elif 'space' in keys :
    win.flip(clearBuffer=True)
    core.wait(0.1)
print(Final_Rand)
for act in Final_Rand:
    ## this line is a bit hard to undertstad it has 4images of each actor right)
    images = [im for im in List_Rand if str(act) in im]
    List_pos = [(-6,-6), (6,-6), (-6, 6), (6, 6)]
    Ans1.setImage(os.path.join(Gpath, Ppath + str(images[0])))  
    Ans1.pos=(List_pos[0])
    Ans1.size= sizeNoMod 
    Ans1.draw()
    Ans2.setImage(os.path.join(Gpath, Ppath + str(images[1])))  
    Ans2.pos=(List_pos[1])
    Ans2.size= sizeNoMod
    Ans2.draw()
    Ans3.setImage(os.path.join(Gpath, Ppath + str(images[2])))  
    Ans3.pos=(List_pos[2])
    Ans3.size= sizeNoMod
    Ans3.draw()
    Ans4.setImage(os.path.join(Gpath, Ppath + str(images[3])))  
    Ans4.pos=(List_pos[3])
    Ans4.size= sizeNoMod
    Ans4.draw()
    StimMid.setImage(os.path.join(Gpath, Rpath + 'texte_' + str(act.replace("_", "")) + '.png'))
    StimMid.pos=(0, 0)
    StimMid.draw()
    win.flip() #fliping the screen to show images
    core.wait(5)
    win.flip(clearBuffer=True)
    core.wait(0.5)
    
    
#============================
# Begining of the experiment
#============================
# do this get all the images with id's, and whats is same (m) and differnt (d)
Stim = os.listdir(os.path.join(Gpath, Spath))

l = ['id1_im1', 'id1_im2', 'id1_im3','id2_im1','id2_im2','id2_im3',
'id3_im1','id3_im2','id3_im3','id4_im1','id4_im2','id4_im3',
'id5_im1','id5_im2','id5_im3','id6_im1','id6_im2',
'id6_im3','id7_im1','id7_im2','id7_im3','id8_im1','id8_im2',
'id8_im3']


l1m = ['id1_im1','id1_im2','id1_im1','id2_im1','id2_im2','id2_im1','id3_im1','id3_im2',
'id3_im1','id4_im1','id4_im2','id4_im1','id5_im1','id5_im2',
'id5_im1','id6_im1','id6_im2','id6_im1','id7_im1','id7_im2','id7_im1','id8_im1','id8_im2',
'id8_im1']


l2m = ['id1_im3','id1_im3','id1_im2','id2_im3','id2_im3',
'id2_im2','id3_im3','id3_im3','id3_im2','id4_im3','id4_im3','id4_im2','id5_im3','id5_im3',
'id5_im2','id6_im3','id6_im3','id6_im2','id7_im3','id7_im3','id7_im2','id8_im3',
'id8_im3','id8_im2']


l1d = ['id1_im1', 'id1_im2', 'id1_im3','id2_im1','id2_im2','id2_im3',
'id3_im1','id3_im2','id3_im3','id4_im1','id4_im2','id4_im3',
'id5_im1','id5_im2','id5_im3','id6_im1','id6_im2',
'id6_im3','id7_im1','id7_im2','id7_im3','id8_im1','id8_im2',
'id8_im3']


l2d = ['id7_im1','id4_im2','id6_im3','id3_im2','id5_im1','id1_im3','id6_im1','id5_im3',
'id2_im2','id8_im3','id7_im2','id8_im1','id2_im1',
'id8_im2','id2_im3','id1_im2','id4_im1',
'id4_im3','id1_im1','id6_im2','id3_im1','id3_im3','id5_im2','id7_im3']

#we can start from here I think already have the Fİnal_Rand ready. 

#our_Final_Rand=['JustinTimberlake','BradPitt', 'DanielRadcliffe', 'RobertPattinson', 'LeonardoDiCaprio', 'RyanGosling', 'GeorgeClooney','DanielCraig']
#Final_Rand =['JustinTimberlake', 'MattDamon', 'BenStiller','BradPitt', 'DanielRadcliffe', 'RobertPattinson', 'KeanuReeves', 'BenAffleck', 'LeonardoDiCaprio', 'RyanReynolds']
  
#selecting only the images for the 10 actors
random.shuffle(Final_Rand)
actstim=[]
for n in Final_Rand:
    #E-does Actors contain all the ids of the actors?
    i = Actors.index(n)
    i = ActorsRank[i]
    #E-does this get all the image names for the same actor?
    images = [im for im in Stim if 'id' + str(i) +'_' in im]
    #E-contains 10 recognized actors' all images??
    actstim = actstim + images
    
#getting the names of the images without modifications
#E- whats .bmp here represent , extracted image identifiers
pattern = "_(.*?).bmp"
ids = []
for image in actstim:
    id = re.search(pattern, image).group(1)          
    ids.append(id)
ids = list(set(ids))
ids.sort()


newids = dict(zip(l, ids))
nl1m = [newids.get(n, n) for n in l1m] #list with corresponding images names for same1
nl2m = [newids.get(n, n) for n in l2m] #same2
nl1d = [newids.get(n, n) for n in l1d] #diff1
nl2d = [newids.get(n, n) for n in l2d] #diff2

            
ImRep = [] #selecting the 10 text images for the answer screen (with the names)
for i in Final_Rand: 
    ImRep.append('Im_' + str(i) + '.png')
#ImRep=['Im_JustinTimberlake.png', 'Im_MattDamon.png', 'Im_BenStiller.png','Im_BradPitt.png', 'Im_DanielRadcliffe.png', 'Im_RobertPattinson.png', 'Im_KeanuReeves.png', 'Im_BenAffleck.png', 'Im_LeonardoDiCaprio.png', 'Im_RyanReynolds.png']


trials=[]
# filters = ['fs','0','30','60','90','120','150']
# filterrand = ['fs','0','30','60','90','120','150']
filters = ['fs','0','90']
filterrand = ['fs','0','90']
listfs=[]
list0=[]
# list30=[]
# list60=[]
list90=[]
# list120=[]
# list150=[]
# listoflists = [listfs, list0, list30, list60, list90, list120, list150]
listoflists = [listfs, list0, list90]
#making a dictionnary with each trial with the condition written
for filter in filters:
    for i in range(len(nl1m)):
        name1 = 'pos' + str (filter) + '_' + str(nl1m[i]) + '.bmp'
        name2 = 'pos' + str (filter) + '_' + str(nl2m[i]) + '.bmp'
        trials.append({'filter':filter, 'imname1':name1, 'imname2': name2, 'sd': 'same'})
    for i in range(len(nl1d)):
        name1 = 'pos' + str (filter) + '_' + str(nl1d[i]) + '.bmp'
        name2 = 'pos' + str (filter) + '_' + str(nl2d[i]) + '.bmp'
        trials.append({'filter':filter, 'imname1':name1, 'imname2': name2, 'sd': 'diff'})


#to randomize the trials but keep them together by condition
a = len(trials) / len(filters)
i = 0
b = 0
triallist = []       
while i < len(trials):
    c = trials[int(i):int(i + a)]
    random.shuffle(c)
    listoflists[b].append(c)
    b += 1
    i += a 
    c = []

listoflists = unlist(listoflists)
conditions=['upright','inverted']


for a in range (24): #because there are 30 trials per condition (the condition filter-150-different count 30 trials) so 60 for each filter
    random.shuffle(conditions)
    for x in conditions:
        random.shuffle(filterrand)  #different order of the filters in each block
        for i in filterrand: #for each filter
            b = filters.index(i) #take the position of the filter selected because same order in listoflists
            cond = str(x)
            dic = copy.deepcopy(listoflists[b][a])
            dic['Cond'] = x
            triallist.append(dic)
        for i in filterrand: #same but have to repeat the operation
            b = filters.index(i)
            cond = str(x)
            dic = copy.deepcopy(listoflists[b][int(a+24)])
            dic['Cond'] = x
            triallist.append(dic) #need to add 2 per filter and to not put the same twice start at 0 and then 30
    a = 0


ntrial = 0

trials_fname = exp_info['participant'] + '_' + 'trials' #define file name
trials_fname = os.path.join(datapath, trials_fname)
ntrial_fname = exp_info['participant'] + '_' + 'ntrial' #define file name
ntrial_fname = os.path.join(datapath, ntrial_fname)
pickled=False
print('notpickled')

if os.path.exists(trials_fname):
    pickled=True
    print('pickled')
    
if not pickled: 
    print('unpickled, pickling now')
    with open(trials_fname, 'wb') as pickle_file:
        pickle.dump(triallist, pickle_file)
    with open(ntrial_fname, 'wb') as pickle_file:
        pickle.dump([ntrial], pickle_file)
    current_triallist = triallist
    print('session1')        
else: 
    with open(trials_fname, 'rb') as pickle_file:
        triallist=pickle.load(pickle_file)
    with open(ntrial_fname, 'rb') as pickle_file:
        ntrial=pickle.load(pickle_file)
        
    # slicer=slice(int(ntrial[0]),len(triallist),1)
    try:
     slicer = slice(int(ntrial[0]), len(triallist), 1)
    except (TypeError, ValueError, IndexError):
    # Handle the error gracefully, e.g., provide a default value
     slicer = slice(0, len(triallist), 1)

    current_triallist=triallist[slicer]
    with open(trials_fname, 'wb') as pickle_file:
        pickle.dump(triallist, pickle_file)




for i in ins[11:14]:
    cons_imname=os.path.join(Gpath, Cpath + str(i))
    StimCons.setImage(cons_imname)
    StimCons.pos=(0, 0)
    StimCons.draw()
    win.flip() #fliping the screen to show images
    event.clearEvents()
    keys = event.waitKeys(keyList=['space', 'escape'])
    if 'escape' in keys:
        win.close()
        core.quit()
    elif 'space' in keys :
        continue
win.flip(clearBuffer=True)
core.wait(1)  

score = 0
scoretot = 0
cond = 0
l = 0
names = ['imname1', 'imname2']
# tilts = ['full', 'mid', 'up']
tilts = ['upright', 'inversed']

rank = 0
i = current_triallist[0]

while current_triallist.index(i) < len(current_triallist): 
    t = tilts[cond]
    for e in range (rank, int(rank + 6)):
        if e>=len(current_triallist):
            win.close()
            logfile.close()
            core.quit()
            # for e in range (rank, int(rank + x)):
        i = current_triallist[e] 
        fixation.draw()
        win.flip()
        core.wait(trand) #I.T.I
        #random.shuffle(names)
        win.flip(clearBuffer=False)
        StimIm.setImage(os.path.join(Gpath,Spath + i[names[0]]))
        StimIm.pos=(0, 0) #image displayed in the center
        
        if i['Cond'] == 'inversed':
            StimIm.ori = 180
        if i['Cond'] == 'upright':
            StimIm.ori = 0
        
        StimIm.draw()
        win.flip() #fliping the screen to show images
        core.wait(t1) #present first image for t1
        StimCons.setImage(os.path.join(Gpath, Mpath + random.choice(mask)))
        StimCons.pos=(0, 0)
        StimCons.draw()
        win.flip() #show mask
        core.wait(tm)
        StimIm.setImage(os.path.join(Gpath,Spath + i[names[1]]))
        StimIm.pos=(0, 0)
        
        if i['Cond'] == 'inversed':
            StimIm.ori = 180
        if i['Cond'] == 'upright':
            StimIm.ori = 0
         
        StimIm.draw()
        win.flip() #fliping the screen to show target image
        core.wait(t2) #present images for t2
        fixation.fillColor = 'black'
        fixation.draw
        win.flip()
        event.clearEvents()
        fixation.fillColor = 'black'
        fixation.draw()
        event.clearEvents()
        Answer = False
        win.flip() #fliping the screen to show images
        timer.reset()
        core.wait(t2) #present images for 300ms
        CT = core.CountdownTimer(3)
        while Answer == False:
            if CT.getTime() < 0:
                break
            fixation.fillColor = 'black'
            fixation.draw
            win.flip()
            fixation.fillColor = 'black'
            fixation.draw()
            win.flip()
            keys = event.getKeys(keyList=['s', 'l'])
            time = timer.getTime()
            if 'l' in keys:
                rep = 'diff'
                if str(i['sd']) == 'diff':
                    score += 1
                    r = 1
                    fixation.fillColor = 'lightgreen'
                    fixation.draw()
                    win.flip()
                    core.wait(0.2)
                    fixation.fillColor = 'white'
                    fixation.draw   ()             
                    win.flip()
                    core.wait(1)
                    Answer = True
                else:
                    r = 0
                    fixation.fillColor = 'darkred'
                    fixation.draw()
                    win.flip()
                    fixation.fillColor = 'white'
                    fixation.draw()      
                    core.wait(0.2)
                    win.flip()
                    core.wait(1)
                    Answer = True
            elif 's' in keys:
                rep = 'same'
                if str(i['sd']) == 'same':
                    score += 1
                    r = 1
                    fixation.fillColor = 'lightgreen'
                    fixation.draw()
                    win.flip()
                    core.wait(0.2)
                    fixation.fillColor = 'white'
                    fixation.draw()
                    win.flip()
                    core.wait(1)
                    Answer = True
                else:
                    r = 0     
                    fixation.fillColor = 'darkred'
                    fixation.draw()
                    win.flip()
                    core.wait(0.2)
                    fixation.fillColor = 'white'
                    fixation.draw()
                    win.flip()
                    core.wait(1)
                    Answer = True
            else:
                rep = 'none'  
        timer.reset()
        toSave = exp_info['participant'] + ',' + str(current_triallist.index(i)) + ',' + str(t) + ',' + str(i['filter']) + ',' + str(i[names[0]]) +'_'+ str(i[names[1]]) + ',' + str(ImRep) + ',' + str(rep) + ',' + str(r) + ',' + str(time) + ',' + str(score) + ',' + str(scoretot) +',\n'
        logfile.write(toSave)
        win.flip(clearBuffer=True)
        #core.wait(0.5)
        with open(ntrial_fname, 'wb') as pickle_file:
            pickle.dump([ntrial], pickle_file)
        event.clearEvents()
        mouse.clickReset()
    cond += 1
    if cond == 2 and l != 6: #every 3 small blocs a break
         rank+=14
         scoretot = score * 100 / 12 #there are 42 trials in one big bloc
         if scoretot >= 75:
             StimText.color = (128, 255, 128)
         else:
             StimText.color = (147, 43, 33)
         StimText.text= 'votre score est de : ' + str(round(scoretot)) + '%\n Progression : ' + str((current_triallist.index(i)+1)/6) + '/' + str(len(current_triallist)/6) 
         StimText.draw()
         win.flip()
         core.wait(5)
         score = 0
         win.flip(clearBuffer=True)
         cons_imname=os.path.join(Gpath, Cpath + 'Diapositive15.bmp')
         StimCons.setImage(cons_imname)
         StimCons.pos=(0, 0)
         StimCons.draw()
         win.flip() #fliping the screen to show images
         event.clearEvents()
         keys = event.waitKeys(keyList=['space', 'escape', 'q'])
         if 'escape' in keys:
             break
             win.close()
             core.quit()
         elif 'q' in keys:
             ntrial = current_triallist.index(i)
             with open(ntrial_fname, 'wb') as pickle_file:
                 pickle.dump([ntrial], pickle_file)  
             print('pickled at' + str(ntrial))
             break
             win.close()
             core.quit()
             #break
         elif 'space' in keys :
             ActorsPos(ImRep, win, Gpath, Rpath)
             win.flip() #fliping the screen to show images
             core.wait(4)
             win.flip(clearBuffer=True)
         cond = 0
         l += 1
         random.shuffle(tilts)
    elif cond == 2 and l == 6: #because we will have the long break
         l += 1
         scoretot = score * 100 / 12 #there are 42 trials in one big bloc
         if scoretot >= 75:
             StimText.color = (128, 255, 128)
         else:
             StimText.color = (147, 43, 33)
         StimText.text= 'votre score est de : ' + str(round(scoretot)) + '%\n Progression : ' + str((current_triallist.index(i)+1)/6) + '/' + str(len(current_triallist)/6)  
         StimText.draw()
         win.flip()
         core.wait(5)
         score = 0
         win.flip(clearBuffer=True)
         CT = core.CountdownTimer(30)
         while CT.getTime() > 0:
             cons_imname=os.path.join(Gpath, Cpath + 'Diapositive16.bmp')
             StimCons.setImage(cons_imname)
             StimCons.pos=(0, 0)
             StimCons.draw()
             win.flip() #fliping the screen to show images
             event.clearEvents()
             keys = event.getKeys(keyList=['space', 'escape', 'q'])
             if 'escape' in keys:
                 break
                 win.close()
                 core.quit()
             elif 'q' in keys:
                 ntrial = current_triallist.index(i)
                 with open(ntrial_fname, 'wb') as pickle_file:
                     pickle.dump([ntrial], pickle_file)  
                 print('pickled at' + str(ntrial))
                 break
                 win.close()
                 core.quit()
         cons_imname=os.path.join(Gpath, Cpath + 'Diapositive17.bmp')
         StimCons.setImage(cons_imname)
         StimCons.pos=(0, 0)
         StimCons.draw()
         win.flip() #fliping the screen to show images
         event.clearEvents()
         keys = event.waitKeys(keyList=['space', 'escape', 'q'])
         if 'escape' in keys:
             break
             win.close()
             core.quit()
         elif 'q' in keys:
             ntrial = current_triallist.index(i)
             with open(ntrial_fname, 'wb') as pickle_file:
                 pickle.dump([ntrial], pickle_file)
             print('pickled at' + str(ntrial))
             break
             win.close()
             core.quit()
             #break
         elif 'space' in keys :
             ActorsPos(ImRep, win, Gpath, Rpath)
             win.flip() #fliping the screen to show images
             core.wait(4)
             win.flip(clearBuffer=True)
         l = 0
         cond = 0
         rank+=14
         random.shuffle(tilts)
    else: #between small blocs
         core.wait(2.5)
         Bip = sound.Sound('C', secs=0.2)
         Bip.play()
         rank += 14
         core.wait(.5)
win.close()        
logfile.close()
core.quit()

