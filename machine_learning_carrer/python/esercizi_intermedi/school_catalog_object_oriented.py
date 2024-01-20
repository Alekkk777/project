from typing import Any


class School:
    def __init__(self,name,level,numberOfStudents):
        self.name=name
        self.level=level
        self.numberOfStudents=numberOfStudents
    def get_Name(self):
        return self.name
    def get_Level(self):
        return self.level
    def get_NumberOfStudents(self):
        return self.numberOfStudents
    def set_NumberOfStudents(self,newNumberOfStudents):
        self.numberOfStudents=newNumberOfStudents
    def __repr__(self):
        return 'A '+ self.level + ' school named ' + self.name + ' with '+str(self.numberOfStudents)+' students '

class PrimarySchool(School):
    def __init__(self,name, numberOfStudents, pickupPolicy):
        super().__init__(name,"primary",numberOfStudents)
        self.pickupPolicy=pickupPolicy
    def get_PickupPolicy(self):
        return self.get_PickupPolicy
    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams=sportsTeams
    def get_SportTeams(self):
        return self.sportsTeams
    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + ",The Sports Team is {sportsTeams}".format(sportsTeams = self.sportsTeams)

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_SportTeams())
print(c)