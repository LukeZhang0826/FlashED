#######============================================Code============================================#######
import os
os.system("py -m pip install customtkinter")
os.system("py -m pip install tk")

os.system("pip3 install customtkinter")
os.system("pip3 install tk")

from tkinter import *
from tkinter import filedialog
import customtkinter ### py -m pip install customtkinter --upgrade
from customtkinter import CTkToplevel
import json
import re
import codecs

appearanceMode = "dark" ### Set Appearance Mode: light, dark
colorTheme = "blue" ### Set Color Theme: blue, dark-blue, green
dictionaryEntryLimit = 20 ### Makes the left and right frame scroll more vertically. The larger the value, the slower the app runs

if appearanceMode == "dark": ### General Color Palette
    primaryGrey = "#404040"
    secondaryGrey = "#A0A0A0"
    tertiaryGrey = "#404040"
elif appearanceMode == "light":
    primaryGrey = "#A0A0A0"
    secondaryGrey = "#404040"
    tertiaryGrey = "#A0A0A0"

directoryString = os.path.dirname(os.path.realpath(__file__)) + "\\" ### Directory String

customtkinter.set_appearance_mode(appearanceMode)
customtkinter.set_default_color_theme(colorTheme)

#####============================================Head============================================#####
app = customtkinter.CTk()
app.geometry("550x520")
app.resizable(width=False, height=False)
app.iconbitmap(directoryString + "FED.ico")
app.title("FlashED")

###============================================Pop Up Windows and Functions============================================###
def saveActiveDictionary(dir): ### saves the current active dictionary
    with codecs.open(directoryString + dir + activeDictionaryName + ".json", "w", encoding='utf-8') as outfile:
            json.dump(activeDictionary, outfile, ensure_ascii=False)

def editWord(term): ### edits the selected word
    newWordWindow = CTkToplevel(app)
    newWordWindow.title("Word Editor")
    newWordWindow.iconbitmap(directoryString + "FED.ico")
    newWordWindow.geometry("360x500")
    newWordWindow.resizable(width=False, height=True)

    def saveWord():
        savedTerm = {}
        for i in range(len(frameArr)):
            savedTerm[frameLabelArr[i].cget("text")] = frameTextBoxArr[i].get("0.0", "end").replace("\n", "")
        activeDictionary[term] = savedTerm
        saveActiveDictionary(activeDirectory + "\\")
        newWordWindow.destroy()

    frameTopNW = customtkinter.CTkFrame(master=newWordWindow, width=780, height=40, corner_radius=0)
    frameTopNW.grid(row=0, column=0)
    SearchBoxNW = customtkinter.CTkEntry(master=frameTopNW, width=288, height=35, placeholder_text=term)
    SearchBoxNW.insert(0, term)
    SearchBoxNW.grid(padx=5, pady=5, row=0, column=0)
    buttonSaveNW = customtkinter.CTkButton(master=frameTopNW, border_width=2, width=50, height=35, text="SAVE", command = saveWord)
    buttonSaveNW.grid(padx=5, pady=5, row=0, column=2)

    termKeys = activeDictionary[term].keys()

    frameArr = []
    frameLabelArr = []
    frameTextBoxArr = []
    count = 0

    for key in termKeys:
        frameArr.append(customtkinter.CTkFrame(master=newWordWindow, corner_radius=10))
        frameArr[count].grid(row=count + 1, column=0,padx=5, pady=5)
        frameLabelArr.append(customtkinter.CTkLabel(master=frameArr[count], text=key))
        frameLabelArr[count].grid(row=0, column=0)
        frameTextBoxArr.append(customtkinter.CTkTextbox(master=frameArr[count], width=338, height=80))
        frameTextBoxArr[count].grid(row=1, column=0, padx=5, pady=5)
        frameTextBoxArr[count].insert("0.0", activeDictionary[term][key])
        count += 1

    def termAddKey():
        newFileWindow = CTkToplevel(app)
        newFileWindow.title("New Key")
        newFileWindow.iconbitmap(directoryString + "FED.ico")
        newFileWindow.geometry("250x39")
        #ImportWindow.resizable(width=False, height=True)  #####Bug Not Fixed with Tkinter

        def getKeyName(e):
            nonlocal count
            newKeyName = textboxRW.get()
            frameArr.append(customtkinter.CTkFrame(master=newWordWindow, corner_radius=10))
            frameArr[count].grid(row=count + 1, column=0,padx=5, pady=5)
            frameLabelArr.append(customtkinter.CTkLabel(master=frameArr[count], text=newKeyName))
            frameLabelArr[count].grid(row=0, column=0)
            frameTextBoxArr.append(customtkinter.CTkTextbox(master=frameArr[count], width=338, height=80))
            frameTextBoxArr[count].grid(row=1, column=0, padx=5, pady=5)
            count += 1
            newFileWindow.destroy()

        textboxRW = customtkinter.CTkEntry(master=newFileWindow, width=240, placeholder_text="Key Name:", placeholder_text_color="#D2D2D2")
        textboxRW.grid(row=0, column=0, padx=5, pady=5)
        textboxRW.bind('<Return>', getKeyName)

    addTermField = customtkinter.CTkButton(master=newWordWindow, width=27, height=27, text="+", font=("arial",16), border_width=2, command=termAddKey)
    addTermField.grid(padx=5, pady=5, row=999, column=0)

def Import(): ### Import Pop Up Window
    ImportWindow = CTkToplevel(app)
    ImportWindow.title("Import")
    ImportWindow.iconbitmap(directoryString + "FED.ico")
    ImportWindow.geometry("560x500")
    ImportWindow.resizable(width=False, height=True)
    frameTopIW = customtkinter.CTkFrame(master=ImportWindow, corner_radius=0)
    frameTopIW.grid(row=0, column=0)
    textDictName = customtkinter.CTkEntry(master=frameTopIW, width=150, height=35, placeholder_text="Dictionary Name:")
    textDictName.grid(padx=5, pady=5, row=0, column=0)
    textRegex = customtkinter.CTkEntry(master=frameTopIW, width=200, height=35, placeholder_text="Field Separation By (Regex):")
    textRegex.grid(padx=5, pady=5, row=0, column=1)

    ImportArrInfo = [' ', ' ', ' ', ' ']

    def addTxt():
        ImportArrInfo[0] = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("text files","*.txt"), ("all files", "*.*")))
        fileName = re.split(r"/|\\", ImportArrInfo[0])[-1]
        fileNameIW.configure(text=fileName)

    buttonFileIW = customtkinter.CTkButton(master=frameTopIW, border_width=2, width=50, height=35, text="File:", command=addTxt)
    buttonFileIW.grid(padx=5, pady=5, row=0, column=2)
    fileNameIW = customtkinter.CTkLabel(master=frameTopIW, text="No File Selected", fg_color=primaryGrey, width=120, height=35, corner_radius=10)
    fileNameIW.grid(padx=5, pady=5, row=0, column=3)

    frameBoxIW = []
    labelIW = []
    textboxIW = []

    indexIW = 0

    frameBoxIW.append(customtkinter.CTkFrame(master=ImportWindow, corner_radius=10))
    frameBoxIW[indexIW].grid(row=indexIW + 1, column=0,padx=5, pady=5)
    labelIW.append(customtkinter.CTkLabel(master=frameBoxIW[indexIW], text="Field {} Name:".format(indexIW)))
    labelIW[indexIW].grid(row=0, column=0)
    textboxIW.append(customtkinter.CTkEntry(master=frameBoxIW[indexIW], width=340, placeholder_text="0th Field is Always \"Term\"", placeholder_text_color="#D2D2D2"))
    textboxIW[indexIW].grid(row=1, column=0, padx=5, pady=5)
    indexIW += 1
    frameBoxIW.append(customtkinter.CTkFrame(master=ImportWindow, corner_radius=10))
    frameBoxIW[indexIW].grid(row=indexIW + 1, column=0,padx=5, pady=5)
    labelIW.append(customtkinter.CTkLabel(master=frameBoxIW[indexIW], text="Field {} Name:".format(indexIW)))
    labelIW[indexIW].grid(row=0, column=0)
    textboxIW.append(customtkinter.CTkEntry(master=frameBoxIW[indexIW], width=340, placeholder_text="Definition", placeholder_text_color="#D2D2D2"))
    textboxIW[indexIW].grid(row=1, column=0, padx=5, pady=5)
    indexIW += 1

    def addDictField():
        nonlocal indexIW

        frameBoxIW.append(customtkinter.CTkFrame(master=ImportWindow, corner_radius=10))
        frameBoxIW[indexIW].grid(row=indexIW + 1, column=0,padx=5, pady=5)
        labelIW.append(customtkinter.CTkLabel(master=frameBoxIW[indexIW], text="Field {} Name:".format(indexIW)))
        labelIW[indexIW].grid(row=0, column=0)
        textboxIW.append(customtkinter.CTkEntry(master=frameBoxIW[indexIW], width=340, placeholder_text="Dicionary Key", placeholder_text_color="#D2D2D2"))
        textboxIW[indexIW].grid(row=1, column=0, padx=5, pady=5)
        indexIW += 1

    buttonAddDictField = customtkinter.CTkButton(master=ImportWindow, width=27, height=27, text="+", font=("arial",16), border_width=2, command = addDictField)
    buttonAddDictField.grid(padx=5, pady=5, row=998, column=0)

    def ImportFunc():
        exec("ImportArrInfo[1] = r\"" + textRegex.get() + "\"")

        fieldArr = []
        for i in range(len(textboxIW)):
            fieldArr.append(textboxIW[i].get())
        ImportArrInfo[2] = fieldArr[1:]

        ImportArrInfo[3] = textDictName.get()

        txt = ImportArrInfo[0] #####txt file directory                      "new.txt"
        parse = ImportArrInfo[1] #####parse via regex                       " \(|\) "
        fields = ImportArrInfo[2] #####word keys in the dictionary          ['POS', 'Definition']
        name = ImportArrInfo[3] #####dictionary name or json file name      "English"

        f = open(txt, 'r', encoding="utf8")
        contents = f.read().split("\n")
        dict = {}

        for i in range(len(contents)):
            tempArr = re.split(parse, contents[i])
            if tempArr[0] in dict:
                for j in range(len(fields)):
                    if j == len(fields) - 1:
                        dict[tempArr[0]][fields[j]] += " " + " ".join(tempArr[j+1:])
                    else:
                        dict[tempArr[0]][fields[j]] += " " + tempArr[j+1]
            else:
                dict[tempArr[0]] = {}
                for j in range(len(fields)):
                    if j == len(fields) - 1:
                        dict[tempArr[0]][fields[j]] = " ".join(tempArr[j+1:])
                    else:
                        dict[tempArr[0]][fields[j]] = tempArr[j+1]

        with codecs.open(directoryString + "Templates\\" + name + ".txt", "w") as fp:
            for item in fields:
                fp.write("%s\n" % item)
        with codecs.open(directoryString + "Dictionaries\\" + name + ".json", "w", encoding='utf-8') as outfile:
            json.dump(dict, outfile, ensure_ascii=False)


        ImportWindow.destroy()

    buttonImportIW = customtkinter.CTkButton(master=ImportWindow, width=100, height=40, text="IMPORT", font=("arial",14), border_width=2, command=ImportFunc)
    buttonImportIW.grid(padx=20, pady=20, row=999, column = 0)

def Export(): ### Export Pop Up Window
    ExportWindow = CTkToplevel(app)
    ExportWindow.title("Export")
    ExportWindow.iconbitmap(directoryString + "FED.ico")
    ExportWindow.geometry("430x500")
    ExportWindow.resizable(width=False, height=True)

    termIntVar = IntVar()
    
    choiceFrame = customtkinter.CTkFrame(master=ExportWindow, corner_radius=10)
    choiceFrame.grid(row=1, column=0)
    fileExportFrontFrame = customtkinter.CTkFrame(master=choiceFrame)
    fileExportFrontFrame.grid(padx=5, pady=5, row=1, column=1)
    fileExportBackFrame = customtkinter.CTkFrame(master=choiceFrame)
    fileExportBackFrame.grid(padx=5, pady=5, row=1, column=2)
    fileExportFrontText = customtkinter.CTkLabel(master=fileExportFrontFrame, text="FRONT", width=120, height=25, corner_radius=10)
    fileExportFrontText.grid(padx=5, pady=5, row=0, column=0)
    fileExportBackText = customtkinter.CTkLabel(master=fileExportBackFrame, text="BACK", width=120, height=25, corner_radius=10)
    fileExportBackText.grid(padx=5, pady=5, row=0, column=0)

    frameTerm = customtkinter.CTkFrame(master=choiceFrame)
    frameTerm.grid(padx=5, pady=5, row=2, column=0)
    labelTerm = customtkinter.CTkLabel(master=frameTerm, text="Term", width=120, height=25, corner_radius=10)
    labelTerm.grid(padx=5, pady=5, row=0, column=0)

    termFront = customtkinter.CTkRadioButton(master=choiceFrame, variable=termIntVar, width = 30, value = 1, text="")
    termBack = customtkinter.CTkRadioButton(master=choiceFrame, variable=termIntVar, width = 30, value = 2, text="")
    termFront.grid(padx=5, pady=5, row=2, column=1)
    termBack.grid(padx=5, pady=5, row=2, column=2)

    choiceArr = []
    uniqueKeys = []
    uniqueKeysFrameArr = []
    uniqueKeysFrontButtonArr = []
    uniqueKeysBackButtonArr = []
    exportDict = ""
    currentFileName = ""

    def frontORback(file):
        nonlocal currentFileName
        currentFileName = file

        choiceArr.clear()
        uniqueKeys.clear()

        for i in range(len(uniqueKeysFrameArr)):
            uniqueKeysFrameArr[i].destroy()
            uniqueKeysFrontButtonArr[i].destroy()
            uniqueKeysBackButtonArr[i].destroy()

        uniqueKeysFrameArr.clear()
        uniqueKeysFrontButtonArr.clear()
        uniqueKeysBackButtonArr.clear()

        f = open(directoryString + "Files\\" + file + ".json", encoding='utf-8')
        nonlocal exportDict
        exportDict = json.load(f)
        for term in exportDict:
            for key in list(exportDict[term].keys()):
                if key not in uniqueKeys:
                    uniqueKeys.append(key)

        count = 0
        for key in uniqueKeys:
            uniqueKeysFrameArr.append(customtkinter.CTkFrame(master=choiceFrame))
            uniqueKeysFrameArr[count].grid(padx=5, pady=5, row=count+3, column=0)
            keyLabel = customtkinter.CTkLabel(master=uniqueKeysFrameArr[count], text=key, width=120, height=25, corner_radius=10)
            keyLabel.grid(padx=5, pady=5, row=0, column=0)

            choiceArr.append(IntVar())

            uniqueKeysFrontButtonArr.append(customtkinter.CTkRadioButton(master=choiceFrame, variable=choiceArr[count], width = 30, value = 1, text=""))
            uniqueKeysBackButtonArr.append(customtkinter.CTkRadioButton(master=choiceFrame, variable=choiceArr[count], width = 30, value = 2, text=""))
            uniqueKeysFrontButtonArr[count].grid(padx=5, pady=5, row=count+3, column=1)
            uniqueKeysBackButtonArr[count].grid(padx=5, pady=5, row=count+3, column=2)
            count += 1

    fileList = os.listdir(directoryString + "Files")
    for i in range(len(fileList)):
        fileList[i] = fileList[i].replace(".json", "")

    frameTopEW = customtkinter.CTkFrame(master=ExportWindow, corner_radius=0)
    frameTopEW.grid(row=0, column=0)
    fileComboBox = customtkinter.CTkComboBox(master=frameTopEW, values=fileList, width=205, height=35, command=frontORback)
    fileComboBox.grid(padx=5, pady=5, row=0, column=0)
    fileComboBox.set("Choose File:")
    separationStringEntry = customtkinter.CTkEntry(master=frameTopEW, placeholder_text="Separated By:", width=205, height=35)
    separationStringEntry.grid(padx=5, pady=5, row=0, column=1)

    def exportTXT():
        with open(directoryString + "Exports\\" + currentFileName + ".txt", 'w', encoding='utf-8') as f:

            choiceIntArr=[]
            firstString=""
            secondString=""
            separationString=separationStringEntry.get()

            for intvar in choiceArr:
                choiceIntArr.append(intvar.get())

            for term in exportDict:
                for i in range(len(choiceArr)):
                    if choiceIntArr[i] == 1:
                        if uniqueKeys[i] in exportDict[term]:
                            firstString += " " + exportDict[term][uniqueKeys[i]]
                    elif choiceIntArr[i] == 2:
                        if uniqueKeys[i] in exportDict[term]:
                            secondString += " " + exportDict[term][uniqueKeys[i]]
                            

                if termIntVar.get() == 1:
                    firstString = term + firstString
                elif termIntVar.get() == 2:
                    secondString = term + secondString
                    
                completeString = firstString + separationString + secondString

                f.write(completeString)
                f.write('\n')

                firstString=""
                secondString=""

        ExportWindow.destroy()

    buttonExportEW = customtkinter.CTkButton(master=ExportWindow, width=100, height=40, text="EXPORT", font=("arial",14), border_width=2, command=exportTXT)
    buttonExportEW.grid(padx=20, pady=20, row=999, columnspan=3, column = 0)

def delFrameContents(frame): ### General Command for delete widgets in a frame
    for widgets in frame.winfo_children():
        widgets.destroy()

def search(e): ### Search current active dictionary on key release of the search box
    delFrameContents(bFR2)
    count = 0
    typed = SearchBox.get()
    for term in activeDictionary:
        if count >= dictionaryEntryLimit:
            break
        if term.lower().startswith(typed.lower()):
            termButton = customtkinter.CTkButton(master=bFR2, text=term, width = 280, height = 25, anchor='w', command=lambda m=str(term): editWord(m))
            termButton.grid(row = count, column = 0, pady=2, padx=2)
            termButton.bind('<Button-3>', lambda event, word=str(term): mWordClick(word, event))
            count += 1

def setActiveDict(name): ### Sets the active dictionary, active dictionary name, and directory to Dictionaries
    f = open(directoryString + "Dictionaries\\" + name + ".json", encoding='utf-8')
    global activeDictionary
    global activeDictionaryName
    global activeDirectory
    activeDirectory = "Dictionaries"
    activeDictionary = json.load(f)
    activeDictionaryName = name
    search(e = None)

def setActiveFile(name): ### Sets the active files, active file name, and directory to Files
    f = open(directoryString + "Files\\" + name + ".json", encoding='utf-8')
    global activeDictionary
    global activeDictionaryName
    global activeDirectory
    activeDirectory = "Files"
    activeDictionary = json.load(f)
    activeDictionaryName = name
    search(e = None)

def ForD(value): ### Shows either the list of dictionaries or files for the compound button in the left frame
    if value == "Dictionaries":
        showDictionaries()
    elif value == "Files":
        showFiles()

def showDictionaries(): ### Creates radio buttons for the list of dictionaries
    delFrameContents(bFL2)
    dictList = os.listdir(directoryString + "Dictionaries")
    for i in range(len(dictList)):
        dictList[i] = dictList[i].replace(".json", "")
    dictArr = []
    r = IntVar()
    for i in range(len(dictList)):
        dictArr.append(customtkinter.CTkRadioButton(master=bFL2, variable=r, value = i + 1, text=dictList[i], command=lambda m=str(dictList[i]): setActiveDict(m)))
        dictArr[i].grid(row = i, column = 0, pady=10, padx=10)
        dictArr[i].bind('<Button-3>', lambda event, word=str(dictList[i]): mDictClick(word, event))

def showFiles(): ### Creates radio buttons for the list of Files
    delFrameContents(bFL2)
    fileList = os.listdir(directoryString + "Files")
    for i in range(len(fileList)):
        fileList[i] = fileList[i].replace(".json", "")
    fileArr = []
    r = IntVar()
    for i in range(len(fileList)):
        fileArr.append(customtkinter.CTkRadioButton(master=bFL2, variable=r, value = i + 1, text=fileList[i], command=lambda m=str(fileList[i]): setActiveFile(m)))
        fileArr[i].grid(row = i, column = 0, pady=10, padx=10)
        fileArr[i].bind('<Button-3>', lambda event, word=str(fileList[i]): mFileClick(word, event))

    def newFile():
        newFileWindow = CTkToplevel(app)
        newFileWindow.title("New File")
        newFileWindow.iconbitmap(directoryString + "FED.ico")
        newFileWindow.geometry("250x39")
        newFileWindow.resizable(width=False, height=False)

        def getName(e):
            newName = textboxRW.get()
            with codecs.open(directoryString + "Files\\" + newName + ".json", "w", encoding='utf-8') as outfile:
                json.dump({}, outfile, ensure_ascii=False)
            newFileWindow.destroy()
            showFiles()

        textboxRW = customtkinter.CTkEntry(master=newFileWindow, width=240, placeholder_text="File Name:", placeholder_text_color="#D2D2D2")
        textboxRW.grid(row=0, column=0, padx=5, pady=5)
        textboxRW.bind('<Return>', getName)

    buttonAddFile = customtkinter.CTkButton(master=bFL2, width=100, text="New File", font=("arial",14), border_width=2, command=newFile)
    buttonAddFile.grid(padx=0, pady=10, row=999, column=0)

def RenameDict(dictName): ### Renames Selected Dictionary
    RenameWindow = CTkToplevel(app)
    RenameWindow.title("Name")
    RenameWindow.iconbitmap(directoryString + "FED.ico")
    RenameWindow.geometry("250x39")
    RenameWindow.resizable(width=False, height=False)
    
    tempDS = directoryString

    def renameD(e):
        newName = textboxRW.get()
        os.rename(tempDS + "Dictionaries\\" + dictName + ".json", tempDS + "Dictionaries\\" + newName + ".json")
        RenameWindow.destroy()
        showDictionaries()

    textboxRW = customtkinter.CTkEntry(master=RenameWindow, width=240, placeholder_text="New Name:", placeholder_text_color="#D2D2D2")
    textboxRW.grid(row=0, column=0, padx=5, pady=5)
    textboxRW.bind('<Return>', renameD)

def DeleteDict(dictName): ### Deletes Selected Dictionary
    os.remove(directoryString + "Dictionaries\\" + dictName + ".json")
    showDictionaries()

def RenameFile(fileName): ### Renames Selected File
    RenameWindow = CTkToplevel(app)
    RenameWindow.title("Name")
    RenameWindow.iconbitmap(directoryString + "FED.ico")
    RenameWindow.geometry("250x39")
    RenameWindow.resizable(width=False, height=False)

    tempDS = directoryString

    def renameF(e):
        newName = textboxRW.get()
        os.rename(tempDS + "Files\\" + fileName + ".json", tempDS + "Files\\" + newName + ".json")
        RenameWindow.destroy()
        showFiles()

    textboxRW = customtkinter.CTkEntry(master=RenameWindow, width=240, placeholder_text="New Name:", placeholder_text_color="#D2D2D2")
    textboxRW.grid(row=0, column=0, padx=5, pady=5)
    textboxRW.bind('<Return>', renameF)

def DeleteFile(fileName): ### Deletes Selected File
    os.remove(directoryString + "Files\\" + fileName + ".json")
    showFiles()

def DeleteWord(word): ### Deletes Selected Word
    activeDictionary.pop(word, None)
    saveActiveDictionary(activeDirectory + "\\")
    event = None
    search(event)

def addNewTerm(): ### Add a new term for the current active dictionary
    if activeDirectory == "Files":
        return

    newWordWindow = CTkToplevel(app)
    newWordWindow.title("Word Editor")
    newWordWindow.iconbitmap(directoryString + "FED.ico")
    newWordWindow.geometry("360x500")
    newWordWindow.resizable(width=False, height=True)

    def saveWord():
        savedTerm = {}
        for i in range(len(frameArr)):
            savedTerm[frameLabelArr[i].cget("text")] = frameTextBoxArr[i].get("0.0", "end")
        activeDictionary[SearchBoxNW.get()] = savedTerm
        saveActiveDictionary("Dictionaries\\")
        newWordWindow.destroy()

    frameTopNW = customtkinter.CTkFrame(master=newWordWindow, width=780, height=40, corner_radius=0)
    frameTopNW.grid(row=0, column=0)
    SearchBoxNW = customtkinter.CTkEntry(master=frameTopNW, width=288, height=35)
    SearchBoxNW.grid(padx=5, pady=5, row=0, column=0)
    buttonSaveNW = customtkinter.CTkButton(master=frameTopNW, border_width=2, width=50, height=35, text="SAVE", command=saveWord)
    buttonSaveNW.grid(padx=5, pady=5, row=0, column=2)

    frameArr = []
    frameLabelArr = []
    frameTextBoxArr = []
    count = 0

    with open(directoryString + "Templates\\" + activeDictionaryName + ".txt", encoding='utf-8') as fp:
        for line in fp:
            key = line[:-1]
            frameArr.append(customtkinter.CTkFrame(master=newWordWindow, corner_radius=10))
            frameArr[count].grid(row=count + 1, column=0,padx=5, pady=5)
            frameLabelArr.append(customtkinter.CTkLabel(master=frameArr[count], text=key))
            frameLabelArr[count].grid(row=0, column=0)
            frameTextBoxArr.append(customtkinter.CTkTextbox(master=frameArr[count], width=338, height=80))
            frameTextBoxArr[count].grid(row=1, column=0, padx=5, pady=5)
            count += 1

    def termAddKey():
        newFileWindow = CTkToplevel(app)
        newFileWindow.title("New Key")
        newFileWindow.iconbitmap(directoryString + "FED.ico")
        newFileWindow.geometry("250x39")
        #ImportWindow.resizable(width=False, height=True)  #####Bug Not Fixed with Tkinter

        def getKeyName(e):
            nonlocal count
            newKeyName = textboxRW.get()
            frameArr.append(customtkinter.CTkFrame(master=newWordWindow, corner_radius=10))
            frameArr[count].grid(row=count + 1, column=0,padx=5, pady=5)
            frameLabelArr.append(customtkinter.CTkLabel(master=frameArr[count], text=newKeyName))
            frameLabelArr[count].grid(row=0, column=0)
            frameTextBoxArr.append(customtkinter.CTkTextbox(master=frameArr[count], width=338, height=80))
            frameTextBoxArr[count].grid(row=1, column=0, padx=5, pady=5)
            count += 1
            newFileWindow.destroy()

        textboxRW = customtkinter.CTkEntry(master=newFileWindow, width=240, placeholder_text="Key Name:", placeholder_text_color="#D2D2D2")
        textboxRW.grid(row=0, column=0, padx=5, pady=5)
        textboxRW.bind('<Return>', getKeyName)

    addTermField = customtkinter.CTkButton(master=newWordWindow, width=27, height=27, text="+", font=("arial",16), border_width=2, command=termAddKey)
    addTermField.grid(padx=5, pady=5, row=999, column=0)

def addWordToFile(file, word): ### Move a dicitonary term to a file
    f = open(directoryString + "Files\\" + file + ".json", encoding='utf-8')
    editedDictionary = json.load(f)
    editedDictionary[word] = activeDictionary[word]
    with codecs.open(directoryString + "Files\\" + file + ".json", "w", encoding='utf-8') as outfile:
            json.dump(editedDictionary, outfile, ensure_ascii=False)

###============================================Pop Up Menus============================================###
def mDictClick(word, event = None): ### Dictionary Pop Up Menu
    mDict = Menu(bFL2, tearoff = 0)
    mDict.add_command(label ="Rename", command = lambda: RenameDict(word))
    mDict.add_separator()
    mDict.add_command(label ="Delete", command = lambda: DeleteDict(word))

    try:
        mDict.tk_popup(event.x_root, event.y_root)
    finally:
        mDict.grab_release()

def mFileClick(word, event = None): ### File Pop Up Menu
    mFile = Menu(bFL2, tearoff = 0)
    mFile.add_command(label ="Rename", command = lambda: RenameFile(word))
    mFile.add_separator()
    mFile.add_command(label ="Delete", command = lambda: DeleteFile(word))

    try:
        mFile.tk_popup(event.x_root, event.y_root)
    finally:
        mFile.grab_release()

def mWordClick(word, event = None): ### Word Pop Up Menu
    mWord = Menu(bFR2, tearoff = 0)

    mWordAdd = Menu(mWord, tearoff = 0)
    mWord.add_cascade(menu=mWordAdd, label='Add To')

    fileList = os.listdir(directoryString + "Files")
    for i in range(len(fileList)):
        fileList[i] = fileList[i].replace(".json", "")
    for i in fileList:
        mWordAdd.add_command(label=i, command = lambda file=str(i): addWordToFile(file, word))

    mWord.add_command(label="Edit", command = lambda: editWord(word))
    mWord.add_separator()
    mWord.add_command(label="Delete", command = lambda: DeleteWord(word))

    try:
        mWord.tk_popup(event.x_root, event.y_root)
    finally:
        mWord.grab_release()

#####============================================Body============================================#####

###============================================Top Frame============================================###
frameTop = customtkinter.CTkFrame(master=app, corner_radius=0)
frameTop.grid(row=0, column=0, columnspan=2)

buttonImport = customtkinter.CTkButton(master=frameTop, border_width=2, width=60, height=35, text="IMPORT", command=Import)
buttonImport.grid(padx=5, pady=5, row=0, column=0)
buttonExport = customtkinter.CTkButton(master=frameTop, border_width=2, width=60, height=35, text="EXPORT", command=Export)
buttonExport.grid(padx=5, pady=5, row=0, column=1)
SearchBox = customtkinter.CTkEntry(master=frameTop, width=352, height=35, placeholder_text="Search")
SearchBox.grid(padx=5, pady=5, row=0, column=2)
SearchBox.bind("<KeyRelease>", search)
buttonAdd = customtkinter.CTkButton(master=frameTop, width=34, height=27, text="+", font=("arial",24), border_width=2, command=addNewTerm)
buttonAdd.grid(padx=5, pady=5, row=0, column=3)

###============================================Left Frame============================================###
frameLeft = customtkinter.CTkFrame(master=app, corner_radius=10)
frameLeft.grid(padx=10, pady=10, row=1, column=0)

segemented_button = customtkinter.CTkSegmentedButton(master=frameLeft, values=["Dictionaries", "Files"], command=ForD)
segemented_button.grid(padx=5, pady=5, row=0, column=0)
buttonFrameL = customtkinter.CTkFrame(master=frameLeft, width=190, height=400, corner_radius = 10)
buttonFrameL.grid(padx=5, pady=5, row=1, column=0)
bFLCanvas = Canvas(buttonFrameL, width=170, height=405, bg=primaryGrey, bd=0, highlightthickness=0)
bFLCanvas.pack(side=LEFT, fill=BOTH, expand=1)
scrollbarLeft = customtkinter.CTkScrollbar(buttonFrameL, orientation="vertical", button_color=primaryGrey , button_hover_color=secondaryGrey, command=bFLCanvas.yview)
scrollbarLeft.pack(side=RIGHT, fill=Y)
bFLCanvas.configure(yscrollcommand=scrollbarLeft.set)
bFLCanvas.bind('<Configure>', lambda e: bFLCanvas.configure(scrollregion = bFLCanvas.bbox("all")))
bFL2 = customtkinter.CTkFrame(bFLCanvas, fg_color=primaryGrey)
bFLCanvas.create_window((0,0), window=bFL2, anchor="nw")

#============================================Left Frame Set Up Buttons============================================#
for i in range(dictionaryEntryLimit):
    startUpButton = Button(master=bFL2, text='', width = 20, bg=primaryGrey, activebackground=primaryGrey, fg=primaryGrey, bd=0, font=("arial",10), activeforeground=primaryGrey)
    startUpButton.grid(row = i, column = 0, pady=2, padx=2)

###============================================Right Frame============================================###
frameRight = customtkinter.CTkFrame(master=app, corner_radius=10)
frameRight.grid(padx=10, pady=10, row=1, column=1)

buttonFrameR = customtkinter.CTkFrame(master=frameRight, width=260, height=400, corner_radius = 10)
buttonFrameR.grid(padx=5, pady=5, row=1, column=0)
bFRCanvas = Canvas(buttonFrameR, width=285, height=445, bg=primaryGrey, bd=0, highlightthickness=0)
bFRCanvas.pack(side=LEFT, fill=BOTH, expand=1)
scrollbarRight = customtkinter.CTkScrollbar(buttonFrameR, orientation="vertical", button_color=primaryGrey , button_hover_color=secondaryGrey, command=bFRCanvas.yview)
scrollbarRight.pack(side=RIGHT, fill=Y)
bFRCanvas.configure(yscrollcommand=scrollbarRight.set)
bFRCanvas.bind('<Configure>', lambda e: bFRCanvas.configure(scrollregion = bFRCanvas.bbox("all")))
bFR2 = customtkinter.CTkFrame(bFRCanvas, fg_color=primaryGrey)
bFRCanvas.create_window((0,0), window=bFR2, anchor="nw")

#============================================Right Frame Set Up Buttons============================================#
for i in range(dictionaryEntryLimit):
    startUpButton = customtkinter.CTkButton(master=bFR2, width = 280, text = "", height = 25, fg_color = primaryGrey, hover_color=primaryGrey)
    startUpButton.grid(row = i, column = 0, pady=2, padx=2)

app.mainloop()

#######============================================LOL666============================================#######