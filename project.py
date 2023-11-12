import tkinter as tk
from tkinter import ttk

def degreeToString(degree):
    try:
        return f"{degree['degreeType']} in {degree['degreeField']}: {degree['degreeSubField']}"
    except KeyError as e:
        print(f"Key error: {e} in degree")
        return " "

def addNewDegree(DegreeType, DegreeField, degreeSubField, schoolCity, schoolState, 
                 SchoolDateEndMonth, SchoolDateEndYear, GPA, degreeDetails, schoolName):
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
        "dateEndMonth": SchoolDateEndMonth
    }
    userEducation.append(newEducation)

def makePersonalInformationtab(tab1, firstName, middleInitial, lastName, userLinkedin, 
                               userGithub, userPhone, userEmail):
    currCol = 0
    currRow = 0
    newEntryFrame = createLabelEntry(tab1, "First name: ", firstName)
    newEntryFrame.grid(column=currCol,row=currRow)
    currRow += 1
    newEntryFrame = createLabelEntry(tab1, "Middle Initial: ", middleInitial)
    newEntryFrame.grid(column=currCol,row=currRow)
    currRow += 1
    newEntryFrame = createLabelEntry(tab1, "Last name: ", lastName)
    newEntryFrame.grid(column=currCol,row=currRow)
    currRow += 1
    newEntryFrame = createLabelEntry(tab1, "LinkedIn: ", userLinkedin)
    newEntryFrame.grid(column=currCol,row=currRow)
    currRow += 1
    newEntryFrame = createLabelEntry(tab1, "Github: ", userGithub)
    newEntryFrame.grid(column=currCol,row=currRow)
    currRow += 1
    newEntryFrame = createLabelEntry(tab1, "Phone Number: ", userPhone)
    newEntryFrame.grid(column=currCol,row=currRow)
    currRow += 1
    newEntryFrame = createLabelEntry(tab1, "Email : ", userEmail)
    newEntryFrame.grid(column=currCol,row=currRow)
    currRow += 1

def makeDegreeDetailList(degreeDetails):
    tempString = degreeDetails
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

def createLabelEntry(parent, labelText, input):
    thisFrame = tk.Frame(parent)
    ttk.Label(thisFrame, text=labelText).grid(row=0, column=0)
    entry = tk.Entry(thisFrame, textvariable=input )
    entry.grid(row=0, column=1)
    return thisFrame

def createLabelTextField(parent, labelText, input):
    thisFrame = tk.Frame(parent)
    ttk.Label(thisFrame, text=labelText, wraplength=125).grid(column=0,row=0)
    input = tk.Text(thisFrame, width=50, height=6)
    input.grid(column=0, row=1)
    return thisFrame

def createSpinMonthYear(parent, labelText, input1, input2, yearsList):
    thisFrame = tk.Frame(parent)
    ttk.Label(thisFrame, labelText).grid(column=0,row=0)
    newComboBox = ttk.Combobox(parent, width = 5,
                               textvariable = input1 ,
                               values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newComboBox.grid(column=1,row=0)
    ttk.Label(parent, text=" - ").grid(column=2,row=0)
    newComboBox = ttk.Combobox(parent, width = 5,
                               textvariable = input2,
                               values = yearsList)
    newComboBox.grid(column=3,row=0)
    input1.set(1)
    input2.set(1800)
    return thisFrame

def createSpinState(parent, labelText, input):
    thisFrame = tk.Frame(parent)
    ttk.Label(thisFrame, labelText).grid(column=0,row=0)
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
    newComboBox = ttk.Combobox(thisFrame, textvariable=input, values=stateList)
    input.set("State")
    newComboBox.grid(column=1, row=0)
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
    DegreeType = tk.StringVar()
    DegreeField = tk.StringVar()
    degreeSubField = tk.StringVar()
    schoolName = tk.StringVar()
    schoolCity = tk.StringVar()
    schoolState = tk.StringVar()
    SchoolDateEndMonth = tk.IntVar()
    SchoolDateEndYear = tk.IntVar()
    GPA = tk.StringVar()
    degreeDetails = tk.StringVar()
    # ... Declare other StringVar or IntVar variables ...

    yearsList = [year for year in range(1950, 2050)]

    #setting default for auto population
    DegreeField.set("Field")
    DegreeType.set("select a Type")

    # ... Populate Education Tab with labels, entries, comboboxes ...
    curRow = 0
    curCol = 0
    newLabel = tk.Label(tab2, text="Degree type:")
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
    newComboBox = ttk.Combobox(tab2, textvariable = DegreeType,
                                values = [ ' Highschool',  ' Accociate', ' Bachelor', 
                                          ' Master', ' Doctorate' ])
    newComboBox.grid(column=curCol,row=curRow)
    curCol = 0
    curRow += 1
    newEntryField = createLabelEntry(tab2, "Enter your degree's field: ", DegreeField)
    newEntryField.grid(column=curCol,row=curRow, columnspan=2)
    curRow += 1
    newEntryField = createLabelEntry(tab2, "Enter your Minor: ", degreeSubField)
    newEntryField.grid(column=curCol,row=curRow, columnspan=2)
    curRow += 1
    newEntryField = createLabelEntry(tab2, "Enter your Minor: ", schoolName)
    newEntryField.grid(column=curCol,row=curRow, columnspan=2)
    curRow += 1
    newEntryField = createLabelEntry(tab2, "Enter your Minor: ", schoolCity)
    newEntryField.grid(column=curCol,row=curRow, columnspan=2)
    curRow += 1
    newEntryField = createLabelEntry(tab2, "Enter your Minor: ", schoolState)
    newEntryField.grid(column=curCol,row=curRow, columnspan=2)
    curRow += 1
    newEntryField = createLabelEntry(tab2, "Enter your Minor: ", GPA)
    newEntryField.grid(column=curCol,row=curRow, columnspan=2)
    curRow += 1
    newEntryField = createSpinMonthYear(tab2, "Grad date(month - year): ", 
                                        SchoolDateEndMonth, SchoolDateEndYear, yearsList)
    newEntryField.grid(column=curCol,row=curRow, columnspan=2)
    curRow += 1
    newEntryField = createLabelTextField(tab2, "Some details about your time getting this degree:", degreeDetails)
    newEntryField.grid(column=curCol,row=curRow, columnspan=2)
    curRow += 1
    

    # Add Degree Button
    btnSchoolSubmit = tk.Button(tab2, text="Add Degree", 
                                command=lambda:addNewDegree(DegreeType.get(), 
                                                            DegreeField.get(),
                                                            degreeSubField.get(),
                                                            schoolName.get(), 
                                                            schoolCity.get(),  
                                                            schoolState.get(),  
                                                            SchoolDateEndMonth.get(), 
                                                            SchoolDateEndYear.get(), 
                                                            GPA.get(), 
                                                            makeDegreeDetailList(degreeDetails.get("1.0", 'end-1c')))) # Add other .get() calls
    btnSchoolSubmit.grid(column=curCol, row=curRow)

    # ... Other GUI elements ...

    root.mainloop()

# Global Variables
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
    "companyCity":"",
    "occupationTitle":"",
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
