import pytest
import System

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


#1. login - System.py
def test_login(grading_system):
    username = "saab"
    password = "boomr345"
    grading_system.login(username,password)
    assert grading_system.usr.name == username
    assert grading_system.usr.courses[0] == "comp_sci"
    assert grading_system.usr.password == password

#2. check_password - System.py
def test_check_password(grading_system):
    username = "yted91"
    password = "imoutofpasswordnames"
    grading_system.login(username,password)
    assert grading_system.usr.password == password

#3. change_grade - Staff.py
def test_change_grade(grading_system):
    username = "goggins"
    password = "augurrox"
    grading_system.login(username,password)
    user = "yted91"
    course = "software_engineering"
    assignment = "assignment2"
    grade = 42
    grading_system.usr.change_grade(user,course,assignment,grade)
    assert grading_system.usr.check_grades(user,course)[1][1] == grade

#4. create_assignment Staff.py
def test_create_assignment(grading_system):
    username = "goggins"
    password = "augurrox"
    grading_system.login(username,password)
    assignment_name = "assignmentTEST"
    due_date = "2/28/20"
    course = "software_engineering"
    grading_system.usr.create_assignment(assignment_name, due_date, course)
    grading_system.reload_data()
    assert grading_system.usr.all_courses[course]['assignments'][assignment_name]["due_date"] == due_date

#5. add_student - Professor.py
def test_add_student(grading_system):
    username = "goggins"
    password = "augurrox"
    grading_system.login(username,password)
    name = 'bcrf53'
    course = 'software_engineering'
    grading_system.usr.add_student(name,course)         # fails in Line 21

#6. drop_student Professor.py
def test_drop_student(grading_system):
    username = "goggins"
    password = "augurrox"
    grading_system.login(username,password)
    name = "hdjsr7"
    course = 'software_engineering'
    grading_system.usr.drop_student(name,course)
    grading_system.reload_data()
    if course in grading_system.usr.users[name]['courses']:
        assert False
    else:
        assert True

#7. submit_assignment - Student.py
def test_submit_assignment(grading_system):
    username = 'yted91'
    password = 'imoutofpasswordnames'
    grading_system.login(username,password)
    course = 'software_engineering'
    assignment_name = 'assignmentTEST'
    submission = 'TEST TEST TEST'
    submission_date = '2/12/20'          # due_date is '2/3/20'
    grading_system.usr.submit_assignment(course,assignment_name,submission,submission_date)
    grading_system.reload_data()
    assert grading_system.usr.users[username]['courses'][course][assignment_name]['submission_date'] == submission_date #"This doesn't work because it uses the due_date for comp_sci assignment3, which doesn't exist"

#8. check_ontime - Student.py
def test_check_ontime(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username,password)
    date1 = '2/5/20'
    date2 = '2/26/20'
    assert grading_system.usr.check_ontime(date1,date2) == True
    assert grading_system.usr.check_ontime(date2,date1) == False

#9. check_grades - Student.py
def test_check_grades(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username,password)
    course1 = 'comp_sci'
    course2 = 'databases'
    grade11 = 99
    grade12 = 66
    grade21 = 23
    grade22 = 46
    assert grading_system.usr.check_grades(course1)[0][1] == grade11
    assert grading_system.usr.check_grades(course1)[1][1] == grade12
    assert grading_system.usr.check_grades(course2)[0][1] == grade21
    assert grading_system.usr.check_grades(course2)[1][1] == grade22

#10. view_assignments - Student.py
def test_view_assignments(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username,password)
    course1 = 'comp_sci'
    course2 = 'databases'
    due_date11 = '2/2/20'
    due_date12 = '2/10/20'
    due_date21 = '1/6/20'
    due_date22 = '2/6/20'
    assert grading_system.usr.view_assignments(course1)[0][1] == due_date11
    assert grading_system.usr.view_assignments(course1)[1][1] == due_date12
    assert grading_system.usr.view_assignments(course2)[0][1] == due_date21 # it checks the due_date for 'comp_sci'
    assert grading_system.usr.view_assignments(course2)[1][1] == due_date22

#11. test_case_login
def test_case_login(grading_system):
    username = "saab"
    password = "Boomr345"
    grading_system.login(username,password)
    assert grading_system.usr.name == username
    assert grading_system.usr.courses[0] == "comp_sci"
    assert grading_system.usr.password == password      # This has to be case sensitive!

#12. test wrong_professor
def test_wrong_person_creating(grading_system):
    username = "cmhbf5"
    password = "bestTA"
    grading_system.login(username,password)
    assignment_name = "assignmentTEST"
    due_date = "2/28/20"
    course = "databases"
    assert grading_system.usr.all_courses[course]['ta'] == username
    grading_system.usr.create_assignment(assignment_name, due_date, course)
    grading_system.reload_data()

#13. test_that_fails
def test_wrong_professor_changing(grading_system):
    username = "goggins"
    password = "augurrox"
    grading_system.login(username,password)
    user = "yted91"
    course = "cloud_computing"
    assert grading_system.usr.all_courses[course]['professor'] == username
    assignment = "assignment2"
    grade = 42
    grading_system.usr.change_grade(user,course,assignment,grade)

#14. drop_student Professor.py
def test_drop_wrong_student(grading_system):
    username = "goggins"
    password = "augurrox"
    grading_system.login(username,password)
    name = "akend3"
    course = 'comp_sci'
    assert grading_system.usr.all_courses[course]['professor'] == username
    grading_system.usr.drop_student(name,course)
    grading_system.reload_data()
    if course in grading_system.usr.users[name]['courses']:
        assert False
    else:
        assert True

#15. test_add_student_towrongclass
def test_add_student_towrongclass(grading_system):
    username = "goggins"
    password = "augurrox"
    grading_system.login(username,password)
    name = 'bcrf53'
    course = 'cloud_computing'
    assert grading_system.usr.all_courses[course]['professor'] == username
    grading_system.usr.add_student(name,course)         # fails in Line 21
