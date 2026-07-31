from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, staff_id, employee_name, email_address, mobile, department):
        self.staff_id = staff_id
        self.employee_name = employee_name
        self.email_address = email_address
        self.mobile = mobile
        self.department = department

    @abstractmethod
    def perform_duty(self):
        pass

    def show_information(self):
        print(f"Employee ID:{self.staff_id}")
        print(f"Employee Name:{self.employee_name}")
        print(f"Employee Email:{self.email_address}")
        print(f"Employee Mobile No.:{self.mobile}")
        print(f"Employee Department:{self.department}")
    
class Receptionist(Employee):
   
    def perform_duty(self):
        print("Perform Recption Duty")
    
    def show_information(self):
       super().show_information()
       print(f"------------------")


class Nurse(Employee):
    def __init__(self, staff_id, employee_name, email_address, mobile, department, specialization ):
        super().__init__(staff_id, employee_name, email_address, mobile, department)
        self.specialization = specialization

    def perform_duty(self):
        print("Perform Nurse Duty")
    
    def show_information(self):
        super().show_information()
        print(f"Specialization: {self.specialization}")
        print(f"------------------")
        

class Doctor(Employee):
    def __init__(self, staff_id, employee_name, email_address, mobile, department, qualification, specialization):
        super().__init__(staff_id, employee_name, email_address, mobile, department)
        self.qualification = qualification
        self.specialization = specialization


    def perform_duty(self):
        print("Perform Doctor Duty")


    def show_information(self):
        super().show_information()
        print(f"Qualification: {self.qualification}")
        print(f"Specialization: {self.specialization}")
        print(f"--------------------")

class Patient:
    def __init__(self, patient_id, patient_name, address, email, phone, medical_history, assigned_doctor):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.address = address
        self.email = email
        self.phone = phone
        self.__medical_history = medical_history
        self.assigned_doctor = assigned_doctor

    def show_information(self):
        print(f"Patient Id: {self.patient_id}")
        print(f"Patient Name: {self.patient_name}")
        print(f"Patient Address: {self.address}")
        print(f"Patient Email: {self.email}")
        print(f"Patient Phone: {self.phone}")
        print(f"Patient Medical History: {self.__medical_history}")
        print(f"Patient Assigned Doctor: {self.assigned_doctor}")
        print(f"---------------------")





# d1 = Doctor(5, "Harish Chandra", "harish@gmail.com", 9855050402, "Surgery")
# d1.show_information()
# p1 = Patient("Ram Lal", "Ratnanagar", "ramlal@gmail.com", 9830320250, "Have cough and fever from last night", "Harish Chandra")
# p1.show_information()
# # print(p1.__medical_history)
# p1.__medical_history = "Updated medial problems"
# p1.show_information()
# print(p1.__dict__)

r1 = Receptionist(15, "Receptionist Rita", "rita@gmail.com", 9845336960, "main")
r1.show_information()

n1 = Nurse(25, "Nurse Gita", "gita@gmail.com", 9820250502, "Nursing", "Common Medicine")
n1.show_information()

d1 = Doctor(10, "Dr. Subash", "subash@gmail.com", 9855050201, "Neuro", "MD in Neuro Science", "Neuro Surgeon")
d1.show_information()

all_employees = [r1]
for employee in all_employees:
    employee.perform_duty()
    
p1 = Patient(5, "Ramu", "Ratnanagar", "ramu@gmail.com", 9845550301, "Have stomach pain", "Doctor subash")
p1.show_information()


# =========================
# TODO - Future Versions
# =========================

# TODO: Assign a Doctor object to a Patient instead of storing the doctor's name.

# TODO: Allow only an authorized Doctor to update medical history
# through controlled access.

# TODO: Create dynamic employee management instead of manually
# creating employee objects.

# TODO: Add file persistence after learning JSON/CSV.