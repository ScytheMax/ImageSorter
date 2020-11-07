# Author
https://github.com/ScytheMax

# License
GNU GPL v3.0

# Required modules
tkinter (pip install tkinter)
os (should be pre installed with python)
PIL (pip install pillow)

# Purpose
Previewer for images.

Functions:

1. 'Searched for' textbox: Define, for which image file endings you are searching.

-> pre filled with jpg and png
-> for example you want to add 'jpeg', then write semicolon and 'jpeg' (result in textbox then 'jpg;png;jpeg')
-> uppercase endings are included ('jpg' searches also for 'Jpg' and 'JPG') 

2. 'Directory' button: Opens a directory dialog. Choose your image directory. After choosing a directory
	the running image number and the total image number of this directory is shown.

3. '<' and '>' buttons: Click on it to go the previous or next image.

3. 'Delete' button: The actually choosed image will be moved to a 'trash' subdirectory in your actually choosen directory.

# Bugfixes

a. 'Bug: buttons disappear while switching through images' issue from @marcelpetrick

-> using '.pack()' for the three main widgets instead of '.grid(...)' solves it

# Further ideas

d. Using arrow keys for switching images. Using delete key for deleting the actually image.