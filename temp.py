import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as st
from tkinter import Canvas, Frame, Label, PhotoImage, messagebox
from functools import partial
from PIL import ImageTk, Image


class content:
    messages = [
        [
            "Project Name will be used as a project's name (ie. 'my_app') and will be added to package.json",
            'info'
        ],
        [
            "Project version specifies the version of your project (ie. 1.0)",
            'info'
        ],
        [
            "project description is for other team members to get the motive behind the project",
            'info'
        ]
    ]


class widgets:
    def __init__(self, main):
        super().__init__()
        self.window = main
        # Set window title
        self.window.title('Create ReactJs Project')
        # Set window size
        self.window.geometry("720x520")
        #disable resizing
        self.window.resizable(False, False)
        # Set window background
        self.window.configure(bg='#262625')
        #create frames
        self.headerFrame = Frame(self.window, background="#262625")
        self.headerFrame.grid(row=0, column=0, sticky="NSEW", pady=10)
        self.contentFrame1 = Frame(self.window,
                                   background="#262625",
                                   highlightbackground="#42B3D2",
                                   highlightthickness=1,
                                   relief=tk.RAISED,
                                   borderwidth=0)
        self.contentFrame1.grid(row=1, column=0, sticky="NS", pady=10, padx=0)
        self.contentFrame2 = Frame(self.window, background="#262625")
        self.contentFrame2.grid(row=2, column=0, sticky="NSEW", pady=10)
        self.footerFrame = Frame(self.window)
        self.createLabelFields()
        self.createInputFields()
        self.actionButtons()
        #self.createConsole()
        self.createHeader()
        self.createGraphics()

    def createHeader(self):
        self.titleIamge = Canvas(self.headerFrame,
                                 width=600,
                                 height=120,
                                 background="#262625",
                                 bd=0,
                                 highlightthickness=0)
        self.titleIamge.grid(row=0, column=0, padx=55)
        self.img = ImageTk.PhotoImage(Image.open("title.png"))
        self.titleIamge.create_image(240, 80, image=self.img)

    def createGraphics(self):
        self.graphicImage = Canvas(self.contentFrame1,
                                   width=130,
                                   height=140,
                                   background="#262625",
                                   bd=0,
                                   highlightthickness=0)
        self.graphicImage.grid(row=3, column=3, rowspan=3, padx=60)
        self.img2 = ImageTk.PhotoImage(Image.open("graphics1.png"))
        self.graphicImage.create_image(70, 70, image=self.img2)

    def createLabelFields(self):
        Label(self.contentFrame1,
              text="Select Project Directory",
              background="#262625").grid(row=0,
                                         column=0,
                                         sticky=tk.W + tk.N,
                                         padx=20,
                                         pady=23)
        Label(self.contentFrame1,
              text="Enter Project Name",
              background="#262625").grid(row=1,
                                         column=0,
                                         sticky=tk.W,
                                         padx=20,
                                         pady=10)
        Label(self.contentFrame1,
              text="Enter Project Version",
              background="#262625").grid(row=2,
                                         column=0,
                                         sticky=tk.W,
                                         padx=20,
                                         pady=10)
        Label(self.contentFrame1,
              text="Enter Project Description",
              background="#262625").grid(row=3,
                                         column=0,
                                         sticky=tk.W + tk.N,
                                         padx=20,
                                         pady=10)

    def createInputFields(self):
        self.e1 = tk.Entry(self.contentFrame1,
                           borderwidth=0,
                           disabledbackground="#343634",
                           disabledforeground="#c7c9c7",
                           font=("Times New Roman", 12))
        self.e1.grid(row=0, column=1, columnspan=2, padx=8)
        self.e1.insert(0, " -- nothing selected --")
        self.e1.configure(state='disabled')
        self.e2 = tk.Entry(self.contentFrame1,
                           background="#343634",
                           fg="#c7c9c7",
                           borderwidth=0)
        self.e2.grid(row=1, column=1, columnspan=2, padx=8)
        self.e3 = tk.Entry(self.contentFrame1,
                           background="#343634",
                           fg="#c7c9c7",
                           borderwidth=0)
        self.e3.grid(row=2, column=1, columnspan=2, padx=8)
        #textarea for input
        self.textarea = st.ScrolledText(self.contentFrame1,
                                        width=18,
                                        height=4,
                                        borderwidth=0,
                                        highlightthickness=0,
                                        font=("Times New Roman", 12),
                                        background="#343634",
                                        fg="#c7c9c7")
        self.textarea.grid(row=3, column=1, columnspan=2, padx=6, pady=8)

    def createConsole(self):

        #textarea for logs
        self.showLogsArea = st.ScrolledText(self.contentFrame2,
                                            width=50,
                                            height=7,
                                            font=("Times New Roman", 15))

        self.showLogsArea.grid(column=0, columnspan=3, pady=14, padx=50)

        # Inserting Text which is read only
        self.showLogsArea.insert(tk.INSERT, "Loading....")

        # Making the text read only
        self.showLogsArea.configure(state='disabled')
        self.showLogsArea.configure(state='normal')

    def actionButtons(self):
        #for choose button
        self.folderimg = PhotoImage(file="folderIcon.png")
        self.chooseBtn = tk.Button(self.contentFrame1,
                                   background="#262625",
                                   image=self.folderimg,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   activebackground="#2b2b2a",
                                   cursor="hand1",
                                   command=self.selectFolder).grid(row=0,
                                                                   column=3,
                                                                   sticky=tk.W,
                                                                   pady=4)
        #generating information buttons
        messages = content.messages
        #wrapper function
        self.infoimg = PhotoImage(file="infoIcon.png")
        for j in range(0, len(messages)):
            self.infoBtn = tk.Button(
                self.contentFrame1,
                image=self.infoimg,
                borderwidth=0,
                highlightthickness=0,
                background="#262625",
                activebackground="#2b2b2a",
                cursor="hand1",
                command=partial(self.messageWidget, messages[j][0],
                                messages[j][1])).grid(row=j + 1,
                                                      column=3,
                                                      sticky=tk.W + tk.N,
                                                      pady=10)
        #for submit button
        self.startimg = PhotoImage(file="startIcon.png")
        self.submitBtn = tk.Button(self.contentFrame1,
                                   image=self.startimg,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   background="#262625",
                                   activebackground="#2b2b2a",
                                   cursor="hand1",
                                   command=self.processData).grid(row=5,
                                                                  column=1,
                                                                  sticky=tk.W +
                                                                  tk.E,
                                                                  padx=15,
                                                                  pady=20)

    def processData(self):
        print(self.e1.get(), self.e2.get(), self.e3.get(),
              self.textarea.get("1.0", tk.END))

    def selectFolder(self):
        self.folder_selected = filedialog.askdirectory()
        self.e1.configure(state='normal')
        self.e1.delete(0, last=len(self.e1.get()))
        self.e1.insert(0, self.folder_selected)
        self.e1.configure(state='disabled')

    def printLogs(self):
        print("log")

    def runCommands(self, command):
        print("Running command >" + command + "....")

    def messageWidget(self, message, mtype):
        if mtype == 'info':
            messagebox.showinfo("Information", message)
        elif mtype == "error":
            messagebox.showerror("Opps An Error Occured", message)
        elif mtype == "warning":
            messagebox.showwarning("Warning", message)


if __name__ == "__main__":
    window = tk.Tk()
    wg = widgets(window)
    window.mainloop()