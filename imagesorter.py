from tkinter import *
from os import *
import os
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

NO_DIR = 0
EMPTY_DIR = 1

class ImageSorter(object):

    def defaultValues(self):
        self.lblDir.configure(text = '...')
        self.lblCounter.configure(text = "-/-")
        self.filenames = []
        self.index = -1
        self.frmImg.configure(image = self.blackground)

        self.setBtnState('disabled')
        self.bindKeys('unbind')
        
    def formatCheck(self, file):
        for format in self.formats.get().split(';'):
            if format in file.lower() and len(format) > 0:
                return True
        return False

    def setDir(self):
        try:
            tmpdir = filedialog.askdirectory()
            if tmpdir == '':
                raise Exception(NO_DIR)
            else:
                self.dir = tmpdir
        
            self.lblDir.configure(text = self.dir)
            self.filenames = list(filter(self.formatCheck, listdir(self.dir)))
            if len(self.filenames) == 0:
                raise Exception(EMPTY_DIR)

            self.index = 0
            self.updateCounter()
            self.updateImage()

            self.setBtnState('normal')
            self.bindKeys('bind')

        except Exception as e:
            if e.args[0] == NO_DIR:
                messagebox.showinfo('Message', 'No dir choosed.')
            elif e.args[0] == EMPTY_DIR:
                messagebox.showinfo('Message', self.dir + ' is empty.')
                self.defaultValues()
            else:
                messagebox.showinfo('Error', 'Problem with: ' + str(e))        
                self.defaultValues()

    def previous(self):
        try:
            self.index -= 1
            if self.index < 0:
                self.index = len(self.filenames) - 1
            self.updateCounter()
            self.updateImage()
        except Exception as e:
            messagebox.showinfo('Error', 'Problem with: ' + str(e))

    def previousKey(self, event):
        self.previous()

    def next(self):
        try:
            self.index += 1
            self.overMaxIndex()
            self.updateCounter()
            self.updateImage()
        except Exception as e:
            messagebox.showinfo('Error', 'Problem with: ' + str(e))

    def nextKey(self, event):
        self.next()

    def trash(self):
        try:
            if not os.path.isdir(self.dir + '/trash'):
                os.mkdir(self.dir + '/trash')
                    
            filename = self.filenames[self.index]
            os.rename(self.dir + '/' + filename, self.dir + '/trash/' + filename)
            self.filenames = list(filter(self.formatCheck, listdir(self.dir)))
            if len(self.filenames) == 0:
                messagebox.showinfo('Message', self.dir + ' is empty.')
                self.defaultValues()
                return

            self.overMaxIndex()
            self.updateCounter()
            self.updateImage()
        except Exception as e:
            messagebox.showinfo('Error', 'Problem with: ' + str(e))

    def trashKey(self, event):
        self.trash()

    def overMaxIndex(self):
        if self.index >= len(self.filenames):
            self.index = 0
    
    def updateCounter(self):
        self.lblCounter.configure(text = str(self.index + 1) + "/" + str(len(self.filenames)))

    def updateImage(self):
        load = Image.open(self.dir + '/' + self.filenames[self.index])
        HeightDivideByWidth = load.size[1] / load.size[0]
        if HeightDivideByWidth < self.size[1] / self.size[0]:
            width = self.size[0]
            height = int(HeightDivideByWidth * self.size[0])
        else:
            height = self.size[1]
            width = int(self.size[1] / HeightDivideByWidth)
        self.img = ImageTk.PhotoImage(load.resize((width, height)))
        self.frmImg.configure(image = self.img)

    def setBtnState(self, state):
        self.btnLeft['state'] = state
        self.btnDelete['state'] = state
        self.btnRight['state'] = state

    def bindKeys(self, state):
        self.window.bind('<Left>', self.previousKey) if state == 'bind' else self.window.unbind('<Left>')
        self.window.bind('<Right>', self.nextKey)    if state == 'bind' else self.window.unbind('<Right>')
        self.window.bind('<Delete>', self.trashKey)  if state == 'bind' else self.window.unbind('<Delete>') 

    def __init__(self):
        self.window = Tk()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        self.window.geometry(str(screen_width) + 'x' + str(screen_height))
        self.size = (screen_width, int(0.8 * screen_height))
        self.index = -1
        
        self.frmHeader = LabelFrame(self.window)
        self.frmHeader.pack()
        self.lblFormats = Label(self.frmHeader, text = 'Searched for:')
        self.lblFormats.grid(row = 0, column = 0, padx = 10)
        self.formats = StringVar(value = 'jpg;png;jpeg')
        self.txtFormats = Entry(self.frmHeader, textvariable = self.formats)
        self.txtFormats.grid(row = 0, column = 1, padx = 10)
        self.btnDir = Button(self.frmHeader, text = 'Directory:', command = self.setDir)
        self.btnDir.grid(row = 0, column = 2)
        self.lblDir = Label(self.frmHeader, text = '...')
        self.lblDir.grid(row = 0, column = 3, ipadx = 10)
        self.lblCounter = Label(self.frmHeader, text = '-/-')
        self.lblCounter.grid(row = 0, column = 4, ipadx = 20)

        self.blackground = ImageTk.PhotoImage(Image.open('blackground.png').resize(self.size))
        self.frmImg = Label(self.window, image = self.blackground)
        self.frmImg.pack()

        self.frmButtons = Label(self.window)  
        self.btnLeft = Button(self.frmButtons, text = '<', command = self.previous)
        self.btnLeft.grid(row = 0, column = 0, ipadx = int(0.15 * screen_width), ipady = 10)
        self.btnDelete = Button(self.frmButtons, text = 'Delete', command = self.trash)
        self.btnDelete.grid(row = 0, column = 1, ipadx = int(0.15 * screen_width), ipady = 10)
        self.btnRight = Button(self.frmButtons, text = '>', command = self.next)
        self.btnRight.grid(row = 0, column = 2, ipadx = int(0.15 * screen_width), ipady = 10)
        self.frmButtons.pack()
        self.setBtnState('disabled')
        
        self.window.mainloop()

iD = ImageSorter()
