from abc import ABC, abstractmethod


class HospitalStaff(ABC):
    def show_name(self):
        print("Hospital Name")

    @abstractmethod
    def perform_duty(self):
        pass

class Doctor(HospitalStaff):
    def perform_duty(self):
        print("Doctor do the treatment of patient")

class Nurse(HospitalStaff):
    def perform_duty(self):
        print("Do care of patient")

class Receptionist(HospitalStaff):
    def perform_duty(self):
        print("Assist everyone and take phone calls")


# d1 = Doctor()
# d1.show_name()
# d1.perform_duty()

doctor = Doctor()
nurse = Nurse()
receptionist = Receptionist()

# Instead of calling each object's methods one by one,
# we store the objects in a list and use a loop to call the methods.

staff_members = [doctor, nurse, receptionist]
for staff in staff_members:
    staff.show_name()
    staff.perform_duty()

# without loop
# doctor.show_name()
# doctor.perform_duty()

# nurse.show_name()
# nurse.perform_duty()

# receptionist.show_name()
# receptionist.perform_duty()