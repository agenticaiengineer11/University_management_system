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
    if age < 16 or age > 100:
        return False

    return True
print(validate_age(15))
print(validate_age(16))
print(validate_age(22))
print(validate_age(100))
print(validate_age(101))
print(validate_age(-5))




def validate_cgpa(cgpa:float)-> bool:
    pass




def validate_student_id(student_id:int)-> bool:
    pass
