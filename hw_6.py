from collections import UserDict

class Field:
    # Базовий клас для полів запису.
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    # Поле для зберігання імені контакту.
    pass

class Phone(Field):
    # Поле для зберігання номера телефону.(вал 10 цифр)
    def __init__(self, value):
        super().__init__(value)
        if len(str(self.value)) != 10:
            raise ValueError("The number must be 10 digits long")
        
class Record:
    # Зберігання інформації про контакт, включаючи ім'я та список телефонів
    # Додавання Видалення Редагування Пошук
    def __init__(self, name):
        self.name = Name(name) 
        self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone)) 
    
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
            else: 
                raise ValueError(f"'{phone}' not found")
  
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone 
            else:
                raise ValueError(f"'{old_phone}' not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            else:
                raise ValueError(f"'{phone}' not found")
  
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    # Клас для зберігання та управління записами.
    # Додавання Пошук Видалення за іменем
    def add_record(self,name):
        self.data[name] = Record(name)
        
    def find_record(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise ValueError(f"'{name}' not found")
    
    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"'{name}' not found")