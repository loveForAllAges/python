

# class MyClass:
#     """Custom class"""
#     i = 1000

#     def __init__(self, a, b, s) -> None:
#         """Вызывается с после создания экземпляра с помощью __new__()."""
#         self.a = a
#         self.b = b
#         self.s = s
#         self.length = len(s)

#     def __iter__(self):
#         """Возвращает обьект с помощью __next__()."""
#         return self
    
#     def __next__(self):
#         """Обращается к элементам в контейнере по одному."""
#         if not self.length:
#             raise StopIteration
#         self.length -= 1
#         return self.s[self.length]

#     def foo(self):
#         return 1+2




# from datetime import date, datetime


# class Person:
# 	def __init__(self, last_name, first_name, birth_date):
# 		self.last_name = last_name
# 		self.first_name = first_name
# 		self.birth_date = datetime.strptime(birth_date, '%d.%m.%Y')
	
# 	def about(self):
# 		return f'ФИО: {self.last_name} {self.first_name}'
	
# 	def age(self):
# 		return f'Возраст: {int((datetime.today() - self.birth_date).total_seconds() // (60 * 60 * 24 * 365))}'


# class Enrollee(Person):
# 	def __init__(self, last_name, first_name, birth_date, faculty):
# 		super().__init__(last_name, first_name, birth_date)
# 		self.faculty = faculty
		

# class Student(Person):
# 	def __init__(self, last_name, first_name, birth_date, faculty, course):
# 		super().__init__(last_name, first_name, birth_date)
# 		self.faculty = faculty
# 		self.course = course
	

# class Teacher(Person):
# 	def __init__(self, last_name, first_name, birth_date, faculty, job, exp):
# 		super().__init__(last_name, first_name, birth_date)
# 		self.faculty = faculty
# 		self.job = job
# 		self.exp = exp


# e = Enrollee('Ivanov', 'Ivan', '03.03.2002', 'Development')
# s = Student('Petrov', 'Petr', '13.01.2004', 'Development', 4)
# t = Teacher('Sidorov', 'Sidr', '16.07.1988', 'Development', 'Teacher', 10)

# print(e.about(), e.age())
# print(s.about(), s.age())
# print(t.about(), t.age())

