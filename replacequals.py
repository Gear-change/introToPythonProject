
from workTabFrame import addWorkToList
from skilltabframe2 import addNewSkill
from ProjectTabFrame import addNewProject
from relevencyFrame import *
from EducationTabFrame import *
from replacequals import *

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
