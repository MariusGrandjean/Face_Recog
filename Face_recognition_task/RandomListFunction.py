# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 13:26:52 2023

@author: ln
"""


import os
import random
import tabulate
from psychopy import core, visual, gui, data, event, monitors, sound



def AnswerscreenDict (folder):
    Images = os.listdir(folder)
    Actor_Name = [i[6:-9].replace("_", " ") for i in Images]
    Actors_list = list(set([i[6:-9].replace("_", " ") for i in Images]))
    Answerscreen = {}
    pos = 0
    for image in Images:
        ListNames = []
        Name_list = Actors_list.copy()
        Name_list.remove(image[6:-9].replace("_", " "))
        ListNames.append(image[6:-9].replace("_", " "))
        for i in range(4):
             random_element = random.choice(Name_list)
             Name_list.remove(random_element)
             ListNames.append(random_element)
        Answerscreen.update({image: ListNames})
    return Answerscreen
    


#I think we don't need this function the main aim is 
def DialogueActors (listFin, Actors):
    dictDlg = gui.Dlg(title='Actors list')
    remain = list(set(Actors) - set(listFin))
    miss = 10 - len(listFin) 
    i = 0
    #info = {}
    n = 0
    for i in listFin:
        dictDlg.addField('Actor' + str(n + 1), i)
        n += 1
    for i in range(miss):
        dictDlg.addField('Actor' + str(n + 1), choices=remain)
        n += 1
    listFin = dictDlg.show()
    listFin = random.sample(listFin, 10)
    return listFin

import itertools
def unlist(list_of_lists):
  """
  Unlists a nested list.
  Args:
    list_of_lists: A nested list.
  Returns:
    A flattened list.
  """
  flattened_list = list(itertools.chain(*list_of_lists))
  return flattened_list






def ActorsPos(list_of_Actors, win, Gpath, Rpath):
    Ans1 = visual.ImageStim(win, size =[16, 2.68])  #add mask parameter it will be automatically faded
    Ans2 = visual.ImageStim(win, size =[16, 2.68]) 
    Ans3 = visual.ImageStim(win, size =[16, 2.68]) 
    Ans4 = visual.ImageStim(win, size =[16, 2.68]) 
    Ans5 = visual.ImageStim(win, size =[16, 2.68]) 
    Ans6 = visual.ImageStim(win, size =[16, 2.68]) 
    Ans7 = visual.ImageStim(win, size =[16, 2.68]) 
    Ans8 = visual.ImageStim(win, size =[16, 2.68]) 
    # Ans9 = visual.ImageStim(win, size =[16, 2.68]) 
    # Ans10 = visual.ImageStim(win, size =[16, 2.68]) 
    
    
    List_pos_test = [(-14, 4.5), (-7, 4.5), (0, 4.5), (7, 4.5), (14, 4.5),
                     (-14,-4.5), (-7, -4.5), (0, -4.5), (7, -4.5), (14, -4.5)]
    Ans1.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[0])))  
    Ans1.pos=(List_pos_test[0])
    Ans1.size=[6.5, 7.5]
    Ans1.draw()
    Ans2.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[1])))  
    Ans2.pos=(List_pos_test[1])
    Ans2.size=[6.5, 7.5]
    Ans2.draw()
    Ans3.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[2])))  
    Ans3.pos=(List_pos_test[2])
    Ans3.size=[6.5, 7.5]
    Ans3.draw()
    Ans4.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[3])))  
    Ans4.pos=(List_pos_test[3])
    Ans4.size=[6.5, 7.5]
    Ans4.draw()
    Ans5.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[4])))  
    Ans5.pos=(List_pos_test[4])
    Ans5.size=[6.5, 7.5]
    Ans5.draw()
    Ans6.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[5])))  
    Ans6.pos=(List_pos_test[5])
    Ans6.size=[6.5, 7.5]
    Ans6.draw()
    Ans7.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[6])))  
    Ans7.pos=(List_pos_test[6])
    Ans7.size=[6.5, 7.5]
    Ans7.draw()
    Ans8.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[7])))  
    Ans8.pos=(List_pos_test[7])
    Ans8.size=[6.5, 7.5]
    Ans8.draw()
    # Ans9.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[8])))  
    # Ans9.pos=(List_pos_test[8])
    # Ans9.size=[6.5, 7.5]
    # Ans9.draw()
    # Ans10.setImage(os.path.join(Gpath, Rpath + str(list_of_Actors[9])))  
    # Ans10.pos=(List_pos_test[9])
    # Ans10.size=[6.5, 7.5]
    # Ans10.draw()