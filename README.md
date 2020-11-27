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

-> pre filled with jpg, jpeg and png
-> for example you want to add 'gif', then write semicolon and 'gif' (result in textbox then 'jpg;png;jpeg;gif')
-> uppercase endings are included ('jpg' searches also for 'Jpg' and 'JPG') 

2. 'Directory' button: Opens a directory dialog. Choose your image directory. After choosing a directory
	the running image number and the total image number of this directory is shown.

3. '<' and '>' buttons: Click on it to go the previous or next image. Also you can use <Left> or <Right> keys.

4. 'Delete' button: The actually choosed image will be moved to a 'trash' subdirectory in your actually choosen directory.
	Also you can use <Delete> key.

# Bugfixes

a. 'Bug: buttons disappear while switching through images' issue from @marcelpetrick

-> using '.pack()' for the three main widgets instead of '.grid(...)' solves it

# Further ideas
