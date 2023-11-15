import tkinter as tk
from tkinter import ttk

def degreeToString(degree):
    try:
        return f"{degree['degreeType']} in {degree['degreeField']}: {degree['degreeSubField']}"
    except KeyError as e:
        print(f"Key error: {e} in degree")
        return " "

def addNewDegree(DegreeType, DegreeField, degreeSubField, schoolName, schoolCity, schoolState, 
                 SchoolDateEndMonth, SchoolDateEndYear, GPA, degreeDetails):
    newEducation = {
        "degreeType": DegreeType,
        "degreeField": DegreeField,
        "degreeMinor": degreeSubField,
        "SchoolName": schoolName,
        "degreeDetails": degreeDetails,
        "gradeGPA": GPA,
        "schoolCity": schoolCity,
        "schoolState": schoolState,
        "dateEndYear": SchoolDateEndYear,
        "dateEndMonth": SchoolDateEndMonth,
        "isRelevent": True
    }
    userEducation.append(newEducation)
    print(newEducation)

def makePersonalInformationtab(tab1, firstName, middleInitial, lastName, userLinkedin, 
                               userGithub, userPhone, userEmail):
    curCol = 0
    currRow = 0
    newEntry, newlabel = createLabelEntry(tab1, "First name: ", firstName)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(tab1, "Middle Initial: ", middleInitial)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(tab1, "Last name: ", lastName)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(tab1, "LinkedIn: ", userLinkedin)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(tab1, "Github: ", userGithub)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(tab1, "Phone Number: ", userPhone)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(tab1, "Email : ", userEmail)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0 
    currRow += 1

def createLabelEntry(parent, labelText, input):
    thislabel = ttk.Label(parent, text=labelText)
    entry = tk.Entry(parent, textvariable=input )
    return entry, thislabel

def createLabelTextField(parent, labelText, input):
    
    label = ttk.Label(parent, text=labelText, wraplength=125)
    input = tk.Text(parent, width=50, height=6)
    return label, input

def createSpinMonthYear(parent, labelText, month, year, yearsList):
    newLabel = ttk.Label(parent, text=labelText)
    newComboBox = ttk.Combobox(parent, width = 5,
                               textvariable = month,
                               values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newLabel2 = ttk.Label(parent, text=" - ")
    newComboBox1 = ttk.Combobox(parent, width = 5,
                               textvariable = year,
                               values = yearsList)
    month.set(1)
    year.set(1950)
    return newLabel, newComboBox, newLabel2, newComboBox1

def createSpinState(parent, labelText, input):
    newLabel = ttk.Label(parent, text=labelText)
    stateList = [ 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
                 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 
                 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
                 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
                 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 
                 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
                 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 
                 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
                 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
                 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    newComboBox = ttk.Combobox(parent, textvariable=input, values=stateList)
    input.set("State")
    return newLabel, newComboBox

def makeListFromText(degreeDetails):
    tempString = degreeDetails.get("1.0", 'end-1c')
    listout = []
    listTempIn = tempString.split('\n')
    for item in listTempIn:
        if len(item) !=0:
            newDictDetail = {
                "degreeDetail":item,
                "isRelevent":True
                }
            listout.append(newDictDetail)
    return(listout)

def addWorkToList(companyName, companyCity, companyState, OccupationTitlelist, 
                  occupationDetailsList, startYear, startMonth, endYear, endMonth):
    newWork = {
        "companyName":companyName,
        "companyCity":companyCity,
        "companyState":companyState,
        "occupationTitles":OccupationTitlelist,
        "occupationDetails":occupationDetailsList,
        #is relevent should only make them sorted between them for only this one, the other ones don't print if it is not relevent.
        "isRelevent":True,
        "dateEndYear":endYear,
        "dateEndMonth":endMonth,
        "dateStartYear":startYear,
        "dateStartMonth":startMonth,
    }
    userWork.append(newWork)

def makeEducationTabFrame(parent):
    newFrame = tk.Frame(parent)
    DegreeType = tk.StringVar()
    DegreeField = tk.StringVar()
    degreeSubField = tk.StringVar()
    schoolName = tk.StringVar()
    schoolCity = tk.StringVar()
    schoolState = tk.StringVar()
    SchoolDateEndMonth = tk.IntVar()
    SchoolDateEndYear = tk.IntVar()
    GPA = tk.StringVar()
    degreeDetails = tk.Text()
    # ... Declare other StringVar or IntVar variables ...

    yearsList = [year for year in range(1950, 2050)]

    #setting default for auto population
    DegreeField.set("Field")
    DegreeType.set("select a Type")

    # ... Populate Education Tab with labels, entries, comboboxes ...
    curRow = 0
    curCol = 0
    newLabel = tk.Label(newFrame, text="Degree type:")
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox = ttk.Combobox(newFrame, textvariable = DegreeType,
                                values = [ ' Highschool',  ' Accociate', ' Bachelor', 
                                          ' Master', ' Doctorate' ])
    newComboBox.grid(column=curCol,row=curRow)
    curCol = 0
    curRow += 1
    newEntry, newlabel =  createLabelEntry(newFrame, "Enter your degree's field: ", DegreeField)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newEntry, newlabel = createLabelEntry(newFrame, "Enter your Minor: ", degreeSubField)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newEntry, newlabel = createLabelEntry(newFrame, "Enter the name of the school you got it at: ", schoolName)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newEntry, newlabel = createLabelEntry(newFrame, "Enter that school's city: ", schoolCity)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newLabel, newComboBox = createSpinState(newFrame, "Enter that school's state: ", schoolState)
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newEntry, newlabel = createLabelEntry(newFrame, "Enter your overall GPA: ", GPA)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newLabel1, newComboBox, newLabel2, newComboBox1 = createSpinMonthYear(newFrame, "Grad date(month - year): ", SchoolDateEndMonth,     SchoolDateEndYear, yearsList)
    newLabel1.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol,row=curRow)
    curCol += 1
    newLabel2.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox1.grid(column=curCol,row=curRow)
    curRow += 1
    curCol = 0
    newLabel, degreeDetails = createLabelTextField(newFrame, "Some details about your time getting this degree:", degreeDetails)
    newLabel.grid(column=curCol,row=curRow)
    curCol+=1
    degreeDetails.grid(column=curCol,row=curRow, columnspan=3)
    curRow += 1
    # Add Degree Button
    btnSchoolSubmit = tk.Button(newFrame, text="Add Degree", 
                                command=lambda:addNewDegree(DegreeType.get(), 
                                                            DegreeField.get(),
                                                            degreeSubField.get(),
                                                            schoolName.get(), 
                                                            schoolCity.get(),  
                                                            schoolState.get(),  
                                                            SchoolDateEndMonth.get(), 
                                                            SchoolDateEndYear.get(), 
                                                            GPA.get(), 
                                                            makeListFromText(degreeDetails))) # Add other .get() calls
    btnSchoolSubmit.grid(column=curCol, row=curRow)
    return newFrame

def WorkFrame(parent):
    #first the variables and frames
    thisFrame = tk.Frame(parent)
    companyName = tk.StringVar()
    companyCity = tk.StringVar()
    companyState = tk.StringVar()
    occupationTitle = tk.Text()
    occupationDetailsText = tk.Text()
    oDateStartYear = tk.IntVar()
    oDateStartMonth = tk.IntVar()
    oDateEndYear = tk.IntVar()
    oDateEndMonth = tk.IntVar()

    #next the years list and other misc variables

    yearsList = [year for year in range(1950, 2050)]
    curCol = 0
    curRow = 0

    #next autopopulation values
    companyName.set("Company")
    companyCity.set("City")

    # create fields for entering data here
    newEntry, newlabel = createLabelEntry(thisFrame, "Name of company: ", companyName)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newEntry, newlabel = createLabelEntry(thisFrame, "Company's city: ", companyCity)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newEntry.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newLabel, newComboBox = createSpinState(thisFrame, "Company's state: ", companyState)
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newLabel, newComboBox, newLabel2, newComboBox1 = createSpinMonthYear(thisFrame, "When where you hired(month-year): ", oDateStartMonth, oDateStartYear, yearsList)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol,row=curRow)
    curCol += 1
    newLabel2.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox1.grid(column=curCol,row=curRow)
    curCol = 0
    curRow += 1
    newLabel, newComboBox, newLabel2, newComboBox1 = createSpinMonthYear(thisFrame, "When where you fired(month-year): ", oDateEndMonth, oDateEndYear, yearsList)
    newlabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox.grid(column=curCol,row=curRow)
    curCol += 1
    newLabel2.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox1.grid(column=curCol,row=curRow)
    curCol = 0
    curRow += 1
    newLabel, occupationTitle = createLabelTextField(thisFrame, "enter each title you had during your time here:", occupationTitle)
    newLabel.grid(column=curCol,row=curRow)
    curCol+=1
    occupationTitle.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    newLabel, occupationDetailsText = createLabelTextField(thisFrame, "enter the responsabilities you had at this job: " , occupationDetailsText)
    newLabel.grid(column=curCol,row=curRow)
    curCol+=1
    occupationDetailsText.grid(column=curCol,row=curRow, columnspan=3)
    curCol = 0
    curRow += 1
    btnSubmit = tk.Button(thisFrame, text="Add to Work history", 
                                command=lambda:addWorkToList(
                                    companyName.get(),
                                    companyCity.get(),
                                    companyState.get(),
                                    makeListFromText(occupationTitle),
                                    makeListFromText(occupationDetailsText),
                                    oDateStartYear.get(),
                                    oDateStartMonth.get(),
                                    oDateEndYear.get(),
                                    oDateEndMonth.get()
                                )) # Add other .get() calls
    btnSubmit.grid(column=curCol, row=curRow)
    return thisFrame

def mainApp():
    root = tk.Tk()
    root.title("Resume Generator")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)
    # ... Create other tabs ...

    tabControl.add(tab1, text='Personal Information')
    tabControl.add(tab2, text='Education')
    tabControl.add(tab3, text ='Work experience')
    tabControl.add(tab4, text ='Skills')
    tabControl.add(tab5, text ='Other')
    tabControl.add(tab6, text ='Output/print/load')
    # ... Add other tabs ...

    tabControl.pack(expand=1, fill="both")

    # Personal Information Tab
    firstName = tk.StringVar()
    middleInitial = tk.StringVar()
    lastName = tk.StringVar()
    userLinkedin = tk.StringVar()
    userGithub = tk.StringVar()
    userPhone = tk.StringVar()
    userEmail = tk.StringVar()
    makePersonalInformationtab(tab1, firstName, middleInitial, lastName, userLinkedin, 
                               userGithub, userPhone, userEmail)

    # ... Add other personal information entries ...
    
    # Education Tab

    newFrame = makeEducationTabFrame(tab2)
    newFrame.grid(column=0,row=0)

    # work tab

    newFrame = WorkFrame(tab3)
    newFrame.grid(column=0, row=0)

    # ... Other GUI elements ...

    root.mainloop()

# Global Variables
userWork = []
userEducation = []
genericEducation = {
    "degreeType":"",
    "degreeField":"",
    "degreeMinor":"",
    "gradeGPA":0,
    "schoolName":"",
    "schoolCity":"",
    "schoolState":"",
    "dateEndYear":0,
    "dateEndMonth":0,
    "isRelevent":True,
    "degreeDetails":[
        {
            "degreeDetail":"",
            "isRelevent":True
        }
    ],
}
genericWork = {
    "companyName":"",
    "companyCity":"",
    "companyState":"",
    "occupationTitles":[{
        "OccupationTitle":"",
        "isRelevent":True
    }],
    "occupationDetails":[{
        "OccupationDetail":"",
        "isRelevent":True
    }],
    #is relevent should only make them sorted between them for only this one, the other ones don't print if it is not relevent.
    "isRelevent":True,
    "dateEndYear":0,
    "dateEndMonth":0,
    "dateStartYear":0,
    "dateStartMonth":0,
}
genericSkill = {
    "skillName":"",
    "skillYears":"",
    "isRelevent":True,
}
genericProject = {
    "projectName":"",
    "hasEvent":True,
    "eventName":"",
    "month":0,
    "year":0,
    "projectDetails":[{
        "OccupationDetail":"",
        "isRelevent":True
    }],
}
# ... Other generic structures ...

mainApp()
