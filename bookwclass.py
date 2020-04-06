class bookwclass():
    """Phone book class"""
    def __init__ (self):
        """creates default book"""
        self.phonebook={'Bob': 4098, 'Nick': 4139, 'Peter': 1489}

    def addo(self, name, valueo):
        """adding unit into dict"""
        self.phonebook.update({name:valueo})

    def delo(self, name):
        """deleting unit from dict"""
        del self.phonebook[name]

    def printall(self):
        """printing all units"""
        print(self.phonebook)

    def findo(self, name):
        """findinf name"""
        print (name, self.phonebook.get(name, 'unknown name'))

    def findno(self, number):
        """finding number"""
        self.mirror=dict(zip(self.phonebook.values(), self.phonebook.keys()))
        print (number, self.mirror.get(number, 'unknown number'))
            

book=bookwclass()
"""creating class object"""

while True:
    c=input ('Input action: addo, delo, printall, findo, findno ')
    
    if c=='0':
        print ('ending...')
        break

    if c in ('addo', 'delo', 'findo'):
        name=(input ('Input name '))
    

        if c=='addo':
            valueo=(input ('Input value '))
            book.addo(name, valueo)
            print ('added', name)

        elif c=='delo':
            book.delo(name)
            print ('deleted', name)

        elif c=='findo':
            book.findo(name)

    elif c=='printall':
        book.printall()

    elif c=='findno':
        b=int(input('Input number '))
        book.findno(b)

    else:
        print ('bad action, try again')

    
    


