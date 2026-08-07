def validate_name(name:str)-> bool:
    name = name.strip()

    if not name:
        return False
    if len(name) < 3 or len(name) > 50:
        return False
    if not name.replace(" ","").isalpha():
        return False
    
    return True



def validate_age(age:int)-> bool:
    if isinstance(age,bool):
        return False
    if not isinstance(age,int):
        return False
    if age < 16 or age > 100:
        return False

    return True





def validate_cgpa(cgpa:float)-> bool:
    if isinstance(cgpa,bool):
        return False
    if not isinstance(cgpa, (int,float)):
        return False
    if cgpa < 0.0 or cgpa > 4.0:
        return False

    return True





def validate_student_id(student_id:int)-> bool:
    if isinstance(student_id, bool):
        return False
    if not isinstance(student_id, int):
        return False
    if student_id <= 0:
        return False

    return True