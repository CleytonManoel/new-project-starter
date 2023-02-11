import os



def lovesetup(a):

    adress=a 
    if(not os.path.exists(adress+"imgs")):
        os.mkdir(adress+"imgs")


    if(not os.path.exists(adress+"components")):
        os.mkdir(adress+"components")

    if(not os.path.exists(adress+"functions")):
        os.mkdir(adress+"functions")

    open(adress+"main.lua","w")  

