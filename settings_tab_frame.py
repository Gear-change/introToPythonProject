import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox


def load_from_file(*args):
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    readFile = askopenfile(mode='r', filetypes=[('Text Document', '*.txt'), ('All Files', "*.*")])
    if readFile is not None:
        #this if clause is in case there is no info in the file selected or no file there
        #first lets clear the existing files
        userWork = []
        userEducation = []
        userSkills = []
        userProjects = []
        listStringFromFile = []
        for x in readFile:
            listStringFromFile.append(x)
        readFile.close()
        firstName.set(listStringFromFile[0])
        middleInitial.set(listStringFromFile[2])
        lastName.set(listStringFromFile[4])
        userLinkedin.set(listStringFromFile[6])
        userGithub.set(listStringFromFile[8])
        userPhone.set(listStringFromFile[10])
        userEmail.set(listStringFromFile[12])
        #from this point onward we need to adjust to what is in the file
        lineNo = 14
        newinput = listStringFromFile[lineNo]
        keysofInput = newinput.keys()
        if 'degreeType' in keysofInput:
            #we know we have a education list now as an input
            newDegree = newinput
            while newDegree != -1:
                userEducation.append(newDegree)
                lineNo += 1
                newDegree = listStringFromFile[lineNo]
            lineNo += 1
            newinput = listStringFromFile(lineNo)
        if 'companyName' in keysofInput:
            #now we know we have a work list as an input
            newWork = newinput
            while newWork != -1:
                userWork.append(newWork)
                lineno += 1
                newWork = listStringFromFile[lineNo]
            lineNo += 1
            newinput = listStringFromFile(lineNo)
        if 'skillName' in keysofInput:
            #now we know we have a skill list as an input
            newSkill = newinput
            while newSkill != -1:
                userSkills.append(newSkill)
                lineNo += 1
                newSkill = listStringFromFile[lineNo]
            lineNo += 1
            newinput = listStringFromFile[lineNo]
        if 'projectName' in keysofInput:
            #now we know we have a project/other list as input
            newProject = newinput
            while newProject != -1:
                userProjects.append(newProject)
                lineNo += 1
                newSkill = listStringFromFile[lineNo]
        #we should be done now            
    else:
        messagebox.showerror(title="there is nothing here", message="try a different file?")
    

def format_string_out(items):
    return '\n-1\n'.join(items)

def save_to_file(*args):
    
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args

  
    personal_info = [firstName.get(), middleInitial.get(), lastName.get(), 
                     userLinkedin.get(), userGithub.get(), userPhone.get(),
                     userEmail.get()]
    string_to_save = format_string_out(personal_info)

   
    for user_data in [userEducation, userWork, userSkills, userProjects]:
        if len(user_data) > 0:
            user_data_str = '\n'.join([str(d) for d in user_data])
            string_to_save += '\n-1\n' + user_data_str

    
    with asksaveasfile(filetypes=[('Text Document', '*.txt'), ('All Files', "*.*")], defaultextension='.txt') as file:
        if file:
            file.write(string_to_save)
    file.write("\n-1")
    file.close()


def make_settings_tab(parent, *args):
    new_frame = tk.Frame(parent)
    curcol = 0
    curRow = 0
    new_label = tk.Label(new_frame, text="use the button here to save the current inputs to a file: ")
    new_label.grid(column=curcol,row=curRow)
    curcol += 1
    save_button = tk.Button(new_frame, text="Save As", command=lambda: save_to_file(*args))
    save_button.grid(column=curcol,row=curRow)
    curRow += 1
    curcol = 0
    new_label = tk.Label(new_frame, text="use the button here to load prior inputs from a previous file: ")
    new_label.grid(column=curcol,row=curRow)
    curcol += 1
    load_button = tk.Button(new_frame, text="open file", command=lambda: load_from_file(*args))
    load_button.grid(column=curcol,row=curRow)
    curRow += 1
    curcol = 0
    new_label = tk.Label(new_frame, text=" use this Button to proceed toward printing a resume: ")
    new_label.grid(column=curcol,row=curRow)
    curcol += 1
    to_relevency_button = tk.Button(new_frame, text="to relevancy input", command=openRelevencyFrame(*args))
    to_relevency_button.grid(column=curcol,row=curRow)
    return new_frame


