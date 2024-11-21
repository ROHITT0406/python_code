from datetime import date
class person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    def age_calculator(self):
        today=date.today()
        age=today.year - self.date_of_birth.year
        if today < date(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        return age
person1=person("rohit","india",date(2001,6,1))
person2=person("mohit","india",date(2003,5,20))
person3=person("rahul","india",date(2004,2,5))
print("person 1 name",person1.name)
print("person 1 country",person1.country)
print("date of birth",person1.date_of_birth)
print("age of person",person1.age_calculator())
print("person 1 name",person2.name)
print("person 1 country",person2.country)
print("date of birth",person2.date_of_birth)
print("age of person",person2.age_calculator())
print("person 1 name",person3.name)
print("person 1 country",person3.country)
print("date of birth",person3.date_of_birth)
print("age of person",person3.age_calculator())