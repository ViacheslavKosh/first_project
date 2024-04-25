from collections import UserDict
'''
Сутності:

    Field: Базовий клас для полів запису.
    Name: Клас для зберігання імені контакту. Обов'язкове поле.
    Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    AddressBook: Клас для зберігання та управління записами.
'''
class Field:
    def __init__(self, value): # field = Field('Hello') | field = Field(1) | field = Field(24.09)
        self.value = value

    def __str__(self):
        return str(self.value) # 'Hello' | '1' | '24.09'
    
    def __repr__(self):
        return str(self.value) # 'Hello' | '1' | '24.09'
    

class Name(Field):
    def __init__(self, name=None):
        if name is None:
            raise ValueError
        super().__init__(name) # self.value = name


class Phone(Field):
    def __init__(self, phone): # '12345' -, '1234567890' +, '12345678901' -, +38012345678901-
        # phone = str(phone)
        if len(phone) != 10:
            raise ValueError
        super().__init__(phone)


class Record:
    def __init__(self, name): # record = Record('Ihor')
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone): # record.add_phone('1234567890')
        for p in self.phones: # [Phone('1234567890'), Phone('0987654321')] 
            if p.value == phone: # Phone('1234567890') == '1234567890' -> Class Phone, str '123' != 123
                return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone): # record.remove_phone('1234567890')
        # self.phones.remove(phone) # Phone('1234567890') == '1234567890'
        for p in self.phones: # [Phone('1234567890'), Phone('0987654321')] 
            if p.value == phone: # Phone('1234567890') == '1234567890' -> Class Phone, str '123' != 123
                self.phones.remove(p)
                return
        raise ValueError
    
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError
    
    def edit_phone_alternative(self, old_phone, new_phone):
        '''This method checks if the phone exists'''
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone): # record.find_phone('1234567890') -> Phone('1234567890')
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError
    
    def __str__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'
    
    def __repr__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'
    

class RecordAlternative:
    def __init__(self, name): # record = Record('Ihor')
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone): # record.add_phone('1234567890')
        if self.find_phone(phone):
            return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone): # record.remove_phone('1234567890')
        phone = self.find_phone(phone)
        if phone:
            self.phones.remove(phone)
            return
        raise ValueError
    
    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone
            return
        raise ValueError

    def find_phone(self, phone): # record.find_phone('1234567890') -> Phone('1234567890')
        for p in self.phones:
            if p.value == phone:
                return p

'''
Field:
    self.value - anything 1 | 3.14 | 'Hello'

Name(Field):
    self.value - str 'Ihor' | 'Andrii'

Phone(Field):
    self.value - str '1234567890' | '0987654321' | '+380098765'

Record:
    self.name - Name Name('Ihor')
    self.phones - list of Phone [] | [Phone('0987654321')] | [Phone('0987654321'), Phone('0987654322')]

AddressBook:
    self.data - dict {} | {'Ihor': Record('Ihor')}
'''
class AddressBook(UserDict): # addressBook = AddressBook()
    def add_record(self, record: Record): # record = Record('Ihor') addressBook.add_record(record)
        name = record.name.value
        self.data.update({name: record}) # {'Ihor': Record('Ihor')}

    def add_record_alternative(self, record: Record): # record = Record('Ihor') addressBook.add_record(record)
        name = record.name.value
        self.update({name: record}) # {'Ihor': Record('Ihor')}

    def find(self, name): # {'Ihor': Record('Ihor')}
        return self.get(name) # Record('Ihor')
    
    def delete(self, name):
        del self[name]

# my_dict = {}
# my_dict.update({'Ihor': Record('Ihor')})
# del my_dict['Ihor']
# print(my_dict)

# addressBook = AddressBook()
# addressBook.add_record('Heello')
# addressBook.update({'hello': 1})
# print(addressBook)
'''
Функціональність:

    AddressBook:Додавання записів.
    Пошук записів за іменем.
    Видалення записів за іменем.
    Record:Додавання телефонів.
    Видалення телефонів.
    Редагування телефонів.
    Пошук телефону.
'''

# if __name__ == '__main__':
#     # Створення нової адресної книги
#     book = AddressBook()

#     # Створення запису для John
#     john_record = Record("John")
#     john_record.add_phone("1234567890")
#     john_record.add_phone("5555555555")

#     # Додавання запису John до адресної книги
#     book.add_record(john_record)

#     # Створення та додавання нового запису для Jane
#     jane_record = Record("Jane")
#     jane_record.add_phone("9876543210")
#     book.add_record(jane_record)

#     # Виведення всіх записів у книзі
#     print('Printing all records')
#     for name, record in book.data.items():
#         print(record)

#     # Знаходження та редагування телефону для John
#     john = book.find("John")
#     john.edit_phone("1234567890", "1112223333")

#     print('Printing John record')
#     print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
#     print('Printing find by phone')
#     found_phone = john.find_phone("5555555555")
#     print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane
#     book.delete("Jane")



john = Record('John')
john.add_phone('1234567890')

addressBook = AddressBook()
addressBook.add_record(john)

jane = Record('Jane')
jane.add_phone('1234567890')

addressBook.add_record(jane)

print(addressBook.find('John'))