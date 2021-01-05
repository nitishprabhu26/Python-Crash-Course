# importing functionality from external python files

import useful_tools

print(useful_tools.roll_dice(10))

# https://docs.python.org/3/py-modindex.html (List of Python Modules)

'''where are these files/modules stored - 2types of modules --> built in & external
built in modules -built into the python language and we automatically have access to them.
external modules - Located in the same folder in which we have installed python on our computer
(some third party ones to be installed externally and are not present in the Lib folder(External libraries))

eg(third party external module): Python-docx (create/format word docs) --> can be installed using pip

pip - a program(comes preinstalled with python3) a package manager- to (install/manage/update and uninstall various python modules)
Run 'pip install python-docx' on command prompt
[when you install 
external modules, it will be placed inside Lib-->site-packages folder (we can see 2 folders, docx and python-dox.. )]
Now we can import docx, and (use docx.____)
When you do pip uninstall python-docx , those folders will be removed'''