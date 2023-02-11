import os
import Setups


print("\033[1;33mYour new project will be created in?\033[m")

adress_project = os.path.join(input()+"/")

print("\033[1;33mThe type your new project is?\033[m")
new_project = input()

if new_project == "love":
    Setups.love.lovesetup(adress_project)

if new_project == "web":
    Setups.web.websetup(adress_project)

if new_project == "python":
    Setups.python.pythonsetup(adress_project)

print("\033[1;32mYour new project was create\033[m")