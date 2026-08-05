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
    if isinstance(age,int):
        return False
    if not isinstance(age,int):
        return False
    if age < 16 or age > 100:
        return False

    return True





def validate_cgpa(cgpa:float)-> bool:
    pass




def validate_student_id(student_id:int)-> bool:
    pass
