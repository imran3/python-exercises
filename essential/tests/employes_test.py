from src.employes import Employee

def test_Employee_fullname():
    employee = Employee("John", "Smith")
    assert employee.fullname == "John Smith"

def test_Employee_email():
    employee = Employee("John", "Smith")
    assert employee.email == "John.Smith@mail.com"