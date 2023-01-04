**Description**

A python script to display the images of a directory.

During go through the images it is possible to sort out unwanted images in a trash directory.

<img width="534" alt="git" src="https://user-images.githubusercontent.com/47299122/210542551-e5ff7460-3575-4f6b-bc6b-f19936a3aad8.PNG">

\
**Required modules**

You need an interpreter for python3 and the following modules:

	- tkinter (pip install tkinter-page)
	- os (should be pre installed with python)
	- PIL (pip install pillow)

\
**Functionalities**

	- 'Searched for' textbox: Define, for which image file endings you are searching.
		-> pre filled with jpg, jpeg and png
		-> for example you want to add 'gif', then write semicolon and 'gif' (result in textbox then 'jpg;png;jpeg;gif')
		-> uppercase endings are included ('jpg' searches also for 'Jpg' and 'JPG') 
	- 'Directory' button: Opens a directory dialog. Choose your image directory. After choosing a directory
		the running image number and the total image number of this directory is shown.
	- '<' and '>' buttons: Click on it to go the previous or next image. Also you can use <Left> or <Right> keys.
	- 'Delete' button: The actually choosed image will be moved to a 'trash' subdirectory in your actually choosen directory.
		Also you can use <Delete> key.

\
**License**

GNU GENERAL PUBLIC LICENSE
