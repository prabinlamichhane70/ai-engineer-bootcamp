#Polymorphism means same method name but different behaviour
# Polymorphism is the ability of different objects to respond to the same method call in different ways.

class Car:
    def fuel(self):
        print("It uses Petrol")

class ElectricCar:
    def fuel(self):
        print("It uses electricity")

c1 = Car()
# c1.fuel()

e1 = ElectricCar()
# e1.fuel()

# obj-name = input # it have to use object name as input as shown below
# obj_name.sound() = out

def fuel_car(Vehicle):
    Vehicle.fuel()

fuel_car(c1)
fuel_car(e1)

# the real polymorphism is if you can pass arguments inside method, creating object and adding method just like obj.method() is somehow a polymorphism but actual polyporhism means pass arguments inside method name

class Camera:
    def photo(self):
        print("Camera can take a good photo")

class Smartphone:
    def photo(self):
        print("Smartphone can take photo nowdays")


c1 = Camera()
s1 = Smartphone()

def take_photos(electronic_device):
    electronic_device.photo() # here if you give any other attributes like new_photo or c_s_photo then it gives error AttributeError: 'Camera' object has no attribute 'new_photo' because it don't have any attributes name like that every class have it's method photo so you have to give the method name here "electronic_device.photo()- arguments with method_name()"
take_photos(c1)
take_photos(s1)




#another example
class Blog:
    def publish(self):
        print("You published blog post")

class Page:
    def publish(self):
        print("It published page")

class Event:
    def publish(self):
        print("Your event is published")

b1 = Blog() #created object
p1 = Page() #created object
e1 = Event()

#example polymorphism
def publish_content(website):
    website.publish()

publish_content(b1) #passed object in new method
publish_content(p1)
publish_content(e1)



class TextMessage:
    def send(self):
        print("Text message send")

class Email:
    def send(self):
        print("Email send")

class WhatsApp:
    def send(self):
        print("Whatsapp message, Done!")

class PushNotification:
    def send(self):
        print("Notification Sended")

t1 = TextMessage()
em1 = Email()
w1 = WhatsApp()
p1 = PushNotification()


def send_notification(notification):
    notification.send()


send_notification(t1)
send_notification(em1)
send_notification(w1)
send_notification(p1)