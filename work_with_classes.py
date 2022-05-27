# Класс "Студент", у которого есть:
# 1. Имя и Фамилия
# 2. Список оконченных и действующих курсов
# 3. Набор оценок по каждому из курсов
# 4. Средняя оценка по каждому из курсов
# 5. Средняя оценка по всем курсам (общая средняя оценка)

class Student:
    
    def __init__(self, name, surname):        
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.course_grade = {}
        self.middle_course_grade = {}
        self.middle_grade = 0.0

# Студент может оценить качество лекии конкретного лектора по конкретному курсу.

    def lecturer_assessment(self, lectur, course: str, grade: dict):    
        if isinstance(lectur, Lecturer):
            if course in lectur.courses_attached:
                if course in lectur.course_grade:
                    lectur.course_grade[course] += [grade]
                else:
                    lectur.course_grade[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return "Ошибка"

# Вычисление средней оценки студента по конкретному курсу.
    def course_average(self, course: str):
        course_grades = list(self.course_grade[course])
        if course in list(self.middle_course_grade.keys()):
            self.middle_course_grade[course] += sum(course_grades) / len(course_grades)
        else:
            self.middle_course_grade[course] = sum(course_grades) / len(course_grades)

# Средняя оценка студента по всем курсам (общая средняя оценка).
    def all_middle_grades(self):
        self.middle_grade = 0
        for course in list(self.course_grade.keys()):
            self.course_average(course)
            self.middle_grade += self.middle_course_grade[course]            
        self.middle_grade = self.middle_grade / len(list(self.course_grade.keys()))
        
# Вывод на экран в формате:
# Имя
# Фамилия
# Средняя оценка за домашние задания
# Курсы в процессе изучения
# Завершенные курсы
    def __str__(self):
        self.all_middle_grades()
        res = f'''Имя: {self.name}\nФамилия: {self.surname}\n
                  Средняя оценка за домашние задания: {self.middle_grade}\n
                  Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n
                  Завершенные курсы: {", ".join(self.finished_courses)}'''
        return res

# Возможность сравнить двух студентов по операнду "<"
    def __lt__(self, other):
        if isinstance(other, Student):
            self.all_middle_grades()
            other.all_middle_grades()
            if self.middle_grade < other.middle_grade:
                return True
            else:
                return False
        else:
            return 'Ошибка'
        
# Класс "Наставник", у которого есть:
# Имя и Фамилия
# Перечень курсов, к которым он относиться
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Класс "Лектор" (основанный на классе "Наставник"), у которого есть в дополнение к параметрам Наставника еще и следующее:
# Оценки по каждому из курсов, поставленные студентами
# Средняя оценка каждого курса
# Средняя оценка по всем курсам (общая средняя оценка)
class Lecturer(Mentor):

    def __init__(self, name, surname):   
        super().__init__(name, surname)
        self.course_grade = {}
        self.middle_course_grade = {}
        self.middle_grade = 0.0

# Вывод на экран в формате:
# Имя
# Фамилия
# Средняя оценка лекций (общая)
    def __str__(self):
        res = f'''Имя: {self.name}\n
                  Фамилия: {self.surname}\n
                  Средняя оценка за лекции: {self.middle_grade}'''
        return res

# Вычисление средней оценки лектора по заданному курсу.
    def course_average(self, course: str):
        course_grades = list(self.course_grade[course])
        if course in list(self.middle_course_grade.keys()):
            self.middle_course_grade[course] += sum(course_grades) / len(course_grades)
        else:
            self.middle_course_grade[course] = sum(course_grades) / len(course_grades)

# Средняя оценка лектора по всем курсам (общая средняя оценка).
    def all_middle_grades(self):
        self.middle_grade = 0
        for course in list(self.course_grade.keys()):
            self.course_average(course)
            self.middle_grade += self.middle_course_grade[course]
        self.middle_grade = self.middle_grade / len(list(self.course_grade.keys()))

# Возможность сравнить двух лекторов по операнду "<"
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            self.all_middle_grades()
            other.all_middle_grades()
            if self.middle_grade < other.middle_grade:
                return True
            else:
                return False
        else:
            return 'Ошибка'

# Класс "Рецензент" (основанный на классе "Наставник"), у которого есть право оценивать студентов по конкретному курсу.
class Reviewer(Mentor):

# Рецензент ставит оценку студенту по определенному курсу.
    def student_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in list(student.course_grade.keys()):
                student.course_grade[course] += [grade]
            else:
                student.course_grade[course] = [grade]
        else:
            return 'Ошибка'

# Вывод на экран в формате:
# Имя
# Фамилия       
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

# Функция для подсчета общей средней оценки всех студентов по всем курсам.
def middle_grade_students(course: str, *students):
    middle_grade = 0.0
    for student in students:
        student.course_average(course)
        middle_grade += student.middle_course_grade[course]
    return middle_grade

# Функция для подсчета общей средней оценки всех лекторов по всем курсам.
def middle_grade_lectures(course, *lectures):
    middle_grade = 0.0
    for lecture in lectures:
        lecture.course_average(course)
        middle_grade += lecture.middle_course_grade[course]
    return middle_grade

# Операционная часть программы
first_student = Student('Первый', 'Студент')
first_student.courses_in_progress += ['Python']

second_student = Student('Второй', 'Студент')
second_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Первый', 'Эусперт')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']

cool_lecturer = Lecturer('Первый', 'Лектор')
cool_lecturer.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('Второй', 'Лектор')
cool_lecturer_2.courses_attached += ['Python']
 
cool_reviewer.student_grade(first_student, 'Python', 10)
cool_reviewer.student_grade(first_student, 'Python', 10)
cool_reviewer.student_grade(first_student, 'Python', 1)

cool_reviewer.student_grade(second_student, 'Python', 1)
cool_reviewer.student_grade(second_student, 'Python', 1)
cool_reviewer.student_grade(second_student, 'Python', 1)

first_student.lecturer_assessment(cool_lecturer, 'Python', 10)
first_student.lecturer_assessment(cool_lecturer, 'Python', 10)
first_student.lecturer_assessment(cool_lecturer, 'Python', 5)

first_student.lecturer_assessment(cool_lecturer_2, 'Python', 10)
first_student.lecturer_assessment(cool_lecturer_2, 'Python', 10)
first_student.lecturer_assessment(cool_lecturer_2, 'Python', 1)

print(middle_grade_lectures('Python', cool_lecturer, cool_lecturer_2))