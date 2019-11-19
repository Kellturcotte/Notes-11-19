class Name():
    def __init__(self,age):
        self.__age = age

    def getAge(self):
        return self.__age


thing = Garth(57)
print(thing)
# # protected variable Can not change 
# #           |
# #           V
# print(thing.__age)
# Has to use method to access variable
#        |
#        V
print(thing.getAge())