import tkinter as tk
from tkinter import ttk
from CommonTools import createComboSet, createLabelEntry, createSpinMonthYear,createLabelTextField, makeListFromText

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
    global userEducation
    userEducation.append(newEducation)

def degreeToString(degree):
    try:
        return f"{degree['degreeType']} in {degree['degreeField']}: {degree['degreeSubField']}"
    except KeyError as e:
        print(f"Key error: {e} in degree")
        return " "

def makeEducationTabFrame(parent, listEducation):
    global userEducation
    userEducation = listEducation
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
    degreeTypeList = [ ' Highschool',  ' Accociate', ' Bachelor', ' Master', ' Doctorate' ]

    #setting default for auto population
    DegreeField.set("Field")
    DegreeType.set("select a Type")

    # ... Populate Education Tab with labels, entries, comboboxes ...
    curRow = 0
    curCol = 0
    newComboBox, newLabel = createComboSet(newFrame, "Degree type:", DegreeType, degreeTypeList)
    newLabel.grid(column=curCol,row=curRow)
    curCol += 1
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
    newComboBox, newLabel = createComboSet(newFrame, "Enter that school's state: ", schoolState, stateList)
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
                                                            makeListFromText(degreeDetails, "degreeDetail"))) # Add other .get() calls
    btnSchoolSubmit.grid(column=curCol, row=curRow)
    return newFrame