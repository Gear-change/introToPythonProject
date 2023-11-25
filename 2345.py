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

# Example 
userSkills = [
    {"skillName": "noYears1", "skillYears": 0, "isRelevent": True},
    {"skillName": "noYears2", "skillYears": 0, "isRelevent": True},
    {"skillName": "oneYears1", "skillYears": 1, "isRelevent": True},
    {"skillName": "oneYears2", "skillYears": 1, "isRelevent": False},
    {"skillName": "threeYears1", "skillYears": 3, "isRelevent": True},
]

listUserSkill = sort_skills(userSkills)
print(listUserSkill)
