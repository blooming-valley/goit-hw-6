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
        if len(self.value) != 10 or not self.value.isdigit():
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
        found = False  # Прапорець для відстеження того, чи знайдено номер
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                found = True
                break  # Зупинка циклу, якщо номер знайдено та змінено
        if not found:
            raise ValueError(f"'{old_phone}' not found")
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
  
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    # Клас для зберігання та управління записами.
    # Додавання Пошук Видалення за іменем
    def add_record(self,name):
        self.data[name] = Record(name)
        
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        del self.data[name]

