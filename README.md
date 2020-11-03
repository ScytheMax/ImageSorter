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

2. 'Directory' button: Opens a directory dialog. Choose your image directory.

3. '<' and '>' buttons: Click on it to go the previous or next image.

3. 'Delete' button: The actually choosed image will be moved to a 'trash' subdirectory in your actually choosen directory.

# Bugfixes

a. 'Bug: buttons disappear while switching through images' issue from @marcelpetrick

-> using '.pack()' for the three main widgets instead of '.grid(...)' solves it

# Further ideas

b. Include upper case endings automatically in the 'Searched for' textbox.

-> Issue: In your directory are images with ending 'JPG'. Then the ImageSorter don't load any image.

c. Counting label to see the image size of the directory and the running number of the actually choosen image.

-> Idea: 'Image 33 of 57'