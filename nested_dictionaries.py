student_data = {
    "student1":{
        "name":"John",
        "age":25,
        "grade":"A",
        "city":"San Diego",
        "address":"California Institute of Technology"
    },
    "student2":{"name":"canny",
                "age":19,
                "grade":"B",
                "city":"texas",
                "address":"standford university"}
    }
# print(student_data["student1"]["name"])
# print(student_data["student2"]["name"])
# print(student_data["student1"]["age"])
# print(student_data["student2"]["age"])
# print(student_data["student1"]["city"])
# print(student_data["student2"]["city"])
# print(student_data["student1"]["address"])
# print(student_data["student2"]["address"])
del student_data["student1"]
print(student_data)