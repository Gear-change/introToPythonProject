def format_education(userEducation):
    education_str = "Education\n"
    for edu in userEducation:
        if edu['isRelevent']:
            education_details = ', '.join(detail['degreeDetail'] for detail in edu['degreeDetails'] if detail['isRelevent'])
            education_str += f"{edu['degreeType']} in {edu['degreeField']}, {edu['schoolName']}, {edu['schoolCity']}, {edu['schoolState']} - GPA: {edu['gradeGPA']}\nMinor: {edu['degreeMinor']}\n{education_details}\n"
    return education_str

def format_work_experience(userWork):
    work_str = "Experience\n"
    for work in userWork:
        if work['isRelevent']:
            occupation_titles = ', '.join(title['OccupationTitle'] for title in work['occupationTitles'] if title['isRelevent'])
            occupation_details = '. '.join(detail['OccupationDetail'] for detail in work['occupationDetails'] if detail['isRelevent'])
            work_str += f"{work['companyName']}, {work['companyCity']}, {work['companyState']}\n{occupation_titles}\n{occupation_details}\n"
    return work_str


