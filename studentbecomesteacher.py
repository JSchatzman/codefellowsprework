lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = float(sum(numbers))/len(numbers)
    return total  

def get_average(student):
    homework = float(average(student["homework"]))
    quizzes = float(average(student["quizzes"]))
    tests = float(average(student["tests"]))
    return homework*.1 + quizzes*.3 + tests*.6 
    
def get_class_average(students):
    return average([get_average(student) for student in students])


students = [lloyd, alice, tyler]
print get_class_average(students)
