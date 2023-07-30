###------------------------------------------------------------------------------
# Clasa este compusa din atribute ( variabile ) si metode ( functii )
# class Computer:
#     def config(self):
#         print("CPU: i5, RAM: 16GB, SSD: 1TB")
#
#
# comp1 = Computer()
#
# comp1.config()
# Computer.config(comp1)

# def __init__(self) - constructorul ( initializarea obiectului ) - creare
# def __del__(self) - destructor ( obiectului initializat ) - sterge/final program
#
# class Student:
#     def __init__(self):
#         print("Apelare constructor")
#
#     def __del__(self):
#         print("Apelare destructor")
#
#
# object = Student()
# # del object
# print("Sfarsit program")

# Python are un garbage collector care manage-uieste memoria automat.
# Totusi nevoia unui destructor apare cand ai o Clasa B care se paseaza pe ea insasi
# altel clase A. Atunci garbage collectorul pur si simplu nu stie ordinea
# in care sa distruga obiectele.

###----------------------------------------------------------------------------
# Tipuri de atribute
# - instance attribute ( declarate in __init__ si folosesc self )
# - class attribute ( declarate in afara oricarei metode )

# class Car:
#     roti = 4
#
#     def __init__(self):
#         self.marca = "Volvo"
#         self.km = 10000
#
#
# c1 = Car()
# c2 = Car()
#
# c1.km = 8000  # Instance attribute ( schimba valoarea lui c1 NU si c2 )
# Car.roti = 5  # class attribute ( schimba valoarea tuturor obiectelor din clasa respectiva )
#
# print(f'Obiectul C1 are: Numarul de roti: {c1.roti}, marca: {c1.marca}, km: {c1.km}')
# print(f'Obiectul C2 are: Numarul de roti: {c2.roti}, marca: {c2.marca}, km: {c2.km}')


###----------------------------------------------------------------------------
# Tipuri de metode
# - instance methods: este atunci cand folosim self in argument, practic lucreaza cu obiectul pe care urmeaza sa il initializam
# - class methods: lucreaza cu variabile de clasa ( de exemplu un get )
# - statis methods: daca vrem sa facem altceva extra cu clasa si nu are de-a face cu variabilele de instanta sau de clasa


# class Student:
#     school = "Poli"
#
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     # Instance method ( self )
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3) / 3
#
#     # Class method
#     @classmethod
#     def get(cls):
#         return cls.school
#
#     # Static method
#     @staticmethod
#     def info():
#         print("This is a help menu")
#


###----------------------------------------------------------------------------
# Mostenire - Inheritance
# - single level inheritance B -> A           => B(A): pass
# - multi level inheritance C-> B -> A        => C(B): pass si B(A): pass
# - multiple level inheritance C->A si C-B    = > B(A, B): pass

# - single level inheritance B -> A           => B(A): pass
# class A:
#     def __init__(self):
#         print("Inside class A")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Inside class B")
#
#
# object_b = B()


# - multi level inheritance C-> B -> A        => C(B): pass si B(A): pass
# class A:
#     def __init__(self):
#         print("Inside class A")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Inside class B")
#
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("Inside class C")
#
#
# object_c = C()


# - multiple level inheritance C->A si C-B    = > B(A, B): pass
# IMPORTANT: MRO Principle
# class A:
#     @staticmethod
#     def show():
#         print("Inside class A")
#
#
# class B:
#     @staticmethod
#     def show():
#         print("Inside class B")
#
#
# class C(A, B):
#     pass
#
#
# object_c = C()
# object_c.show()

###----------------------------------------------------------------------------
# Polimorfism
# Ce inseamna ? Adica poate sa aiba forme, poli = mai multe si form = forma
# In Python polimofismul poate sa fie de 4 tipuri:
# - duck Typing - Doar in PY
# - method overriding
# - method overloading
# - operator overloading

# - duck Typing - Doar in PY
# x = 3
# print(type(x))
#
# x = "ceva"
# print(type(x))

# Schimbarea tipului de date prin simpla atribuire ( din int in str ) se numeste duck typing.

# - method overriding

# class A:
#     @staticmethod
#     def show():
#         print("Inside class A")
#
#
# class B:
#     @staticmethod
#     def show():
#         print("Inside class B")
#
#
# class C(A, B):
#     @staticmethod
#     def show():
#         print("Inside class C")
#
#
# object_c = C()
# object_c.show()

# - method overloading

# class Student:
#     def sum(self, a=None, b=None, c=None):
#         s = 0
#         if a is not None and b is not None and c is not None:
#             s = a + b + c
#         elif a is not None and b is not None:
#             s = a + b
#         else:
#             s = a
#         return s
#
#
# student_1 = Student()
# print(student_1.sum(5, 9))
# print(student_1.sum(5, 9, 1))
# print(student_1.sum(5))

# - operator overloading
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1, m2)
#         return s3
#
#
# s1 = Student(5, 6)
# s2 = Student(10, 20)
#
# s3 = s2 + s1
#
# print(s3.m1)
# print(s3.m2)


### ----------------------------------------------------------------------------------------------------------------
# - Single Leading Underscore ( _var ) este doar o conventie, pentru programator, destinat uzului intern intr-o clasa
# - Single Trailing Underscore ( var_ ) este doar o conventie, pentru a evita conflictele cu anumite cuvinte cheie
# for_ = 2
# print(for_)
# - Double Leading Underscore ( __var ) cand este utilizata in interiorul clasei este redenumita practic
# _class__var pentru a evita conlifctele intr-o subclasa ( la mostenire ). Mai sunt denumite ca atribute private.

# class Sample:
#     def __init__(self):
#         self.mesaj1 = "hello"
#         self.__mesaj2 = "world"
#
#
# s = Sample()
# print(dir(s))

#
# number = 10

# - Double Leading and Trailing Underscore ( __var__ ) - Magic methods definite in python.
# print(number+40)
# print(number.__add__(40))

# - Single Underscore ( _ ) - Utilizator uneori in cazuri in care nu este importanta variabila respectiva, ori este una temp
# for _ in range(5):
#     print("ceva")
