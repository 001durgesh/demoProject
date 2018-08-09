import student

std = student.Student("Durgesh",'Pune','drgEmail','idea')

std.displayName()
std.name = 'Rahul'
std.displayName()

std.setPassword("newPass")
print(std.getPassword())