def sort_skills(userSkills):
    # Finding the maximum years of experience
    max_years = max(skill["skillYears"] for skill in userSkills)

    # Initializing the main list with empty sublists
    sorted_skills = [[] for _ in range(max_years + 1)]

    # Filling the main list with skill names
    for skill in userSkills:
        if skill["isRelevent"]:
            year_index = skill["skillYears"]
            sorted_skills[year_index].append(skill["skillName"])

    return sorted_skills