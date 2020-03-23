import pickle
import os

phonebookdata='phonebook.data'
phonebook={'Tim':'123', 'Lol':'321'}

if 'phonebook.data' not in os.listdir():
    f=open(phonebookdata,'wb')#
    pickle.dump(phonebook, f)  #
    f.close()

"""f=open(phonebookdata,'rb')
storedphonebook=pickle.load(f)"""



while True:
    c=input ('Input action: addo, delo, printall, findo, findno ')
    if c=='0':
        print ('ending...')
        break
    
    if c in ('addo', 'delo', 'findo'):
        name=(input ('Input name '))    

        if c=='addo':
            valueo=(input ('Input value '))
            phonebook[name]=valueo
            print ('added', name)
           
            f=open(phonebookdata,'wb')  
            pickle.dump(phonebook, f)   
            f.close

            f=open(phonebookdata,'rb')     #если этого нет
            storedphonebook=pickle.load(f) #то в файл
            f.close                        #пишется пустота

        elif c=='delo':
            del phonebook[name]
            print ('deleted', name)
            

            f=open(phonebookdata,'wb')
            pickle.dump(phonebook, f)
            f.close

            f=open(phonebookdata,'rb')     #тоже самое
            storedphonebook=pickle.load(f)
            f.close

        elif c=='findo':
                                
            f=open(phonebookdata,'rb')     #тоже самое
            storedphonebook=pickle.load(f)
            f.close

            if name in storedphonebook:
                print (name, storedphonebook[name])
            else:
                print ('no name found')
                            
    elif c=='printall':
            f=open(phonebookdata,'rb')
            storedphonebook=pickle.load(f)
            print(storedphonebook)

    elif c=='findno':
        number=(input('Input number '))
        f=open(phonebookdata,'rb')
        storedphonebook=pickle.load(f)
        
        mirror = dict(zip(storedphonebook.values(), storedphonebook.keys()))
        if number in mirror:
            print(mirror[number])
        else:
            print("no number found")

    else:
        print ('Bad action')



"""import pickle

phonebook={'Tim':'123', 'Lol':'321'}
phonebookdata='phonebook.data'
f=open(phonebookdata,'wb')
pickle.dump(phonebook, f)
f.close

f=open(phonebookdata,'rb')
storedphonebook=pickle.load(f)
print(storedphonebook)"""
