import tkinter as tk                     
from tkinter import Entry, Grid, ttk
def degreeToString(degree):
    try:
        stringOut = degree.get("degreeType") + " in " + degree.get("degreeField") + ":" +("degreeSubField")
        return stringOut
    except:
        print("error degree")
        print(degree)
        return " "

def makeDegreeList(degreeDetails):
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

def addNewDegree(DegreeType, DegreeField, degreeSubField, schoolCity, schoolState, SchoolDateEndMonth, SchoolDateEndYear,GPA,degreeDetails, schoolName):
    global userEducation
    global genericEducation
    newEducation = genericEducation.copy()
    newEducation["degreeType"] = DegreeType
    newEducation["degreeField"] = DegreeField
    newEducation["degreeMinor"] = degreeSubField
    newEducation["gradeGPA"] = GPA
    newEducation["schoolCity"] = schoolCity
    newEducation["schoolState"] = schoolState
    newEducation["dateEndYear"] = SchoolDateEndYear
    newEducation["dateEndMonth"] = SchoolDateEndMonth
    newEducation["degreeDetails"] = degreeDetails
    newEducation["SchoolName"] = schoolName
    userEducation.append(newEducation)

def mainApp():
    global firstName  
    global middleInitial
    global lastName
    global userLinkedin
    global userGithub
    global userPhone
    global userEmail
    global userDescription
    global userEducation
    global userWork
    global userSkills
    global userProjects
    #https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
    root = tk.Tk() 
    root.title("Resume Generator") 
    tabControl = ttk.Notebook(root) 
    global tab2
    tab1 = ttk.Frame(tabControl) 
    tab2 = ttk.Frame(tabControl) 
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='Personal Information') 
    tabControl.add(tab2, text ='Education')
    tabControl.add(tab3, text ='Work experience')
    tabControl.add(tab4, text ='Skills')
    tabControl.add(tab5, text ='Other')
    tabControl.add(tab6, text ='Output/print/load')
    tabControl.pack(expand = 1, fill ="both")
    #now that the tab structure is done, on to populating our first tab 
    currRow = 0
    ttk.Label(tab1, text ="enter your information below: ").grid(row=currRow)
    currRow += 1
    ttk.Label(tab1, text ="First Name: ").grid(row=currRow,column=0)
    firstName = tk.StringVar()
    newEntry = Entry(tab1, textvariable=firstName).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Middle Initial: ").grid(row=currRow,column=0)
    middleInitial = tk.StringVar()
    newEntry = Entry(tab1,textvariable=middleInitial).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Last Name: ").grid(row=currRow,column=0)
    lastName = tk.StringVar()
    newEntry = Entry(tab1,textvariable=lastName).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Linkedin Profile: ").grid(row=currRow,column=0)
    userLinkedin = tk.StringVar()
    newEntry = Entry(tab1, textvariable=userLinkedin).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Github Profile(optional): ").grid(row=currRow,column=0)
    userGithub = tk.StringVar()
    newEntry = Entry(tab1, textvariable= userGithub).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Email: ").grid(row=currRow,column=0)
    userEmail = tk.StringVar()
    newEntry = Entry(tab1,textvariable=userEmail).grid(row=currRow,column=1)
    currRow += 1
    #this is tab1 done, now for tab2
    currCol = 0
    currRow = 0
    ttk.Label(tab2,text = "Degree type:").grid(column=currCol,row=currRow)
    currCol += 1
    #thanks:https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/?ref=lbp
    DegreeType = tk.StringVar()
    newcombo = ttk.Combobox(tab2, width = 27, textvariable = DegreeType , values = [ ' Highschool',  ' Accociate', ' Bachelor', ' Master', ' Doctorate' ])
    newcombo.grid(column=currCol,row=currRow, columnspan=3)
    currCol+=3
    ttk.Label(tab2, text="Degree Field: ").grid(column=currCol,row=currRow)
    currCol+=1
    DegreeField = tk.StringVar()
    newEntry = Entry(tab2, width = 27, textvariable=DegreeField )
    newEntry.grid(column=currCol,row=currRow)
    currCol = 0
    currRow +=1
    ttk.Label(tab2, text="Graduation date: ").grid(column=currCol,row=currRow)
    currCol += 1
    SchoolDateEndMonth = tk.IntVar()
    newComboBox = ttk.Combobox(tab2, width = 5, textvariable = SchoolDateEndMonth , values = [1,2,3,4,5,6,7,8,9,10,11,12])
    newComboBox.grid(column=currCol,row=currRow)
    yearsList= []
    currCol +=1
    ttk.Label(tab2, text=" - ").grid(column=currCol,row=currRow)
    for x in range(1950,2050):
        yearsList.append(x)      
    currCol +=1  
    SchoolDateEndYear = tk.IntVar()
    newComboBox = ttk.Combobox(tab2, width = 5, textvariable = SchoolDateEndYear , values = yearsList)
    newComboBox.grid(column=currCol,row=currRow)
    currCol +=1
    ttk.Label(tab2, text="Degree Minor: ").grid(column=currCol,row=currRow)
    currCol+=1
    degreeSubField = tk.StringVar()
    newEntry = Entry(tab2, width = 27, textvariable=degreeSubField )
    newEntry.grid(column=currCol,row=currRow)
    currCol = 0
    currRow += 1
    ttk.Label(tab2, text="Some details about your time getting this degree: ", wraplength=125).grid(column=currCol,row=currRow,rowspan=6)
    currCol += 1
    degreeDetails = tk.Text(tab2, width=50, height= 6)
    degreeDetails.grid(column=currCol,row=currRow,columnspan=3,rowspan=6)
    currCol+=2
    currCol += 1
    ttk.Label(tab2, text="School name: ").grid(column=currCol,row=currRow)
    currCol +=1
    schoolName = tk.StringVar()
    newEntry= Entry(tab2, textvariable=schoolName)
    newEntry.grid(column=currCol,row=currRow)
    currCol -= 1
    currRow += 1
    ttk.Label(tab2, text="School City: ").grid(column=currCol,row=currRow)
    currCol+=1
    schoolCity = tk.StringVar()
    newEntry = Entry(tab2, width = 27, textvariable=schoolCity )
    newEntry.grid(column=currCol,row=currRow)
    currCol = 0
    currRow+=1
    currCol+=1
    currCol+=3
    ttk.Label(tab2, text="School State: ").grid(column=currCol,row=currRow)
    currCol+=1
    schoolState = tk.StringVar()
    newComboBox = ttk.Combobox(tab2, width = 27, textvariable = schoolState , values = [ 'Alabama',
                                                                                            'Alaska', 
                                                                                            'Arizona', 
                                                                                            'Arkansas',
                                                                                            'California',
                                                                                            'Colorado',
                                                                                            'Connecticut',
                                                                                            'Delaware',
                                                                                            'Florida',
                                                                                            'Georgia',
                                                                                            'Hawaii',
                                                                                            'Idaho',
                                                                                            'Illinois',
                                                                                            'Indiana',
                                                                                            'Iowa',
                                                                                            'Kansas',
                                                                                            'Kentucky',
                                                                                            'Louisiana',
                                                                                            'Maine',
                                                                                            'Maryland',
                                                                                            'Massachusetts',
                                                                                            'Michigan',
                                                                                            'Minnesota',
                                                                                            'Mississippi',
                                                                                            'Missouri',
                                                                                            'Montana',
                                                                                            'Nebraska',
                                                                                            'Nevada',
                                                                                            'New Hampshire',
                                                                                            'New Jersey',
                                                                                            'New Mexico',
                                                                                            'New York',
                                                                                            'North Carolina',
                                                                                            'North Dakota',
                                                                                            'Ohio',
                                                                                            'Oklahoma',
                                                                                            'Oregon',
                                                                                            'Pennsylvania',
                                                                                            'Rhode Island',
                                                                                            'South Carolina',
                                                                                            'South Dakota',
                                                                                            'Tennessee',
                                                                                            'Texas',
                                                                                            'Utah',
                                                                                            'Vermont',
                                                                                            'Virginia',
                                                                                            'Washington',
                                                                                            'West Virginia',
                                                                                            'Wisconsin',
                                                                                            'Wyoming'
                                                                                            ])
    schoolState.set('Alabama')
    newComboBox.grid(column=currCol,row=currRow)
    currRow += 1
    currCol = 4
    #date frame construct
    ttk.Label(tab2, text="GPA: ").grid(column=currCol, row=currRow)
    currCol +=1
    GPA = tk.DoubleVar()
    newEntry = Entry(tab2, width = 27, textvariable = GPA )
    newEntry.grid(column=currCol,row=currRow)
    #date frame construct
    currRow += 1
    currCol = 0
    #add the button to call the function to add an education
    currCol +=5
    btnSchoolSubmit = tk.Button(tab2, text="add Degree", 
                                command = (lambda :addNewDegree(DegreeType.get(),DegreeField.get(), degreeSubField.get(), schoolCity.get(),  schoolState.get(),  SchoolDateEndMonth.get(), SchoolDateEndYear.get(), GPA.get(),makeDegreeList(degreeDetails.get("1.0", 'end-1c')),schoolName.get())))
    btnSchoolSubmit.grid(column=currCol,row=currRow)
    root.mainloop()   
global genericEducation
global genericWork
global genericSkill
global genericProject
global firstName  
global middleInitial
global lastName
global userLinkedin
global userGithub
global userPhone
global userEmail
global userDescription
global userEducation
global userWork
global userSkills
global userProjects
#each education will use this structure,and be stored in the userEducation list
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
#each Work will use this structure,and be stored in the userWork list
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
#each Skill will use this structure,and be stored in the userSkills list
genericSkill = {
    "skillName":"",
    "skillYears":"",
    "isRelevent":True,
}
#each Project will use this structure and be stored in the userProjects list
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
userEducation=[]
userWork = []
userProjects = []
userSkills = []
mainApp()