from tkinter import *
import tkinter as tk
from tkinter import filedialog
import formatter
import os
from PIL import ImageTk, Image 
 
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("CSV Formatter")
        self.geometry('840x400')
        self.custName =  tk.StringVar(None)
        self.file_name = []
        
        # self.wm_iconbitmap('logo.png')
        self.img_path = r"C:\Users\Administrator\Documents\Project\logo.ico" #give path to your logo path(file should be ico format)
        self.image2 =Image.open(self.img_path)
        self.image1 = ImageTk.PhotoImage(self.image2)
        self.label1 = Label(self, image=self.image1, justify=CENTER, height=70,)
        self.label1.place(x=240,y=250)

        self.img = PhotoImage(file=r'C:\Users\Administrator\Documents\Project\logo.gif') #give path to your logo path(file should be gif format)
        self.tk.call('wm', 'iconphoto', self._w, self.img)
        
        
 
        self.labelFrame = tk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 1, row = 1, padx = 20, pady = 20)

        self.tx1 = tk.Entry(self.labelFrame,width=80)
        self.tx1.grid(row=0,column=1,sticky="nsew",padx=10,pady=5)
        # print(str(self.open))
        self.tx2 = tk.Entry(self.labelFrame,width=80)
        self.tx2.grid(row=1,column=1,sticky='we',padx=10,pady=5)
        self.tx3 = tk.Entry(self.labelFrame,width=80,)
        self.tx3.grid(row=2,column=1,sticky='we',padx=10,pady=5)
        
        self.button()
        self.labels()
 
 
 
    def button(self):
        self.button = tk.Button(self.labelFrame, text = "Browse A File",command =lambda: self.open(1)).grid(column = 2, row = 0,pady=5)
        # command=lambda:var.set(tkFileDialog.askopenfilename())
        self.button1 = tk.Button(self.labelFrame, text = "Browse A File",command =lambda: self.open(2)).grid(column = 2, row = 1,pady=5)
        self.button2 = tk.Button(self.labelFrame, text = "Open Converted File path",command =lambda: self.open(4)).grid(column = 2, row = 2,padx=5,pady=5)
        self.convert_bt = tk.Button(self,width=10,text='Convert',command=lambda: self.open(3)).place(x=660,y=170)
        self.exit_bt = tk.Button(self,width=10,text='Exit!',command=self.quit).place(x=560,y=170)
        self.clear_bt = tk.Button(self,width=10,text='clear all!',command=lambda: self.open(5)).place(x=460,y=170)

    def labels(self):
        self.lb1 = tk.Label(self.labelFrame,text='Input CSV: ').grid(row=0,column=0)
        # self.lb1.config(font=("Courier", 44))
        self.lb2 = tk.Label(self.labelFrame,text='Template CSV: ').grid(row=1,column=0)
        self.lb3 = tk.Label(self.labelFrame,text='Output CSV: ').grid(row=2,column=0)

    def open(self,bt):
        self.conv_fl = list()
        if bt==1:
            self.filename = tk.filedialog.askopenfilename(title='Choose a file',filetypes = (("csv files","*.csv"),))
            print('bt1 clicked')
            self.file_name.append(self.filename)
            self.tx1.delete(0,tk.END)
            self.tx1.insert(tk.END, self.filename)

        elif bt==2:
            self.filename = tk.filedialog.askopenfilename(title='Choose a file',filetypes = (("csv files","*.csv"),))
            print('bt2 clicked')
            self.file_name.append(self.filename)
            self.tx2.delete(0,tk.END)
            self.tx2.insert(tk.END, self.filename)

        elif bt==3:
            self.tx3.delete(0,tk.END)
            formatter.main( self.file_name)
            
            if os.path.isfile(self.file_name[-1]):
                self.tx3.delete(0,tk.END)
                print('Converted')
                self.file_name.append (os.getcwd()+'\\new_format_{}.csv'.format(self.file_name[-2].split('/')[-1].split('.')[0]))
                self.tx3.insert(tk.END, self.file_name[-1])
                print(self.file_name)
            else:
                self.tx3.insert(tk.END,'File Not Converted')

        elif bt ==4: 
            try:
                if os.path.isfile(self.file_name[-1]):
                    os.startfile(self.file_name[-1])
                    print('file opened')
                    
                else:
                    print(self.file_name[-1])
                    self.tx3.delete(0,tk.END)
                    self.tx3.insert(tk.END,'File Not Converted')
            finally:
                self.tx3.delete(0,tk.END)
                self.tx3.insert(tk.END,'File Not Converted')
        elif bt==5:
            self.file_name.clear()
            self.tx1.delete(0,tk.END)
            self.tx2.delete(0,tk.END)
            self.tx3.delete(0,tk.END)

root = Root()
root.mainloop()