import os

def websetup(a):

    adress=a 
    if(not os.path.exists(adress+"pages")):
        os.mkdir(adress+"pages")

    if(not os.path.exists(adress+"css")):
        os.mkdir(adress+"css")

    if(not os.path.exists(adress+"js")):
        os.mkdir(adress+"js")

    if(not os.path.exists(adress+"imgs")):
        os.mkdir(adress+"imgs")

    open(adress+"index.html","w")  
