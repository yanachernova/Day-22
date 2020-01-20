from random import randint
# or import random
class Family:
    # init its my constructor we need to call it when we create new family
    def __init__(self):
        self._last_name = "" # this atribute is private to update it we need to call add_member or delete_method
        self._name = ""
        self._age = 0
        self._members = [
            {"id": 1, "name": "Luis", "lastname": "Rodriguez", "age": 30}
        ] # Array need to safe each new family meber we going to create
    def _generateId(self): # Generate random id
        return randint(0, 99999999)
        #return random.randint(0, 99999999)

    def add_member(self, member): # Function to add a family meber
        member = {
            "id": self._generateId(), #create ID
            "name": member._name,
            "lastname": member._last_name,
            "age": member._age

        }
        self._members.append(member) #to add into array
        return member

    def delete_member(self, id): # Deleting element from array
        obj = self.get_member(id)
        self._members.remove(obj)

    def update_member(self, id, data): 
        obj = self.get_member(id)
        obj.update(data)
        return obj


    def get_member(self, id):
        member = list(filter(lambda item: item["id"] == id, self._members))
        return member[0]
    def get_all_members(self):

        return self._members 









