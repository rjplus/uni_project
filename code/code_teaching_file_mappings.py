"""
Maps for Scotland Teaching File categorical variables.
Add/modify as needed according to Teaching_File_Variable_List.xlsx.
"""

GENERAL_HEALTH_MAP = {
    1: "Very good health",
    2: "Good health",
    3: "Fair health",
    4: "Bad health",
    5: "Very bad health"
}

ETHNIC_GROUP_MAP = {
    1: "White Scottish",
    2: "Other White British",
    3: "Irish",
    4: "Gypsy/Traveller",
    5: "Polish",
    6: "Other White",
    7: "Mixed or Multiple",
    8: "Indian",
    9: "Pakistani",
    10: "Bangladeshi",
    11: "Chinese",
    12: "Other Asian",
    13: "African",
    14: "Caribbean or Black",
    15: "Arab",
    16: "Other ethnic group"
}

ECONOMIC_ACTIVITY_MAP = {
   1: "Employee - full-time",
   2: "Employee - part-time",
   3: "Self-employed",
   4: "Student - economically active",
   5: "Unemployed",
   6: "Student - economically inactive",
   7: "Retired",
   8: "Looking after home/family",
   9: "Long-term sick/disabled",
   10: "Other"
}

SOCIAL_GRADE_MAP = {
    1: "Higher managerial",
    2: "Lower managerial",
    3: "Intermediate",
    4: "Small employers and own account workers",
    5: "Lower supervisory and technical",
    6: "Semi-routine",
    7: "Routine",
    8: "Never worked and long-term unemployed"
}

# Add other mappings as needed