from main import StudentsInMLOps

def test_enroll_students():
    students = StudentsInMLOps()
    students.enrollStudents(10)
    assert students.getTotalStrength() == 10

def test_drop_students():
    students = StudentsInMLOps()
    students.enrollStudents(10)
    students.dropStudents(5)
    assert students.getTotalStrength() == 5

def test_class_name():
    students = StudentsInMLOps()
    assert students.getClassName() == "StudentsInMLOps"
