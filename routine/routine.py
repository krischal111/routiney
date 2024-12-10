class Subject:
    def __init__(self, subject, type, teachers):
        self.subject = subject
        self.type = type
        self.teachers = teachers
    
times = [
    "10:15",
    "11:00",
    "11:45",
    "12:30",
    "1:00",
    "1:45",
    "2:30",
    "3:15",
    "4:00",
]

telecommunications_l = Subject("Telecommunications", "L", ["REY"])
professional_practice_l = Subject("Professional Practice", "L", ["SKS"])
information_systems_l = Subject("Information Systems", "L", ["AJ"])
information_systems_t = Subject("Information Systems", "T", ["AJ"])
EES_l = Subject("EES", "L", ["BA"])
telecommunications_lt = Subject("Telecommunications", "L+T", ["REY"])
telecommunications_p = Subject("Telecommunications", "P", ["NBA", "BRP"])
information_systems_p = Subject("Information Systems", "P", ["AJ", "BRP"])
elective_2_l = Subject("Elective 2", "L", [""])
elective_2_p = Subject("Elective 2", "P", [""])
elective_3_l = Subject("Elective 3", "L", [""])
elective_3_p = Subject("Elective 3", "P", [""])


routine = {
    "sunday": [
        (2, telecommunications_l),
        (1, "break"),
        (2, elective_2_l),
        (3, elective_2_p),
    ],
    "monday": [
        (2, elective_3_l),
        (1, "break"),
        (2, elective_3_l),
        (3, elective_3_p),
    ],
    "tuesday": [
        (2, None),
        (1, "break"),
        (2, professional_practice_l),
        (1, information_systems_t),
        (2, information_systems_l),
    ],
    "wednesday": [
        (2, EES_l),
        (1, "break"),
        (2, telecommunications_lt),
        (3, None),
    ],
    "thursday": [
        (1, None),
        (1, information_systems_l),
        (2, elective_2_l),
        (1, "break"),
        (3, telecommunications_p),
    ],
    "friday": [
        (3, information_systems_p),
        (2, None),
        (3, elective_3_p),
    ],
}

def format_routine(day:int):
    # 1 <= day <= 7, 1 = sunday, 7 = saturday
    day = (day) % 7
    if day == 0:
        return "Hooray, no classes on Saturday."
    day = list(routine.keys())[day-1]
    schedule_text = ''
    schedule_text += f"Routine for {day.capitalize()}:\n"
    this_period = 0
    for period, subject in routine[day]:
        schedule_text += f"\n{times[this_period]:5} - {times[this_period+period]:5} [{period} period{'s' if period!=1 else '':1}]: "
        if subject == "break":
            schedule_text += f"*Break*"
        elif subject is None:
            schedule_text += f"*Free period*"
        else:
            schedule_text += f"{subject.subject} [{subject.type}] Teachers: {', '.join(subject.teachers)}"
        this_period += period
    return schedule_text
        
if __name__ == "__main__":
    for i in range(7):
        print(format_routine(i))
        print()
        print()
        print()


    
