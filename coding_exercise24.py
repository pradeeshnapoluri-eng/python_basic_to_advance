student_data = [
    {
        "name":"manish",
        "age":21,
        "roll_no":123,
        "father_name":"satyanarayana",
        "course_learning":"Javascript",
    },
    {
        "name":"naveen",
        "age":21,
        "roll_no":234,
        "father_name":"sarah",
        "course_learning":"C++",
    }]
def add_new_student(name,age,roll_no,father_name,course_learning):
    new_student_data = {}
    new_student_data["name"] = name
    new_student_data["age"] = age
    new_student_data["roll_no"] = roll_no
    new_student_data["father_name"] = father_name
    new_student_data["course_learning"] = course_learning
    student_data.append(new_student_data)
add_new_student("kanika",31,"342","moorthy","python")
print(student_data)