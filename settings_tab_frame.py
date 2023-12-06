import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox
import json
from workTabFrame import WorkFrame, addWorkToList, make_list_from_text_2, make_list_from_text
from skilltabframe2 import skillFrame, addNewSkill
from ProjectTabFrame import addNewProject, makeOtherTab
from relevencyFrame import *
from EducationTabFrame import *

def replaceQual3(editWindow, thisQual, projectName, hasEvent, eventName, monthEvent, yearEvent, projectDetailsList, *args):
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    removeQual(thisQual, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects)
    addNewProject(projectName, hasEvent, eventName, monthEvent, yearEvent, projectDetailsList)
    editWindow.destroy()
    getListOfObjects(*args)

def replaceQual2(editWindow, thisQual, skillName, skillYear, *args):
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    removeQual(thisQual, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects)
    addNewSkill(skillName, skillYear)
    getListOfObjects(*args)    
    editWindow.destroy()

def replaceQual1(editWindow, thisQual, DegreeType, DegreeField, degreeMinor, schoolName, schoolCity, schoolState, SchoolDateEndMonth, SchoolDateEndYear, GPA, degreeDetails, *args):
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    removeQual(thisQual, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects)
    addNewDegree(DegreeType, DegreeField, degreeMinor, schoolName, schoolCity, schoolState, SchoolDateEndMonth, SchoolDateEndYear, GPA, degreeDetails)
    editWindow.destroy()
    getListOfObjects(*args)

def replaceQual(editWindow, thisQual, companyName, companyCity, companyState, OccupationTitlelist, occupationDetailsList, startYear, startMonth, endYear, endMonth, *args):
    global userWork
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    removeQual(thisQual, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects)
    addWorkToList(userWork, companyName, companyCity, companyState, OccupationTitlelist, occupationDetailsList, startYear, startMonth, endYear, endMonth)
    editWindow.destroy()
    getListOfObjects(*args)

def makeEditWindow(thisQual, thingEditing, intItems, args):
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    editWindow = tk.Tk()
    
    match(intItems):
        case 1:
            #this is a work frame we need
            thisFrame = WorkFrame(editWindow, userWork)
            textFromTitles = str()
            listDetails = list()
            listtitles = list()
            textFromDetails = str()
            for title in thingEditing.get("OccupationTitle"):
                listtitles.append(title.get("OccupationTitle"))
            textFromTitles = "\n".join(listtitles)      
            for detail in thingEditing.get("occupationDetails"):
                listDetails.append(detail.get("OccupationDetail"))
            textFromDetails = "\n".join(listDetails)
            thisFrame.setvar("companyName", thingEditing.get("companyName"))
            thisFrame.setvar("companyCity", thingEditing.get("companyCity"))
            thisFrame.setvar("companyState", thingEditing.get("companyState"))
            thisFrame.setvar("occupationTitle", textFromTitles)
            thisFrame.setvar("occupationDetailsText", textFromDetails)
            thisFrame.setvar("oDateStartYear", thingEditing.get("dateEndYear"))
            thisFrame.setvar("oDateStartMonth", thingEditing.get("dateEndMonth"))
            thisFrame.setvar("oDateEndYear", thingEditing.get("dateStartYear"))
            thisFrame.setvar("oDateEndMonth", thingEditing.get("dateStartMonth"))
            thisFrame.children["occupationDetailsText"].insert(
                tk.INSERT,
                textFromDetails
            )
            thisFrame.children["occupationTitle"].insert(
                tk.INSERT,
                textFromTitles
            )
            thisFrame.children["btnSubmit"].configure(
                command=lambda:replaceQual(
                    editWindow,
                    thisQual,
                    editWindow.children["worFrame"].getvar("companyName"),
                    editWindow.children["worFrame"].getvar("companyCity"),
                    editWindow.children["worFrame"].getvar("companyState"),
                    make_list_from_text_2(editWindow.children["worFrame"].children["occupationTitle"], "OccupationTitle"),
                    make_list_from_text(editWindow.children["worFrame"].children["occupationDetailsText"], "OccupationDetail"),
                    editWindow.children["worFrame"].getvar("oDateStartYear"),
                    editWindow.children["worFrame"].getvar("oDateStartMonth"),
                    editWindow.children["worFrame"].getvar("oDateEndYear"),
                    editWindow.children["worFrame"].getvar("oDateEndMonth"),
                    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects
                )
            )
            thisFrame.pack()
        case 2:
            #we need a education frame
            thisFrame = makeEducationTabFrame(editWindow,userEducation)
            textListDetails = list()
            for detail in thingEditing["degreeDetails"]:
                textListDetails.append(detail.get("degreeDetail"))
            textListDetails = "\n".join(textListDetails)
            thisFrame.setvar("DegreeType", thingEditing.get("degreeType"))
            thisFrame.setvar("DegreeField", thingEditing.get("degreeField"))
            thisFrame.setvar("degreeMinor", thingEditing.get("degreeMinor"))
            thisFrame.setvar("schoolName", thingEditing.get("schoolName"))
            thisFrame.setvar("schoolCity", thingEditing.get("schoolCity"))
            thisFrame.setvar("schoolState", thingEditing.get("schoolState"))
            thisFrame.setvar("SchoolDateEndMonth", thingEditing.get("dateEndMonth"))
            thisFrame.setvar("SchoolDateEndYear", thingEditing.get("dateEndYear"))
            thisFrame.setvar("GPA", thingEditing.get("gradeGPA"))
            thisFrame.children["degreeDetails"].insert(
                tk.INSERT,
                textListDetails
            )
            thisFrame.children["btnSubmit"].configure(
                command=lambda:replaceQual1(
                    editWindow,
                    thisQual,
                    editWindow.children["eduFrame"].getvar("DegreeType"), 
                    editWindow.children["eduFrame"].getvar("DegreeField"),
                    editWindow.children["eduFrame"].getvar("degreeMinor"),
                    editWindow.children["eduFrame"].getvar("schoolName"), 
                    editWindow.children["eduFrame"].getvar("schoolCity"),  
                    editWindow.children["eduFrame"].getvar("schoolState"),  
                    editWindow.children["eduFrame"].getvar("SchoolDateEndMonth"), 
                    editWindow.children["eduFrame"].getvar("SchoolDateEndYear"), 
                    editWindow.children["eduFrame"].getvar("GPA"), 
                    make_list_from_text(editWindow.children["eduFrame"].children["degreeDetails"], "degreeDetail"),
                    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects
                )
            )
            thisFrame.pack()

            

        case 3:
            #we need a skill frame
            thisFrame = skillFrame(editWindow, userSkills)
            thisFrame.setvar("skillName", thingEditing.get("skillName"))
            thisFrame.setvar("skillYear", thingEditing.get("skillYears"))
            
            thisFrame.children["btnSubmit"].configure(
                command=lambda:replaceQual2(
                    editWindow,
                    thisQual,
                    editWindow.children["sklFrame"].getvar("skillName"), 
                    editWindow.children["sklFrame"].getvar("skillYear"),
                    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects
                )
            )
            thisFrame.pack()
            

        case 4:
            #we need a project frame
            thisFrame = makeOtherTab(editWindow, userProjects)
            listDetails2 = list()
            for part in thingEditing["projectDetails"]:
                listDetails2.append(part.get("projectDetail"))
            textListDetails = "\n".join(listDetails2)
            thisFrame.setvar("projectName", thingEditing.get("projectName"))
            thisFrame.setvar("hasEvent", thingEditing.get("hasEvent"))
            thisFrame.setvar("eventName", thingEditing.get("eventName"))
            thisFrame.setvar("monthEvent", thingEditing.get("month"))
            thisFrame.setvar("yearEvent", thingEditing.get("year"))
            thisFrame.children["projectDetailsText"].insert(
                tk.INSERT,
                textListDetails
            )
            thisFrame.children["btnSubmit"].configure(
                command=lambda:replaceQual3(
                    editWindow,
                    thisQual,
                    editWindow.children["otrFrame"].getvar("projectName"),
                    editWindow.children["otrFrame"].getvar("hasEvent"),
                    editWindow.children["otrFrame"].getvar("eventName"),
                    editWindow.children["otrFrame"].getvar("monthEvent"),
                    editWindow.children["otrFrame"].getvar("yearEvent"),
                    make_list_from_text(
                        editWindow.children["otrFrame"].children["projectDetailsText"], 
                        "projectDetail"
                    ),
                    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects
                )
            )
            thisFrame.pack()

        case _:
            #error no case passed/no case number in range
            print("error at settings_tab_frame in makeEditWindow, number did not get passed - blame justin")
    editWindow.mainloop()
        
def editQualification(ItemToEdit, *args):
    global firstName
    global middleInitial
    global lastName 
    global userLinkedin
    global userGithub
    global userPhone
    global userEmail
    global userWork
    global userEducation
    global userSkills
    global userProjects
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    global itemList
    thisQual = None
    for ttuple in itemList:
        item1, item2 = ttuple
        if ItemToEdit == item1:
            thisQual = ttuple
            break
    if len(thisQual) == 0:
        print("qualification not found")
        pass
    item1, item2 = thisQual
    if len(userWork) != 0:
        if item2 in userWork[0].keys():
            tempInt = 0
            workEditing = dict
            for work in userWork:
                if work["companyName"] == ItemToEdit:
                    workEditing = work
                    break
                tempInt += 1
            if len(workEditing) != 0:
                makeEditWindow(thisQual, workEditing, 1, args)
    if len(userEducation) != 0:
        if item2 in userEducation[0].keys():
            tempInt = 0
            degreeEditing = dict
            for degree in userEducation:
                if degree["degreeField"] == ItemToEdit:
                    degreeEditing = degree
                    break
                tempInt += 1
            if len(degreeEditing) != 0:
                makeEditWindow(thisQual, degreeEditing, 2, args)
    if len(userSkills) != 0:
        if item2 in userSkills[0].keys():
            tempInt = 0
            skillEditing = dict()
            for skills in userSkills:
                if skills["skillName"] == ItemToEdit:
                    skillEditing = skills
                    break
                tempInt += 1
            if len(skillEditing) != 0:
                makeEditWindow(thisQual, skillEditing, 3, args)

    if len(userProjects) != 0:
        if item2 in userProjects[0].keys():
            tempInt = 0
            projectEditing = dict()
            for project in userProjects:
                if project["projectName"] == ItemToEdit:
                    projectEditing = project
                    break
                tempInt += 1
            if len(projectEditing) != 0:
                makeEditWindow(thisQual, projectEditing, 4, args)
    args = firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects
    itemList = getListOfObjects(*args)

def create_combo_set2(parent, label_text, input, list_of_tuples, altname):
    list_of_values = list()
    for ttuple in list_of_tuples:
        item1, item2 = ttuple
        list_of_values.append(item1)
    return ttk.Combobox(parent, textvariable=input, values=list_of_values, name=altname), tk.Label(parent, text=label_text)

def removeQual(qualToDelete, *args):
    global itemList
    global firstName
    global middleInitial
    global lastName 
    global userLinkedin
    global userGithub
    global userPhone
    global userEmail
    global userWork
    global userEducation
    global userSkills
    global userProjects
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    itemList = getListOfObjects(firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects)
    global thisQual
    thisQual = tuple()
    for ttuple in itemList:
        item1, item2 = ttuple
        if qualToDelete == item1:
            thisQual = ttuple
            break
    
    try:
        item1, item2 = thisQual
    except ValueError:
        item1, item2 = qualToDelete #thisqual is from another program
    except:
        print("typeError here")
        raise
    if len(userWork) != 0:
        if item2 in userWork[0].keys():
            tempInt = 0
            for work in userWork:
                if work["companyName"] == item1:
                    break
                tempInt += 1
            userWork.pop(tempInt)
    if len(userEducation) != 0:
        if item2 in userEducation[0].keys():
            tempInt = 0
            for degree in userEducation:
                if degree["degreeField"] == item1:
                    break
                tempInt += 1
            userEducation.pop(tempInt)
    if len(userSkills) != 0:
        if item2 in userSkills[0].keys():
            tempInt = 0
            for skills in userSkills:
                if skills["skillName"] == item1:
                    break
                tempInt += 1
            userSkills.pop(tempInt)
    if len(userProjects) != 0:
        if item2 in userProjects[0].keys():
            tempInt = 0
            for project in userProjects:
                if project["projectName"] == item1:
                    break
                tempInt += 1
            userProjects.pop(tempInt)
    args = firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects
    getListOfObjects(*args)


def getListOfObjects(*args):
    global itemList
    global firstName
    global middleInitial
    global lastName 
    global userLinkedin
    global userGithub
    global userPhone
    global userEmail
    global userWork
    global userEducation
    global userSkills
    global userProjects
    global new_frame
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    itemList = list()
    for work in userWork:
        itemList.append(tuple((work.get("companyName"), "companyName")))
    for edu in userEducation:
        itemList.append(tuple((edu.get( "degreeField"), "degreeField")))
    for skill in userSkills:
        itemList.append(tuple((skill.get("skillName"), "skillName")))
    for project in userProjects:
        itemList.append(tuple((project.get("projectName"), "projectName")))
    valList = list()
    for ttuple in itemList:
        item1, item2 = ttuple
        valList.append(item1)
    if len(valList) != 0:
        new_frame.children["editCombo"].configure(values=valList)
        new_frame.children["delCombo"].configure(values=valList)
    return itemList

def load_from_file(*args):
    global firstName
    global middleInitial
    global lastName 
    global userLinkedin
    global userGithub
    global userPhone
    global userEmail
    global userWork
    global userEducation
    global userSkills
    global userProjects
    global itemList
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    
    readFile = askopenfile(mode='r', filetypes=[('Text Document', '*.txt'), ('All Files', "*.*")])
    if readFile is not None:
        #this if clause is in case there is no info in the file selected or no file there
        #first lets clear the existing files
        listStringFromFile = []
        for x in readFile:
            listStringFromFile.append(x)
        readFile.close()
        tempInt = 0
        listArgs =[]
        for x in listStringFromFile:
            listArgs.append(json.loads(x))
        listPIIN = listArgs[0]
        listPIset =[firstName ,middleInitial ,lastName ,userLinkedin ,userGithub ,userPhone ,userEmail ]
        for x in range(0,7):
            listPIset[x].set(listPIIN[x])
        for item in listArgs[1]:
            userWork.append(item)
        for item in listArgs[2]:
            userEducation.append(item)
        for item in listArgs[3]:
            userSkills.append(item)
        for item in listArgs[4]:
            userProjects.append(item)
        #repack to args
        args = (firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects)
        itemList = getListOfObjects(*args)
                 
    else:
        
        messagebox.showerror(title="there is nothing here", message="try a different file?")

def save_to_file(*args):
    global userWork
    global userEducation
    global userSkills
    global userProjects
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    PIList = [firstName.get(),middleInitial.get(),lastName.get(),userLinkedin.get(),userGithub.get(),userPhone.get(),userEmail.get()]
    listArgs = []
    listArgs.append(PIList)
    listArgs.append(userWork)
    listArgs.append(userEducation)
    listArgs.append(userSkills)
    listArgs.append(userProjects)
    stringVarOut = ""
    for item in listArgs:
        tempString = stringVarOut + json.dumps(item) + "\n"
        stringVarOut = tempString
    
    string_to_save = stringVarOut
    with asksaveasfile(filetypes=[('Text Document', '*.txt'), ('All Files', "*.*")], defaultextension='.txt') as file:
        if file:
            file.write(string_to_save)

def make_settings_tab(parent, *args):
    global firstName
    global middleInitial
    global lastName 
    global userLinkedin
    global userGithub
    global userPhone
    global userEmail
    global userWork
    global userEducation
    global userSkills
    global userProjects
    global new_frame
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
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
    to_relevency_button = tk.Button(new_frame, text="to relevancy input", command=lambda:prepRelevencyFrame(*args))
    to_relevency_button.grid(column=curcol,row=curRow)
    curcol = 0
    curRow += 1
    qualToEdit = tk.StringVar(new_frame)
    new_combo_box, new_label  = create_combo_set2(new_frame, "select a Qualification to edit:", qualToEdit, getListOfObjects(firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects), "editCombo")
    new_label.grid(column=curcol, row=curRow)
    curcol += 1
    new_combo_box.grid(column=curcol, row=curRow)
    curcol += 1
    edit_button = tk.Button(new_frame, text=" edit ", command = lambda:editQualification(qualToEdit.get(), firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects))
    edit_button.grid(column=curcol,row=curRow)
    curRow += 1
    curcol = 0
    qualToDelete = tk.StringVar(new_frame)
    new_combo_box, new_label  = create_combo_set2(new_frame, "select a Qualification to delete:", qualToDelete, getListOfObjects(firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects), "delCombo")
    new_label.grid(column=curcol, row=curRow)
    curcol += 1
    new_combo_box.grid(column=curcol, row=curRow)
    curcol += 1
    edit_button = tk.Button(new_frame, text=" Delete ", command = lambda:removeQual(qualToDelete.get(), firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects))
    edit_button.grid(column=curcol,row=curRow)

    return new_frame

def prepRelevencyFrame(*args):
    global tempargs
    global userWork
    global userEducation
    global userSkills
    global userProjects
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    openRelevencyFrame(firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects)