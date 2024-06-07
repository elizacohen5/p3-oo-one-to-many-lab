class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.owner = owner
        Pet.all.append(self)
    
    def __repr__(self):
        return f"<{self.name} the {self.pet_type}>"

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        result = []
        for pet in Pet.all:
            if pet.owner is self:
                result.append(pet)
        return result
    
    def add_pet(self, pet):
        if pet.pet_type in Pet.PET_TYPES:
            pet.owner = self

    def pet_key(self, pet):
        return pet.name
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key= self.pet_key)
    
    def __repr__(self):
        return f"<Owner: {self.name}>"


pistachio = Pet("pistachio", "dog", "Eliza")
eliza = Owner('eliza')
eliza.add_pet(pistachio)
print(eliza.get_sorted_pets())