import tkinter as tk
from tkinter import ttk, filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk
global TkLogo
import mysql.connector as sql
mycon = sql.connect(host="192.168.1.4",user="User",password="Rootpassword123",database="hackathon")
cursor = mycon.cursor()


def TipoffScreen():

    def AddImage():
        global photo,binaryData,filename
        filetype = (('Image files', '*.png'),('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetype)
        showinfo(title='Selected File',message=filename)
        photo = tk.PhotoImage(file=filename)
        ImgLabel.configure(image=photo)

    def convert(filenam):
            
        with open(filenam, 'rb') as filea:
            Data = filea.read()
        return Data

    def Submit(Image):

        DateVal = EntryDate.get()
        DescVal = EntryDesc.get()
        TypeVal = CrimeType.get()

        BinaryImage = convert(filename)

        cursor = mycon.cursor()
        Q1 = "insert into test(Image) values (%s)"

        Q2 = convert(filename)
            
        insert_blob_tuple = (BinaryImage)
        result = cursor.execute(Q1,(Q2,))
        mycon.commit()
        print("Image and file inserted successfully as a BLOB into test table", result)
        
        
    
    root.withdraw()
    TipoffWin = tk.Toplevel()
    
    TipoffWin.state("zoomed")
    TipoffWin.grid_columnconfigure((0,1,2),weight=1)

    tk.Label(TipoffWin, text = "Tipoff screen", font = LabelFont).grid(row=0,column=1)

    DetailsBox = tk.Frame(TipoffWin)
    DetailsBox.grid(row=1,column=1)

    tk.Label(DetailsBox, text = "Enter date of incident : ", font = LabelFont).grid(row=0,column=0,pady=20)
    EntryDate = tk.Entry(DetailsBox, font = LabelFont)
    EntryDate.grid(row=0,column=1)
    DateVal = EntryDate.get()

    tk.Label(DetailsBox, text = "Description of Incident (Max 256 letters)", font = LabelFont).grid(row=1,column=0,pady=20)
    EntryDesc = tk.Entry(DetailsBox, font = LabelFont)
    EntryDesc.grid(row=1,column=1)
    DescVal = EntryDesc.get()

    tk.Label(DetailsBox, text = "Type of crime", font = LabelFont).grid(row=2,column=0,pady=20)
    CrimeTypes = ["Assault","Robbery","Theft"]
    CrimeType = ttk.Combobox(DetailsBox, values = CrimeTypes, font = LabelFont)
    CrimeType.grid(row=2,column=1)
    TypeVal = CrimeType.get()

    tk.Label(DetailsBox, text = "Add an Image of the incident", font = LabelFont).grid(row=3,column=0,pady=20)
    ImgLabel = tk.Label(DetailsBox, text = "Image will appear here (testing purposes)", font = LabelFont)
    ImgLabel.grid(row=3,column=1)
    
    ImgButton = tk.Button(DetailsBox, text = "Add an Image", command = AddImage)
    ImgButton.grid(row=3,column=2)

    SubmitButton = tk.Button(DetailsBox, text = "Submit tipoff", command = lambda : Submit(filename))
    SubmitButton.grid(row=4,column=1)



root = tk.Tk()
root.state("zoomed")
root.grid_columnconfigure((0,1,2),weight=1)

LabelFont = ("TKDefaultFont",16)
ButtonFont = ("TKDefaultFont",18)

GuidelineBox = tk.Frame(root,highlightcolor = "black", highlightthickness = 1)
GuidelineBox.grid(row=3,column=1)

OverwatchLogo = Image.open("logo.png")
OverwatchLogo = OverwatchLogo.resize((100,75),Image.ANTIALIAS)
TkLogo = ImageTk.PhotoImage(OverwatchLogo)

CBILogo = Image.open("cbi.png")
CBILogo = CBILogo.resize((150,100),Image.ANTIALIAS)
TkCBI = ImageTk.PhotoImage(CBILogo)

tk.Label(root,text="Overwatch",font=LabelFont).grid(row=0,column=1)
tk.Label(root,text="Stuff",font=LabelFont).grid(row=1,column=1)

NextButton = tk.Button(root,text = "Get started", command = TipoffScreen, font = ButtonFont)
NextButton.grid(row=2,column=1)

tk.Label(GuidelineBox, text = "Overwatch is a platform through which users may submit their complaints anonymously.", font= LabelFont).grid(row=0,column=0)

root.mainloop()
