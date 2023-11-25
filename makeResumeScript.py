
from fpdf2.fpdf import FPDF, YPos, XPos, Align
import m2akeresumescript as m2



def makeResume(*args):
    #TODO: MAKE THE RESUME PRINT FUNCTION
    userFileName, userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    userFileName = userFileName.replace(".", "_")
    userFileName = userFileName.replace("\\", "_")
    userFileName = userFileName.replace("/", "_")
    userFileName = userFileName.replace(":", "_")
    userFileName = userFileName.replace("|", "_")
    userFileName = userFileName.replace("<", "_")
    userFileName = userFileName.replace(">", "_")
    userFileName = userFileName.replace("\*", "_")
    userFileName = userFileName.replace("?", "_")
    userFileName = userFileName.replace("\"", "_")
    userFileName = userFileName.replace("'", "_")
    userFileName = userFileName + ".pdf"
    middleLetter = ""
    for letter in middleInitial:
        if letter.isalpha():
            middleLetter = letter
            break
    userPhoneLen = len(userPhone)-1
    listUserIndecies = []
    for x in range(0,10):
        listUserIndecies.append(userPhoneLen-x)
    userPhoneFormatted = ""
    for index in range(0,len(userPhone)):
        if index < listUserIndecies[9]:
            userPhoneFormatted = userPhoneFormatted + userPhone[index] 
        elif index == listUserIndecies[8]:
            userPhoneFormatted = userPhoneFormatted + "(" + userPhone[index] 
        elif index == listUserIndecies[7]:
            userPhoneFormatted = userPhoneFormatted + userPhone[index] 
        elif index == listUserIndecies[6]:
            userPhoneFormatted = userPhoneFormatted + userPhone[index]
        elif index == listUserIndecies[5]:
            userPhoneFormatted = userPhoneFormatted + ")" + userPhone[index]
        elif index == listUserIndecies[4]:
            userPhoneFormatted = userPhoneFormatted + userPhone[index]
        elif index == listUserIndecies[3]:
            userPhoneFormatted = userPhoneFormatted + userPhone[index]    
        elif index == listUserIndecies[2]:
            userPhoneFormatted = userPhoneFormatted + "-" + userPhone[index]
        else:
            userPhoneFormatted = userPhoneFormatted + userPhone[index]
    middleLetter = middleLetter.capitalize()
    userFullName = " ".join((firstName, middleLetter, lastName))
    contactLine = " ".join([userPhoneFormatted, userEmail, userLinkedin, userGithub])
    marginX = 45.36
    marginYTop = 31.68
    marginYBottom = 13.68
    pdf = FPDF(orientation="portrait", unit="pt",format="letter")
    pdf.add_page("P", "letter")
    pdf.add_font("Arial", fname="C:\Windows\Fonts\\arial.ttf")
    pdf.set_margins(marginX, marginYTop, marginX)
    pdf.set_font("Arial", "B", 16)

    pdf.cell(
        None, 
        None, 
        text=userFullName, 
        new_x=XPos.LEFT,
        new_y=YPos.NEXT
        )
    pdf.set_font("Arial", "", 11)
    pdf.cell(
        None,
        txt=contactLine,
        new_x=XPos.LEFT,
        new_y=YPos.NEXT
    )
    pdf.image(
        "hrBreak.png",
        None,
        None,
        pdf.epw,
        0,
        "",
        "",
        "",
        "Horizontal Rule",
        None,
        True
    )
    pdf.set_font("Arial", "BU", 11)
    pdf.cell(
        txt="Objective:",
        new_x=XPos.LEFT,
        new_y=YPos.NEXT
    )
    pdf.set_font("Arial", "", 11)
    pdf.cell(
        txt=userDesc,
        new_x=XPos.LEFT,
        new_y=YPos.NEXT      
    )
    educationStr, educationDateStr = m2.format_education(userEducation)
    pdf.set_font("Arial", "BU", 11)
    pdf.cell(
        txt="Education",
        new_x=XPos.LEFT,
        new_y=YPos.NEXT
    )
    educationStrList = educationStr.split("\n")
    educationDateStrList = educationDateStr.split("\n")
    tempInt1 = 0
    tempInt2 = 0
    while tempInt1 < len(educationStrList)-1:
        pdf.cell(
            0,
            txt=educationStrList[tempInt1],
            new_x=XPos.LEFT,
        )
        tempInt1 += 1
        pdf.cell(
            0,
            txt=educationDateStrList[tempInt2],
            new_x=XPos.LEFT,
            new_y=YPos.NEXT,
            align=Align.R
        )
        tempInt2 += 1
        pdf.set_font("Arial", "", 11)
        pdf.cell(
            0,
            txt=educationStrList[tempInt1],
            new_x=XPos.LEFT
        )
        tempInt1 += 1
        pdf.cell(
            0,
            txt=educationDateStrList[tempInt2],
            new_x=XPos.LEFT,
            new_y=YPos.NEXT,
            align=Align.R
        )
        tempInt2 += 1
        curDetail = educationStrList[tempInt1]
        while len(educationStrList)-1 != tempInt1 and curDetail.index("•")>0:
            pdf.cell(
                0,
                txt=curDetail,
                new_x=XPos.LEFT,
                new_y=YPos.NEXT,
            )
            tempInt1 += 1
            if len(educationStrList) == tempInt1:
                break
            curDetail = educationStrList[tempInt1]
        pdf.cell(
            txt="\t",
            new_x=XPos.LEFT,
            new_y=YPos.NEXT
        )
    pdf.set_font("Arial", "BU", 11)
    pdf.cell(
        txt="Relevent Experience",
        new_x=XPos.LEFT,
        new_y=YPos.NEXT
    )
    workStr, workDateStr = m2.format_work_experience_relevent(userWork)
    listWorkStr = workStr.split("\n")
    listDateWorkStr = workDateStr.split("\n")
    tempInt1 = 0
    for workDate in listDateWorkStr:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(
            0,
            txt = listWorkStr[tempInt1],
            new_x=XPos.LEFT
        )
        tempInt1 += 1
        if len(listWorkStr)-1 == tempInt1:
            break
        pdf.cell(
            0,
            txt=workDate,
            new_x=XPos.LEFT,
            new_y=YPos.NEXT,
            align=Align.R
        )
        pdf.set_font("Arial", "", 11)
        pdf.cell(
            0,
            txt = listWorkStr[tempInt1],
            new_x=XPos.LEFT,
            new_y=YPos.NEXT
        )
        tempInt1 += 1
        curDetail = listWorkStr[tempInt1]
        while curDetail.index("•")>0:
            pdf.cell(
                0,
                txt=curDetail,
                new_x=XPos.LEFT,
                new_y=YPos.NEXT,
            )
            tempInt1 += 1
            if len(listWorkStr)-1 == tempInt1:
                break
            curDetail = listWorkStr[tempInt1]
        pdf.cell(
            txt="\t",
            new_x=XPos.LEFT,
            new_y=YPos.NEXT
        )
    projectStrList = []
    dateProjectStrList = []
    projectStr, projectDateStr = m2.format_Projects(userProjects)
    projectStrList = projectStr.split("\n")
    dateProjectStrList = projectDateStr.split("\n")
    tempInt1 = 0
    if dateProjectStrList > 0:
        pdf.set_font("Arial", "BU", 11)
        pdf.cell(
            0,
            text="Other Relevent Experiences:",
            new_x=XPos.LEFT,
            new_y=YPos.NEXT
        )
    for project in dateProjectStrList:
        pdf.cell(
            0,
            text=projectStrList[tempInt1],
            new_x=XPos.RMARGIN,
            new_y=YPos.NEXT
        )
        tempInt1 += 1
        pdf.cell(
            0,
            text=project,
            align=Align.R,
            new_x=XPos.LEFT,
            new_y=YPos.NEXT
        )
        curDetail = projectStrList[tempInt1]
        while curDetail.index("•")>0:
            pdf.cell(
                0,
                text=curDetail,
                new_x=XPos.LEFT,
                new_y=YPos.NEXT
            )
            tempInt1+=1
            if len(projectStrList) == tempInt1:
                break
            curDetail = projectStrList[tempInt1]
        pdf.cell(
            0,
            text="\t",
            new_x=XPos.LEFT,
            new_y=YPos.NEXT
        )
    #TODO:add skills script 
    skillYearList = [[
            "skill1", 
            "skill2"
            ],
            [
                "skill3", 
                "skill4"
                ]]
    if len(skillYearList) > 0:
        pdf.set_font("Arial", "BU", 11)
        pdf.cell(
            0,
            txt="Skills",
            new_x=XPos.LEFT,
            new_y=YPos.NEXT
        )
        pdf.set_font("Arial", "", 11)
    for numlist in range(0, len(skillYearList)):
        if len(skillYearList[numlist]) == 2:
            newString = ", and ".join(skillYearList[numlist])
        elif len(skillYearList[numlist]) == 1:
            newString = skillYearList[numlist][0]
        elif len(skillYearList[numlist]) <= 0:
            continue
        else:
            newTempString = ", and ".join(skillYearList[numlist])
            newString = newTempString.replace(", and ", ", ", list(skillYearList[numlist])-2)
        pdf.cell(
        txt=newString,
        new_x=XPos.RIGHT,
        new_y=YPos.TOP
        )
        if numlist > 0:
            yearString = "....."+ str(numlist) + " Year"
            if numlist > 1:
                yearString = yearString + "s"
        else:
            yearstring = ".....Entry Level"
        pdf.cell(
            0,
            txt=yearString,
            new_x=XPos.RMARGIN,
            new_y=YPos.NEXT
        )
    pdf.set_font("Arial", "BU", 11)
    pdf.cell(
        txt="Additional Experience",
        new_x=XPos.LEFT,
        new_y=YPos.NEXT
    )
    workStr, workDateStr = m2.format_work_experience_other(userWork)
    listWorkStr = workStr.split("\n")
    listDateWorkStr = workDateStr.split("\n")
    tempInt1 = 0
    for workDate in listDateWorkStr:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(
            0,
            txt = listWorkStr[tempInt1],
            new_x=XPos.LEFT
        )
        tempInt1 += 1
        pdf.cell(
            0,
            txt=workDate,
            new_x=XPos.LEFT,
            new_y=YPos.NEXT,
            align=Align.R
        )
        pdf.set_font("Arial", "", 11)
        pdf.cell(
            0,
            txt = listWorkStr[tempInt1],
            new_x=XPos.LEFT,
            new_y=YPos.NEXT
        )
        tempInt1 += 1
        curDetail = listWorkStr[tempInt1]
        while len(listWorkStr)-1 != tempInt1 and curDetail.index("•")>0:
            pdf.cell(
                0,
                txt=curDetail,
                new_x=XPos.LEFT,
                new_y=YPos.NEXT,
            )
            tempInt1 += 1
            if len(listWorkStr)-1 == tempInt1:
                break
            curDetail = listWorkStr[tempInt1]
        pdf.cell(
            txt="\t",
            new_x=XPos.LEFT,
            new_y=FPDF.YPos.BOTT
        )
    