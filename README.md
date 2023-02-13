# New Project Starter

## Header

- Project
- Git clone
- Shortcut
- New templates


## Project

The project was created to accelerate the speed of projects  production using pre-defined configurations.

Using python the project manages to run on multiple OS without any changes besides being light and fast.

## Git clone

```sh
git clone https://github.com/CleytonManoel/new-project-starter.git
```

## Shortcut

To increase the speed which you create new projects, you can add an alias in your terminal settings.

In ".bashrc" or in ".bash_aliases" add the line:

```sh
alias newproject="cd /;cd "relative path";bash start.sh"
```

Replacing with relative path.


## New 

### To add a new template:

Create a file inside the folder "Setups" with the name of the new template.

Inside the created file import the native python library "os" and create a function with the name of your preference.

```py
import os

def namesetup(a):
    adress=a 
```

To add a new folder to the template add the following code inside the function:


```py 
if(not os.path.exists(adress+"name_folder")):
    os.mkdir(adress+"name_folder")
```

Replacing "name_folder" by the name of the folder you want to create.

To add a new file in the template add the following code inside the function:

```py
open(adress+"name_file.py","w")  
```

Replacing "name_filer.py" by the name of the filer you want to create.

In the end you should have something like:

```py
import os

def namesetup(a):
    adress=a 

    if(not os.path.exists(adress+"name_folder")):
        os.mkdir(adress+"name_folder")

    open(adress+"name_file","w")  
```


In folder "Setups" you will find a file called "__init__.py" inside it import the name given to your new model


```py
from . import name_your_new_model
```


And finally add to the project you need to add in "main.py"

```py
if new_project == "name":
    Setups.name.namesetup(adress_project)
```

Replacing "name" by the name of your new template and "namesetup" by the name of the function you created.
