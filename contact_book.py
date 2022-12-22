import csv
contacts = {}
print('Welcome to your Contacts!')
print('Here are some functions of the Contactbook')
print('1. Add a new contact')
print('2. Search for a contact using Name')
print('3. Search for a contact using Number')
print('4. Display the Contact List')
print('5. Delete a Contact')

print('6. Exit')
file1 = open('contacts.csv','r')


for row in csv.reader(file1):
    # row = row.split(',')
    # print(row[1])
    # contacts[row[0]] = row[1]
    # data = row.split(',')
    print(row)
    if row !=[]:
        contacts[row[0]] = row[1]



while True:
    inp = input('Enter your choice: ')
    if inp == '1':
        name = input('Enter the Name: ')
        phone = input('Enter the Number: ')
        contacts[name] = phone
        print('Contact Added Successfully')
    elif inp == '2':
        name = input('Enter the Name to search: ')
        names = list(contacts.keys())
        for n in names:
            if n.lower() == name.lower():
                print(f'{n}\t\t Number: {contacts[n]}')
                break
    elif inp == '3':
        number = input('Enter the Number to search: ')
        numbers = list(contacts.values())
        names = list(contacts.keys())

        for n in numbers:
            if n == number:
                i = numbers.index(n)
                print(f'{names[i]}\t\t Number: {n}')
                break
    elif inp == '4':
        for n in contacts:
            print(f'{n}\t\t Number: {contacts[n]}')
    elif inp == '5':
        name = input('Enter the Name to be deleted: ')
        if name in contacts:
            del contacts[name]
            print('Contact deleted successfully')
        else:
            print('No such contact exists')
    elif inp=='6':
        # data = []
        # header = ['Name', 'Number']
        with open('contacts.csv', 'w+') as file:
        # file = open('contacts.csv', 'a')
            writer = csv.writer(file)
            # writer.writerow(header)
            for name in contacts:
                data = [name,contacts[name]]
                writer.writerow(data)
        file.close()
        # for row in data:
        break
    else: print("Couldn't understand your input.")
