#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np 
from array import array
import random
#from tabulate import tabulate


# In[2]:


##os.getcwd()


# 

# In[3]:


df1 = pd.read_excel("sorted_Recipes_500.xlsx", sheet_name='Sheet2')
df1.head(3)


# In[4]:


df1.info()


# In[5]:


df2 = pd.read_excel("sorted_Recipes_500.xlsx", sheet_name='Sheet3')
df2.head(3)


# In[6]:


df1 = df1.fillna(0)


# In[7]:


df2 = df2.fillna(0)


# In[29]:


names = df1['TranslatedRecipeName'].str.lower()
names.head(5)


# In[ ]:





# In[30]:



def get_rid(w5):
    global arr
    global arr_names
    global rand_num
    global r_id
    #global w3
    global arr_recipe_selected
    if len(arr_names) < 5:
        r_id = arr[w5]
        #print(w5)
        #print(r_id)
    else:
        r_id = arr_recipe_selected[w5]
        #print(w5)
        #print(r_id)

def user_choice():
    global arr
    global arr_names
    global rand_num
    global w3
    print("Which recipe number do you want to continue with?")
    speak("Which recipe number do you want to continue with?")
    s = 0
    w3 = 0
    while s==0:    
        recipe_num = takeCommand()
        if recipe_num.isdigit():
            w3 = int(recipe_num) - 1
            #print(w3)
            get_rid(w3)
            s=-1
        else:
            print("Please repeat the recipe number")
            speak("Please repeat the recipe number")
            


# In[31]:


def recipe_search(search):
    recipe = ""
    random_recipe = []
    
    global row_no
    global k
    global f 
    global fs
    global arr
    global arr_names
    global rand_num
    global arr_recipe_selected
    global r_id
    arr_recipe_selected = []
    r_id = 0
    row_no = 0 
     
    f = 1
    fs = 1
 
    if " " in search:
        for k in range(0,457):    
            temp = names[k]
            if search in temp:

                r_id = df2.iloc[k,1]

    else:
        h = 0
        arr = np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
        arr_names = []
        for k in range(0,457):    
            temp = names[k]
            recipe = temp.split()
            
            for j in range (0,len(recipe)):
                if (recipe[j] == search) and (h<30):
                    
                    r_id = df2.iloc[k, 1]
                    arr[h] = r_id
                   
            if arr[h] != -1:
                arr_names.append(temp)
                h=h+1
        
        if r_id != 0:
            
            print("Recipes available are:")
            rand_num = []
            while len(rand_num) < len(arr_names):
                rand_var = random.randint(0,len(arr_names)-1)
                #rint(arr)
                if rand_var not in rand_num:
                    rand_num.append(rand_var)

            
            if len(arr_names)<5:
                for w1 in range(0,h):
                    print("Recipe " + str(w1+1)+ " :  " + arr_names[w1])
            else:
                for w1 in range(0,5):
                    print("Recipe " + str(w1+1)+ " :  " + arr_names[rand_num[w1]])
                    arr_recipe_selected.append(arr[rand_num[w1]])
                    print(arr_recipe_selected)
            user_choice()
          
                      
    if r_id != 0:              
        print()
    else:
        print("Recipie not available")
        speak("Recipie not available")
        
        f = -1
        fs= -1
        
        
    for j in range (0,len(df2['Recipe_id'])):
        temp2 = df2['Recipe_id']
        if temp2[j] == r_id:
            row_no = j;   
    


# In[ ]:





# In[32]:



#pip install pyttsx3


# In[33]:


#pip install SpeechRecognition


# In[34]:


import speech_recognition as sr


# In[35]:


import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        
        print("Please speak") 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Please wait, Interpreting your requierment...")
        #print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query


# In[ ]:





# In[36]:


def f2():
    global var
    global i
    global response 
    #global dict1
    var = df1.loc[row_no,i]
    if var != 0:
        var = df1.loc[row_no,i]
        print(var)
        speak(var)
        response = takeCommand().lower()
        
    else:
        i = -1
        
        print("We are done with the ingredients")
        speak("We are done with the ingredients")
        print(" ")
        Ingredients_display()
    
        
def f1():
    global i
    global var
    global response
    
    #global dict1
    
   
    if f==1:
        i = 0
        response = ""
        var = 0
        var = df1.at[row_no,i]
        print("Lets get started with " + names[row_no])
        speak("Lets get started with " + names[row_no])
        print()
        print("Ingredients for the Recipe are:")
        speak("Ingredients for the Recipe are:")
        print()
        print(var)
        speak(var)
        

        response = takeCommand().lower()
    else: 
        i = -1
        
    
    while i!= -1:
       
        
        if response == 'next':
            i=i+1
            f2()
            
        elif response =='repeat':
            f2()
            
        
        elif response =='stop':
            i = -1
            
        elif response == 'pause':
            z = 1
            while z != 0:
                print("Paused... say 'start' to resume")
                speak("Paused")
                y = takeCommand().lower()

                
                if y == 'start':
                    z = 0
                    i = i+1
                    f2()
                
        else:
            speak("Can you please repeat")
            response = takeCommand().lower()
            


# In[ ]:





# In[37]:


def f4():
    global var2
    global i2
    global response2 
    var2 = df2.loc[row_no,i2]
    if var2 != 0:
        var2 = df2.loc[row_no,i2]
        r = str(i2+1)
        print("step " +r+ ": ")
        print(var2)
        speak("step")
        speak(r)
        speak(var2)
        response2 = takeCommand().lower()
        
    else:
        i2 = -1
        print("We are done with the ingredients")
        speak("We are done with the ingredients")
        
        print()

##response = "next"

def f3():
    global i2
    global var2
    global response2
    if fs==1:
        i2 = 0
        response2 = ""
        var2 = 0
        var2 = df2.at[row_no,i2]
        print()
        print("Lets begin cooking !! Lets look at the steps to be followed...")
        speak("Lets begin cooking !! Lets look at the steps to be followed...")
        print()
        print("Step 1: " +var2)
        speak("step 1")
        speak(var2)
        response2 = takeCommand().lower()
    else: 
        i2 = -1
    
    while i2!= -1:
       
        if response2 == 'next':
            i2=i2+1
            f4()
            
        elif response2 =='repeat':
            print("From which step number do you want me to repeat?")
            speak("From which step number do you want me to repeat?")
            s = 0
            while s==0:    
                step_no = takeCommand()
                if step_no.isdigit():
                    i2 = int(step_no) - 1
                    f4()
                    s=-1
                else:
                    print("Please repeat the step number")
                    speak("Please repeat the step number")
                    s=0
                   
        elif response2 =='stop':
            i2 = -1
        
        elif response2 == 'pause':
            p = 1
            while p != 0:
                
                print("Paused... say 'start' to resume")
                speak("Paused")
                q = takeCommand().lower()

                if q == 'start':
                    p = 0
                    i2 = i2 + 1
                    f4()
        
        else:
            speak("Can you please repeat")
            response2 = takeCommand().lower()


# dict1 = {"Ingredient 1" :[],"Ingredient 2" :[],"Ingredient 3" :[],"Ingredient 4" :[],"Ingredient 5" :[],"Ingredient 6" :[],"Ingredient 7" :[],"Ingredient 8" :[],"Ingredient 9" :[],"Ingredient 10" :[],}
# dict1['Ingredient 1'].append(df1.at[row_no,0])
# dict1["Ingredient 2"].append(df1.at[row_no,1])
# dict1["Ingredient 3"].append(df1.at[row_no,2])
# dict1["Ingredient 4"].append(df1.at[row_no,3])
# dict1["Ingredient 5"].append(df1.at[row_no,4])
# dict1["Ingredient 6"].append(df1.at[row_no,5])
# dict1["Ingredient 7"].append(df1.at[row_no,6])
# dict1["Ingredient 8"].append(df1.at[row_no,7])
# dict1["Ingredient 9"].append(df1.at[row_no,8])
# dict1["Ingredient 10"].append(df1.at[row_no,9])
# ing = pd.DataFrame(dict1)
# print(tabulate(ing))

# row_no = 0
# dict1 = {"Ingredient 1" :[],"Ingredient 2" :[],"Ingredient 3" :[],"Ingredient 4" :[],"Ingredient 5" :[],"Ingredient 6" :[],"Ingredient 7" :[],"Ingredient 8" :[],"Ingredient 9" :[],"Ingredient 10" :[],}
# dict1['Ingredient 1'].append(df1.at[row_no,0])
# dict1["Ingredient 2"].append(df1.at[row_no,1])
# dict1["Ingredient 3"].append(df1.at[row_no,2])
# dict1["Ingredient 4"].append(df1.at[row_no,3])
# dict1["Ingredient 5"].append(df1.at[row_no,4])
# dict1["Ingredient 6"].append(df1.at[row_no,5])
# dict1["Ingredient 7"].append(df1.at[row_no,6])
# dict1["Ingredient 8"].append(df1.at[row_no,7])
# dict1["Ingredient 9"].append(df1.at[row_no,8])
# dict1["Ingredient 10"].append(df1.at[row_no,9])
# ing = pd.DataFrame(dict1)
# print(tabulate(ing))
# 

# In[38]:


def Ingredients_display():
    var = 0
    i = 1
    var = df1.at[row_no,i]
    print("Here is the list of all the ingredients")
    speak("Here is the list of all the ingredients")
    print("")
    
    
    
    while i != -1:
        var = df1.loc[row_no,i]
        if var != 0:
            #i = str(i)
            print("Ingredient " + repr(i) +" :  " + var)
            #i = int(i)
            i = i + 1
        else:
            i = -1
        
    
    


# In[39]:



#i=0
#while i!= -1:
 #   steps = df2.at[0,i]
 ##      ##steps = df2.loc[0,i]
   #     print(steps)
    #    i=i+1
    #else:
     #   i= -1


# In[40]:


##print(r_id)


# In[41]:


##x = "Harshil"
##print(x.lower())


# In[ ]:





# In[42]:


##recipe_search('cheesecake')


# def f2():
#     global var
#     global i
#     
#     global row_no
#     var = df1.loc[row_no,i]
#     if var != 0:
#         var = df1.loc[row_no,i]
#         print(var)
#     else:
#         i = -1
#         print("We are done with the ingredients")

# In[ ]:





#  ## f4()  while loop steps
#   while i2 != -1:
#         if response2 == "":
#             i2 = i2 + 1
#             f4()
#         elif repsonse2 == "pause":
#             p = 1
#             while p != 0:
#                 q = takeCommand().lower()
#                 print("Paused... say 'start' to resume")
#                 speak("Paused")
# 
#                 if q == 'resume':
#                     p = 0
#                     i2 = i2 + 1
#                     f4()
#         
#         else:
#             
#             speak("Can you please repeat")
#             response2 = takeCommand().lower()

#   while s==0: 
#                 try:
#                     step_no = int(takeCommand())
#                 except:
#                     print("Please repeat the step number")
#                     speak("Please repeat the step number")
#                     s=0
#                 if is_integer(step_no):
#                     i2 = step_no - 1
#                     f4()
#                     s=-1
#                 
#                 else:
#                     print("Please repeat the step number")
#                     speak("Please repeat the step number")
#                     s=0

# string = "healthy and tasty salad"
# string_1 = "tasty salad"
# 
# if string_1 in string:
#     print('horaha hai')
# else:
#     print("kuch aur karna padega")
# 

# In[43]:


# search = "methi sprouts salad"
# r_id = 0
# for k in range(0,457):    
#     temp = names[k]
#     if search in temp:

#         r_id = df2.iloc[k,1]
#         print(r_id)
#     #else:
#       #  r_id = 0
        
# if r_id != 0:              
#     print("horaha hai")
# else:
#     print("Recipie not available")
#     speak("Recipie not available")

#     f = -1
#     fs= -1
    


# In[44]:


# def recipe_search(search):
#     recipe = ""
#     random_recipe = []
    
#     global row_no
#     global k
#     global f 
#     global fs
#     global arr
#     global arr_names
#     global rand_num
#     global arr_recipe_selected
#     arr_recipe_selected = []
#     r_id = 0
#     row_no = 0 
    
    
#     f = 1
#     fs = 1
    
    
# #     #if search in names:
# #     for k in range(0,457):    
# #         temp = names[k]
# #         #recipe = temp.split()
# #         for j in range (0,len(recipe)):
# #             if recipe[j] == search:
                
# #                 r_id = df2.iloc[k, 1]
# #             #else:
# #              #   r_id = 0

#     if " " in search:
        
    
#         for k in range(0,457):    
#             temp = names[k]
#             if search in temp:

#                 r_id = df2.iloc[k,1]
#            # else:
#             #    r_id = 0

#     else:
#         h = 0
#         arr = np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
#         arr_names = []
#         for k in range(0,457):    
#             temp = names[k]
#             recipe = temp.split()
#             #print(recipe)
#             for j in range (0,len(recipe)):
#                 if (recipe[j] == search) and (h<30):
                    
#                     r_id = df2.iloc[k, 1]
#                     arr[h] = r_id
#                     #print(r_id)
#             if arr[h] != -1:
#                 arr_names.append(temp)
#                 h=h+1
#         #print(arr_names)
                
#         print("Recipes available are:")
#         rand_num = []
#         while len(rand_num) < len(arr_names):
#             rand_var = random.randint(0,len(arr_names)-1)
#             #rint(arr)
#             if rand_var not in rand_num:
#                 rand_num.append(rand_var)
                
#         #print(rand_num)
#         if len(arr_names)<5:
#             for w1 in range(0,h):
#                 print("Recipe " + str(w1+1)+ " :  " + arr_names[w1])
#         else:
#             for w1 in range(0,5):
#                 print("Recipe " + str(w1+1)+ " :  " + arr_names[rand_num[w1]])
#                 arr_recipe_selected.append(arr[rand_num[w1]])
                
#     #print(arr_recipe_selected)          
#     user_choice()
        
# #     if r_id != 0:              
# #         print()
# #     else:
# #         print("Recipie not available")
# #         speak("Recipie not available")

# #         f = -1
# #         fs= -1
     
    
        
# #     for j in range (0,len(df2['Recipe_id'])):
# #         temp2 = df2['Recipe_id']
# #         if temp2[j] == r_id:
# #             row_no = j;

            
            
#             #print(row_no)  
    


# In[45]:



# def get_rid():
#     global arr
#     global arr_names
#     global rand_num
#     global r_id
#     global w3
#     global arr_recipe_selected
#     if len(arr_names) < 5:
#         r_id = arr[(w3)]
#         #print(r_id)
#     else:
#         r_id = arr_recipe_selected[(w3)]
#         #print(r_id)

# def user_choice():
#     global arr
#     global arr_names
#     global rand_num
#     global w3
#     print("Which step number do you want me to repeat?")
#     speak("Which step number do you want me to repeat?")
#     s = 0
#     w3 = 0
#     while s==0:    
#         recipe_num = takeCommand()
#         if recipe_num.isdigit():
#             w3 = int(recipe_num) - 1
#             get_rid()
#             s=-1
#         else:
#             print("Please repeat the step number")
#             speak("Please repeat the step number")
            


# 

# names[2]

# print(random.randint(1,len(names)))

# arr = ["f", "a","c","d"]
# print(len(arr))
# print(arr[3])

# In[46]:



# search = "chessecake"
# h = 0
# arr = np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
# arr_names = []
# for k in range(0,457):    
#     temp = names[k]
#     recipe = temp.split()
#     #print(recipe)
#     for j in range (0,len(recipe)):
#         if (recipe[j] == search) and (h<30):

#             r_id = df2.iloc[k, 1]
#             arr[h] = r_id
#             #print(r_id)
#     if arr[h] != -1:
#         arr_names.append(temp)
#         h=h+1
# #print(arr_names)

# print("Recipes available are:")
# rand_num = []
# while len(rand_num) < len(arr_names):
#     rand_var = random.randint(0,len(arr_names)-1)
#     #rint(arr)
#     if rand_var not in rand_num:
#         rand_num.append(rand_var)

# #print(rand_num)
# if len(arr_names)<5:
#     for w1 in range(0,h):
#         print("Recipe " + str(w1+1)+ " :  " + arr_names[w1])
# else:
#     for w1 in range(0,5):
#         print("Recipe " + str(w1+1)+ " :  " + arr_names[rand_num[w1]])
#         arr_recipe_selected.append(arr[rand_num[w1]])
# user_choice()


# In[47]:


#recipe_search("chessecake")


# In[48]:


# temp = names[4]
# a = temp.split()
# print(a)
# print(len(a))
# a


# In[49]:


#     #if search in names:
#         for k in range(0,457):    
#             temp = names[k]
#             #recipe = temp.split()
#             for j in range (0,len(recipe)):
#                 if recipe[j] == search:

#                     r_id = df2.iloc[k, 1]
#                 #else:
#                  #   r_id = 0


# In[ ]:





# In[ ]:




