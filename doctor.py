class Doctor:
    def studied_years(self):
     print("I studied 7 years")
    def works_where(self):
     print("I work in a hospital")
    def paid_by_who(self):
     print("I get paid by the government")

class FamilyDoctor(Doctor):
    def what_specialization(self):
       print("I work with families")
    def paid_by_who(self):
     print("I get paid by the people")
    