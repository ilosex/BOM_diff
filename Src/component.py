

class ParsedComponent:
    name = ''
    quantity = 0
    description = ''
    designator = ''
    company = ''
    diff = ''
    LEN = 5

    def __init__(self, parameters):
        self.set_name(parameters)
        self.set_quantity(parameters)
        self.set_description(parameters)
        self.set_designator(parameters)
        self.set_company(parameters)

    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if self.name == other.name:
            return self.quantity > other.quantity
        else:
            return self.name > other.name

    def __str__(self):
        return f'{self.name}, {self.quantity}, {self.designator}, {self.description}, {self.company}'

    def __repr__(self):
        return f'{self.name}, {self.quantity}, {self.designator}, {self.description}, {self.company}'

    def set_name(self, parameters):
        self.name = parameters[0]

    def set_quantity(self, parameters):
        self.quantity = parameters[3]

    def set_designator(self, parameters):
        self.designator = parameters[2]

    def set_description(self, parameters):
        self.description = parameters[1]

    def set_company(self, parameters):
        self.company = parameters[4]


class SavedComponent:
    name = ''
    quantity = 0
    commentary = ''

    def __init__(self, parameters):
        self.set_name(parameters)
        self.set_quantity(parameters)
        self.set_commentary(parameters)

    def __gt__(self, other):
        if self.commentary == other.commentary:
            return self.name > other.name
        else:
            return self.commentary > other.commentary

    def __str__(self):
        return f'{self.name}, {self.quantity}, {self.commentary}'

    def __repr__(self):
        return f'[{self.name}, {self.quantity}, {self.commentary}]'

    def to_list(self):
        return [self.name, self.quantity, self.commentary]

    def set_name(self, parameters):
        self.name = parameters[0]

    def set_quantity(self, parameters):
        self.quantity = parameters[1]

    def set_commentary(self, parameters):
        self.commentary = parameters[2]
