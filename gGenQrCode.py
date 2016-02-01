import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import genQrCode

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        #self.pack()
        self.createWidgets(master)

    def createWidgets(self, root):
        tk.Label(root, text="content",justify="left").grid(row=0)
        tk.Label(root, text="export path").grid(row=1)
        tk.Label(root, text="logo path").grid(row=2)


        self.sourceText = tk.Entry(root)
        self.sourceText.grid(row=0, column=1)

        self.exportPathVar = tk.StringVar()
        #self.exportPathVar.set("Please select a path to store QR code")
        self.exportPath = tk.Entry(root)
        self.exportPath["textvariable"] = self.exportPathVar
        self.exportPath.grid(row=1, column=1)

        self.logoVar = tk.StringVar()
        #self.logoVar.set("Where is the logo?")
        self.logoPath = tk.Entry(root)
        self.logoPath["textvariable"] = self.logoVar
        self.logoPath.grid(row=2, column=1)

        self.exportPathButton = tk.Button(root, text='Select Path', command=self.exportPathCallBack)
        self.exportPathButton.grid(row=1, column=2)
        self.logoPathButton = tk.Button(root, text='Select Path', command=self.logoPathCallBack)
        self.logoPathButton.grid(row=2, column=2)
        
        self.genButton = tk.Button(root)
        self.genButton["text"] = "Gen QR Code"
        self.genButton["command"] = self.genQrCode
        self.genButton.grid(row=3)

    def exportPathCallBack(self):
        name = asksaveasfile(defaultextension=".png")
        print(name.name)
        self.exportPathVar.set(name.name)
        print(self.exportPath.get())

    def logoPathCallBack(self):
        name = askopenfilename()

        self.logoVar.set(name)
        print(self.logoVar.get())

    def genQrCode(self):
        print("gen qr code")
        print(self.sourceText.get(), self.exportPath.get(), self.logoPath.get(), sep=" ", end='\n')
        genQrCode.CreateQrCode(self.sourceText.get(), self.exportPath.get(), self.logoPath.get())


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
