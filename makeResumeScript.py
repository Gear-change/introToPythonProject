from fpdf import FPDF
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
    userFileName.append(".pdf")
    middleLetter = ""
    for letter in middleInitial:
        if letter.isalpha():
            middleLetter = letter
            break
    middleLetter = middleLetter.capitalize()
    userFullName = " ".join((firstName, middleLetter, lastName))
    userPhoneLen = len(userPhone)-1
    userPhoneFormatted = userPhone[
        0,
        userPhoneLen-10
    ] + "(" + userPhone[
        userPhoneLen-9,
        userPhoneLen-7
        ] + ") " + userPhone[
            userPhoneLen-6,
            userPhoneLen-4
            ] + "-" + userPhone[
                userPhoneLen-3,
                userPhoneLen
                ]
    contactLine = "\t".join((
        userPhoneFormatted, 
        userEmail, 
        userLinkedin, 
        userGithub
        ))
    marginX = 45.36
    marginYTop = 31.68
    marginYBottom = 13.68
    widthMax = 622 - marginX * 2
    pdf = FPDF(orientation="portrait", unit="pt",format="letter")
    pdf.add_page()
    pdf.set_margins(marginX, marginYTop, marginX)
    pdf.set_font("Cambria", "B", 16)

    pdf.cell(
        None, 
        None, 
        text=userFullName, 
        new_x="LEFT",
        new_y="BOTTOM"
        )
    pdf.set_font("Cambria", "", 11)
    pdf.cell(
        None,
        txt=contactLine,
        new_x="LEFT",
        new_y="BOTTOM"
    )
    pdf.image(
        "/components/hrBreak.png",
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
    pdf.set_font("Cambria", "BU", 11)
    pdf.cell(
        txt="Objective:",
        new_x="LEFT",
        new_y="BOTTOM"
    )
    pdf.set_font("Cambria", "", 11)
    pdf.cell(
        txt=userDesc,
        new_x="LEFT",
        new_y="BOTTOM"      
    )
    educationStr, educationDateStr = m2.format_education(userEducation)
    pdf.set_font("Cambria", "BU", 11)
    pdf.cell(
        txt="Education",
        new_x="LEFT",
        new_y="BOTTOM"
    )
    educationStrList = educationStr.split("\n")
    educationDateStrList = educationDateStr.split("\n")
    tempInt1 = 0
    tempInt2 = 0
    while tempInt1 < len(educationStrList):
        pdf.set_font("Cambria", "B", 11)
        pdf.cell(
            0,
            txt=educationStrList[tempInt1],
            new_x="LEFT",
        )
        tempInt1 += 1
        pdf.cell(
            0,
            educationDateStrList[tempInt2],
            new_x="LEFT",
            new_y="BOTTOM",
            align="R"
        )
        tempInt2 += 1
        pdf.set_font("Cambria", "", 11)
        pdf.cell(
            0,
            txt=educationStrList[tempInt1],
            new_x="LEFT"
        )
        tempInt1 += 1
        pdf.cell(
            0,
            educationDateStrList[tempInt2],
            new_x="LEFT",
            new_y="BOTTOM",
            align="R"
        )
        tempInt2 += 1
        curDetail = educationStrList[tempInt1]
        while curDetail.index("•")>0:
            pdf.cell(
                0,
                txt=curDetail,
                new_x="LEFT",
                new_y="BOTTOM",
            )
            tempInt1 += 1
            curDetail = educationStrList[tempInt1]
        pdf.cell(
            txt="\t",
            new_x="LEFT",
            new_y="BOTTOM"
        )
    pdf.set_font("Cambria", "BU", 11)
    pdf.cell(
        txt="Relevent Experience",
        new_x="LEFT",
        new_y="BOTTOM"
    )
    workStr, workDateStr = m2.format_work_experience_relevent(userWork)
    listWorkStr = workStr.split("\n")
    listDateWorkStr = workDateStr.split("\n")
    tempInt1 = 0
    for workDate in listDateWorkStr:
        pdf.set_font("Cambria", "B", 11)
        pdf.cell(
            0,
            txt = listWorkStr[tempInt1],
            new_x="LEFT"
        )
        tempInt1 += 1
        pdf.cell(
            0,
            txt=workDate,
            new_x="LEFT",
            new_y="BOTTOM",
            align="R"
        )
        pdf.set_font("Cambria", "", 11)
        pdf.cell(
            0,
            txt = listWorkStr[tempInt1],
            new_x="LEFT",
            new_y="BOTTOM"
        )
        tempInt1 += 1
        curDetail = listWorkStr[tempInt1]
        while curDetail.index("•")>0:
            pdf.cell(
                0,
                txt=curDetail,
                new_x="LEFT",
                new_y="BOTTOM",
            )
            tempInt1 += 1
            curDetail = listWorkStr[tempInt1]
        pdf.cell(
            txt="\t",
            new_x="LEFT",
            new_y="BOTTOM"
        )
    #TODO:create project and skill printouts
    pdf.set_font("Cambria", "BU", 11)
    pdf.cell(
        txt="Additional Experience",
        new_x="LEFT",
        new_y="BOTTOM"
    )
    workStr, workDateStr = m2.format_work_experience_other(userWork)
    listWorkStr = workStr.split("\n")
    listDateWorkStr = workDateStr.split("\n")
    tempInt1 = 0
    for workDate in listDateWorkStr:
        pdf.set_font("Cambria", "B", 11)
        pdf.cell(
            0,
            txt = listWorkStr[tempInt1],
            new_x="LEFT"
        )
        tempInt1 += 1
        pdf.cell(
            0,
            txt=workDate,
            new_x="LEFT",
            new_y="BOTTOM",
            align="R"
        )
        pdf.set_font("Cambria", "", 11)
        pdf.cell(
            0,
            txt = listWorkStr[tempInt1],
            new_x="LEFT",
            new_y="BOTTOM"
        )
        tempInt1 += 1
        curDetail = listWorkStr[tempInt1]
        while curDetail.index("•")>0:
            pdf.cell(
                0,
                txt=curDetail,
                new_x="LEFT",
                new_y="BOTTOM",
            )
            tempInt1 += 1
            curDetail = listWorkStr[tempInt1]
        pdf.cell(
            txt="\t",
            new_x="LEFT",
            new_y="BOTTOM"
        )
    