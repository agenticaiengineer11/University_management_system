def validate_name(name:str)-> bool:
    name = name.strip()

    if not name:
        return False
    if len(name) < 3 or len(name) > 50:
        return False
    if not name.replace(" ","").isalpha():
        return False
    
    return True
print(validate_name("Noman"))
print(validate_name("ali123"))
print(validate_name("Mukurram Aziz"))
print(validate_name("1234"))



def validate_age(age:int)-> bool:
    pass 




def validate_cgpa(cgpa:float)-> bool:
    pass




def validate_student_id(student_id:int)-> bool:
    pass
