import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as st
from tkinter import Canvas, Frame, Label, PhotoImage, messagebox
from functools import partial
from PIL import ImageTk, Image
import subprocess
import time
from tkinter.ttk import Progressbar
import threading
import json
import os


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
    #==== Content of files ================================================================#
    #===== Add .gitignore file
    git = """
    node_modules
    .cache/
    dist/
    .env
    .DS_Store
    coverage/
    .vscode/"""
    #=== .prettierrc.json file
    pretty = """
    {
        "singleQuote": true
    }
    """
    #===== .eslintrc.json file
    eslint = """
    {
        "extends":[
            "eslint:recommended",
            "plugin:import/errors",
            "plugin:react/recommended",
            "plugin:jsx-a11y/recommended",
            "prettier",
            "prettier/react",
            "airbnb"],
            "rules":{
                "react/prop-types":0,
                "react/jsx-filename-extension": [1, { "extensions": [".js", ".jsx"] }],
                "react-hooks/rules-of-hooks": "error",
                "react-hooks/exhaustive-deps":1,
                "no-console":1,
                "no-sequences":"off"
            },
        "plugins":["react","import","jsx-a11y","react-hooks"],
        "parserOptions":{
            "ecmaVersion":11,
            "sourceType":"module",
            "ecmaFeatures":{
                "jsx":true
            }
        },
        "env": {
            "browser": true,
            "es2020": true,
            "node": true
        },
        "settings":{
            "react":{
                "version":"detect"
            }
        }
    }
    """
    #index.html
    indexHtml = """
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
        <link rel="stylesheet/css" href="style.css" />
    </head>
    <body>
        <div id="root">content not rendered</div>
        <script src="./App.js"></script>
    </body>
    </html>
    """
    #App.js
    appJs = """
    import React from 'react';
    import ReactDOM from 'react-dom';

    const App = () => (
    <div>
        <p>dekh liya? AA gaya swad?</p>
    </div>
    );
    ReactDOM.render(<App />, document.getElementById('root'));

    """
    #style.css
    styleCss = ''


class widgets:
    def __init__(self, main):
        super().__init__()
        self.window = main
        # Set window title
        self.window.title('Create ReactJs Project')
        # Set window size
        self.window.geometry("720x530")
        #disable resizing
        self.window.resizable(False, False)
        # Set window background
        self.window.configure(bg='#262625')
        #create frames
        self.headerFrame = Frame(self.window, background="#262625")
        self.headerFrame.grid(row=0, column=0, sticky="NSEW", pady=10)
        self.footerFrame = Frame(self.window)
        self.createHeader()
        self.createFirstWindow()

    def createHeader(self):  #creates global header for application
        self.titleIamge = Canvas(self.headerFrame,
                                 width=600,
                                 height=120,
                                 background="#262625",
                                 bd=0,
                                 highlightthickness=0)
        self.titleIamge.grid(row=0, column=0, padx=55)
        self.img = ImageTk.PhotoImage(Image.open("images/titleIcon.png"))
        self.titleIamge.create_image(240, 80, image=self.img)

    def createFirstWindow(self):  # creates first window
        self.contentFrame1 = Frame(self.window,
                                   background="#262625",
                                   highlightbackground="#42B3D2",
                                   highlightthickness=1,
                                   relief=tk.RAISED,
                                   borderwidth=0)
        self.contentFrame1.grid(row=1, column=0, sticky="NS", pady=10, padx=0)
        self.createForm()
        #self.createLabelFields()
        #self.createInputFields()
        #self.createGraphics()
        #self.actionButtons()

    def createForm(self):  #creates form for fisrt window
        # ================================= creation and placement of form labels ========================== #
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
        # ================================= creation and placements of form inputs ========================== #
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

        # ================================= creation and placements of action buttons ========================== #

        #for choose button
        self.folderimg = PhotoImage(file="images/folderIcon.png")
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
        self.infoimg = PhotoImage(file="images/infoIcon.png")
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
        self.startimg = PhotoImage(file="images/startIcon.png")
        self.submitBtn = tk.Button(self.contentFrame1,
                                   text="Start",
                                   borderwidth=0,
                                   highlightthickness=0,
                                   background="#1d84bf",
                                   foreground="white",
                                   activebackground="#2b2b2a",
                                   cursor="hand1",
                                   command=self.processData).grid(row=5,
                                                                  column=1,
                                                                  sticky=tk.W +
                                                                  tk.E,
                                                                  padx=15,
                                                                  pady=20)

        # ================================= creation and placements of decorative images ========================== #
        self.graphicImage = Canvas(self.contentFrame1,
                                   width=130,
                                   height=140,
                                   background="#262625",
                                   bd=0,
                                   highlightthickness=0)
        self.graphicImage.grid(row=3, column=3, rowspan=3, padx=60)
        self.img2 = ImageTk.PhotoImage(Image.open("images/graphics1.png"))
        self.graphicImage.create_image(70, 70, image=self.img2)

    #---------------- action functions --------------------------------------------------------------------------------#
    def selectFolder(self):  #folder selection widget for form input
        self.folder_selected = filedialog.askdirectory()
        self.e1.configure(state='normal')
        self.e1.delete(0, last=len(self.e1.get()))
        self.e1.insert(0, self.folder_selected)
        self.e1.configure(state='disabled')

    def processData(self):  #handling of form data once submitted
        #storing form data
        self.dirPath = self.e1.get()
        self.name = self.e2.get()
        self.version = self.e3.get()
        self.description = self.textarea.get("1.0", tk.END)
        os.system(f"mkdir {self.dirPath}/{self.name}")
        self.createSecondWindow()  #!important creation of second window
        #self.createThirdWindow()
    # ===================================== ++++++++++++++++++++++++++ =================================== #
    # ============================================  Second window ======================================== #
    # ===================================== ++++++++++++++++++++++++++ =================================== #

    def createSecondWindow(self):  #second window initialization
        #distroy current widgets
        self.contentFrame1.destroy()
        self.contentFrame2 = Frame(self.window,
                                   background="#262625",
                                   highlightbackground="#42B3D2",
                                   highlightthickness=1,
                                   relief=tk.RAISED,
                                   borderwidth=0)
        self.contentFrame2.grid(row=1, column=0, sticky="NS", pady=10, padx=0)
        self.createProgressbar()
        self.createConsole()

        #cancle button to terminate process
        self.cancelBtn = tk.Button(self.contentFrame2,
                                   borderwidth=0,
                                   text="Terminate tasks",
                                   highlightthickness=0,
                                   background="#bf1d1d",
                                   activebackground="#2b2b2a",
                                   cursor="hand1",
                                   foreground="white",
                                   command=self.cancelTask).grid(row=3,
                                                                 column=0,
                                                                 sticky=tk.W,
                                                                 pady=15,
                                                                 padx=250)
        self.fetchCommands()

    def cancelTask(self):  #cancle processes
        if messagebox.askyesno(
                "Are you sure?",
                "Do you really wants to cancel installation process?"):
            self.contentFrame2.destroy()
            self.createFirstWindow()
        else:
            pass

    def updateFrame(self, ind):  #frame updater function for gif(loader)
        self.frame = self.loaderFrames[ind]
        ind += 1
        ind = ind % (len(self.loaderFrames) - 1)
        self.label.configure(image=self.frame)
        self.contentFrame2.after(200, self.updateFrame, ind)

    def createProgressbar(self):  #main progressbar components

        #status label for progressbar
        self.statusLabel = Label(self.contentFrame2,
                                 text="initializing commands..",
                                 background="#262625")
        self.statusLabel.grid(row=0, column=0, sticky="NW", padx=55, pady=15)

        #loader gif
        self.loaderFrames = [
            PhotoImage(file='images/loader.gif', format='gif -index %i' % (i))
            for i in range(24)
        ]
        self.label = Label(self.contentFrame2, background="#262625")
        self.label.grid(row=0, column=0, sticky="W", padx=25)
        self.contentFrame2.after(0, self.updateFrame, 0)

        #progressbar
        self.p = Progressbar(self.contentFrame2,
                             orient=tk.HORIZONTAL,
                             length=570,
                             mode="determinate",
                             takefocus=True,
                             maximum=100)
        self.p.grid(row=1, column=0, sticky="E", padx=30, pady=2)

    def createConsole(self):  #console creation

        #textarea for logs
        self.showLogsArea = st.ScrolledText(self.contentFrame2,
                                            width=61,
                                            height=8,
                                            borderwidth=0,
                                            highlightthickness=0,
                                            background="#343634",
                                            fg="#68D9B5",
                                            font=('arial', 12, 'normal'))

        self.showLogsArea.grid(row=2, column=0, columnspan=3, pady=10, padx=20)

    def printLogs(self, log, commandDesc=''):  #inserts text in textarea
        #print(log)
        self.statusLabel['text'] = commandDesc
        self.showLogsArea.configure(state='normal')
        # Inserting Text which is read only
        self.showLogsArea.update()
        self.showLogsArea.insert(tk.INSERT, log)
        self.showLogsArea.see("end")
        self.showLogsArea.configure(state='disabled')

    def runCommands(self, command,
                    commandDesc):  #core function for running commands
        self.lock.acquire()
        self.printLogs(
            " > " + command + '\n' +
            '----------------------------------------------\n', commandDesc)
        print(command)
        result = subprocess.getoutput(
            f"cd {self.dirPath}/{self.name}; {command}")
        self.p.step(99 // len(self.commandList))
        self.printLogs(result + '\n \n')
        self.counter += 1
        if self.counter >= len(self.commandList):
            self.generateFiles()
        self.lock.release()
       

    def fetchCommands(self):  #fetch commands from commands.json
        #multithreading synchronization lock
        self.lock = threading.Lock()

        #reading json
        cmdFile = open("commands.json", "r")
        commandJsonObject = json.load(cmdFile)
        self.commandList = commandJsonObject["linux"]['commands']
        self.counter = 0
        for cmd in self.commandList:
            threading.Thread(target=self.runCommands,
                             args=(cmd, self.commandList[cmd])).start()
            #t1.start()
            #self.contentFrame2.after(200, self.runCommands(cmd))

    #message widget
    def messageWidget(self, message, mtype):
        if mtype == 'info':
            messagebox.showinfo("Information", message)
        elif mtype == "error":
            messagebox.showerror("Opps An Error Occured", message)
        elif mtype == "warning":
            messagebox.showwarning("Warning", message)

    def generateFiles(self):
        dirPath, name, version, description = self.dirPath, self.name, self.version, self.description
        dirPath = f"{dirPath}/{name}"
        #======================= generating files with content========================================
        filedict = {
            '.gitignore': content.git,
            '.prettierrc.json': content.pretty,
            '.eslintrc.json': content.eslint,
            'src/index.html': content.indexHtml,
            'src/App.js': content.appJs,
            'src/style.css': content.styleCss
        }
        os.system(f"mkdir {dirPath}/src")
        for fil in filedict:
            print(fil)
            with open(f"{dirPath}/{fil}", '+w') as rw:
                rw.write(filedict[fil])

        #==================== updating package file =========

        #=== package.json
        jsonFile = open(f"{dirPath}/package.json", "r")
        json_object = json.load(jsonFile)
        jsonFile.close()

        jsonFile = open(f"{dirPath}/package.json", "w")
        json_object['name'] = name
        json_object['version'] = version
        json_object['description'] = description
        json_object['scripts'][
            'format'] = "prettier \"src/**/*.{js,html}\" --write"
        json_object['scripts']['lint'] = "eslint \"src/**/*.{js,jsx}\" --quiet"
        json_object['scripts']['dev'] = "parcel src/index.html"

        json.dump(json_object, jsonFile, indent=2)
        jsonFile.close()

        #===== package-lock.json
        jsonFile = open(f"{dirPath}/package-lock.json", "r")
        json_object = json.load(jsonFile)
        jsonFile.close()

        jsonFile = open(f"{dirPath}/package-lock.json", "w")
        json_object['name'] = name
        json_object['version'] = version

        json.dump(json_object, jsonFile, indent=2)
        jsonFile.close()
        self.statusLabel['text'] = "installation finished!"
        self.printLogs("\nHappy Coding \n")
        self.contentFrame2.after(4000,self.createThirdWindow)
    
    def createThirdWindow(self):
        self.contentFrame2.destroy()
        self.contentFrame3 = Frame(self.window,
                                   background="#262625",
                                   highlightbackground="#42B3D2",
                                   highlightthickness=1,
                                   relief=tk.RAISED,
                                   borderwidth=0)
        self.contentFrame3.grid(row=1, column=0, sticky="NS", pady=10, padx=0)
        self.showInfo()
    def showInfo(self):
        # ================================= creation and placements of decorative images ========================== #
        self.tickImage = Canvas(self.contentFrame3,
                                   width=40,
                                   height=40,
                                   background="#262625",
                                   bd=0,
                                   highlightthickness=0)
        self.tickImage.grid(row=0, column=0,sticky=tk.W,padx=14)
        self.img3 = ImageTk.PhotoImage(Image.open("images/tick.png"))
        self.tickImage.create_image(20, 20, image=self.img3)
        Label(self.contentFrame3,
              text="React Project has been created successfully",
              background="#262625",font=("",12)).grid(row=0,
                                         column=0,
                                         sticky=tk.W + tk.N,
                                         padx=50,
                                         pady=13)
        # Label(self.contentFrame3,
        #       text="Instructions :",
        #       background="#262625",font=("",11)).grid(row=1,
        #                                  column=0,
        #                                  sticky=tk.W + tk.N,
        #                                  padx=20,
        #                                  )
        Label(self.contentFrame3,
              text="npm run format",
              background="#1a1919",foreground="#68D9B5",width=72,font=("Times New Roman", 12)).grid(row=2,
                                         column=0,
                                         sticky=tk.W,
                                         padx=20,
                                         pady=7)
        Label(self.contentFrame3,
              text="> Run this command to format whole project's source code. You can always change this format settings in '.prettierrc.json' file ",
              background="#262625",font=("", 10),wraplength=616, justify="left").grid(row=3,
                                         column=0,
                                         sticky=tk.W + tk.N,
                                         padx=20,
                                         )   
        Label(self.contentFrame3,
              text="npm run -- --fix lint",
              background="#1a1919",foreground="#68D9B5",width=72,font=("Times New Roman", 12)).grid(row=4,
                                         column=0,
                                         sticky=tk.W,
                                         padx=20,pady=7)
        Label(self.contentFrame3,
              text="> Run this command to fix all auto-fixable errors. You can always change lint settings in '.eslintrc.json' file",
              background="#262625",font=("", 10),wraplength=616, justify="left").grid(row=5,
                                         column=0,
                                         sticky=tk.W + tk.N,
                                         padx=20,
                                         )   

        Label(self.contentFrame3,
              text="npm run dev",
              background="#1a1919",foreground="#68D9B5",width=72,font=("Times New Roman", 12)).grid(row=6,
                                         column=0,
                                         sticky=tk.W,
                                         padx=20,
                                         pady=7)
        Label(self.contentFrame3,
              text="> Run this command to start development server with babel. Parcel web bundler is pre-configured.",
              background="#262625",font=("", 10),wraplength=616, justify="left").grid(row=7,
                                         column=0,
                                         sticky=tk.W + tk.N,
                                         padx=20,
                                         )

        #cancle button to terminate process
        self.QuitBtn = tk.Button(self.contentFrame3,
                                   borderwidth=0,
                                   text="Quit",
                                   highlightthickness=0,
                                   background="#bf1d1d",
                                   activebackground="#2b2b2a",
                                   cursor="hand1",
                                   foreground="white",
                                   command=lambda:self.window.destroy()).grid(row=10,
                                                                 column=0,
                                                                 sticky=tk.W,
                                                                 pady=17,
                                                                 padx=280)
if __name__ == "__main__":
    window = tk.Tk()
    wg = widgets(window)
    window.mainloop()