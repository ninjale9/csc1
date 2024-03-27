def student_grades (system,name,grades) :
    system[name]=grades 
    return system
def updating_student_grades(system,add_grading): 
    for key,value in system.items():
        if len(system) == 1 :
            system[key] += add_grading
        return system
system={}
while True :
    name = input("Please enter the name of the student: ")
    grades = input("Please enter the grade of the student: ")
    system.update({name : grades})
    
    if name.lower() == "stop" or grades.lower() == "stop" :
        break
    print (system)
