class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grades = {}

    def rate_lecturer(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grade(self, course):
        course_grades = list(self.grades[course])
        if course in list(self.middle_grades.keys()):
            self.middle_grades[course] += sum(course_grades) / len(course_grades)
        else:
            self.middle_grades[course] = sum(course_grades) / len(course_grades)

    def __str__(self):
        middle = 0
        for elem in list(self.grades.values()):
            middle += sum(elem) / len(elem)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {middle}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            middle_self = 0
            for elem in list(self.grades.values()):
                middle_self += sum(elem) / len(elem)
            middle_other = 0
            for elem in list(other.grades.values()):
                middle_other += sum(elem) / len(elem)
            if middle_self < middle_other:
                return False#f'{self.name} {self.surname} < {other.name} {other.surname} ({middle_self} < {middle_other})'
            else:
                return True#f'{self.name} {self.surname} > {other.name} {other.surname} ({middle_self} > {middle_other})'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.middle_grades = {}

    def __str__(self):
        middle = 0
        for elem in list(self.grades.values()):
            middle += sum(elem) / len(elem)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {middle}'
        return res

    def middle_grade(self, course):
        course_grades = list(self.grades[course])
        if course in list(self.middle_grades.keys()):
            self.middle_grades[course] += sum(course_grades) / len(course_grades)
        else:
            self.middle_grades[course] = sum(course_grades) / len(course_grades)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            middle_self = 0
            for elem in list(self.grades.values()):
                middle_self += sum(elem) / len(elem)
            middle_other = 0
            for elem in list(other.grades.values()):
                middle_other += sum(elem) / len(elem)
            if middle_self < middle_other:
                return False #f'{self.name} {self.surname} < {other.name} {other.surname} ({middle_self} < {middle_other})'
            else:
                return True #f'{self.name} {self.surname} > {other.name} {other.surname} ({middle_self} > {middle_other})'

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res
 
first_student = Student('Саша', 'Пузан', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['C++']

second_student = Student('Гриша', 'Бикинеев', 'your_gender')
second_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Первый', 'Преподователь')
cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Первый', 'Эусперт')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Первый', 'Лектор')
cool_lecturer.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('Второй', 'Лектор')
cool_lecturer_2.courses_attached += ['Python']
 
cool_reviewer.rate_hw(first_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Python', 1)

cool_reviewer.rate_hw(second_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Python', 5)

first_student.rate_lecturer(cool_lecturer, 'Python', 10)
first_student.rate_lecturer(cool_lecturer, 'Python', 10)
first_student.rate_lecturer(cool_lecturer, 'Python', 10)

second_student.rate_lecturer(cool_lecturer_2, 'Python', 10)
second_student.rate_lecturer(cool_lecturer_2, 'Python', 10)
second_student.rate_lecturer(cool_lecturer_2, 'Python', 5)
 
first_student.middle_grade('Python')
print(first_student.middle_grades)

cool_lecturer.middle_grades('Python')
print(cool_lecturer.middle_grades)