# Класс "Студент", у которого есть:
# 1. Имя и Фамилия
# 2. Список оконченных действующих курсов
# 3. Набор оценок по каждому из курсов
# 4. 
class Student:
    
    def __init__(self, name, surname):
        
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.course_grade = {}
        self.course_middle_grades = {}
        self.middle_grade = 0.0

    def lecturer_evaluate(self, lectur, course: str, grade: dict):
        
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

    def course_middle_grade(self, course: str):
        
        course_grades = list(self.course_grade[course])

        if course in list(self.course_middle_grades.keys()):
            self.course_middle_grades[course] += sum(course_grades) / len(course_grades)
        else:
            self.course_middle_grades[course] = sum(course_grades) / len(course_grades)

    def all_middle_grades(self):

        self.middle_grade = 0
        
        for course in list(self.course_grade.keys()):
            self.course_middle_grade(course)
            self.middle_grade += self.course_middle_grades[course]
            
        self.middle_grade = self.middle_grade / len(list(self.course_grade.keys()))
        
        
    def __str__(self):

        self.all_middle_grades()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.middle_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

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
        
class Mentor:
    
    def __init__(self, name, surname):
        
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        
        super().__init__(name, surname)
        self.course_grade = {}
        self.course_middle_grades = {}
        self.middle_grade = 0.0

    def __str__(self):
        
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_grade}'
        return res

    def course_middle_grade(self, course: str):

        course_grades = list(self.course_grade[course])

        if course in list(self.course_middle_grades.keys()):
            self.course_middle_grades[course] += sum(course_grades) / len(course_grades)
        else:
            self.course_middle_grades[course] = sum(course_grades) / len(course_grades)

    def all_middle_grades(self):

        self.middle_grade = 0
        
        for course in list(self.course_grade.keys()):
            self.course_middle_grade(course)
            self.middle_grade += self.course_middle_grades[course]

        self.middle_grade = self.middle_grade / len(list(self.course_grade.keys()))

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

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in list(student.course_grade.keys()):
                student.course_grade[course] += [grade]
            else:
                student.course_grade[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

def middle_grade_students(course: str, *students):
    middle_grade = 0.0
    for student in students:
        student.course_middle_grade(course)
        middle_grade += student.course_middle_grades[course]
    return middle_grade

def middle_grade_lectures(course, *lectures):
    middle_grade = 0.0
    for lecture in lectures:
        lecture.course_middle_grade(course)
        middle_grade += lecture.course_middle_grades[course]
    return middle_grade
 
first_student = Student('Саша', 'Пузан')
first_student.courses_in_progress += ['Python']

second_student = Student('Саша', 'Пузан')
second_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Первый', 'Эусперт')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']

cool_lecturer = Lecturer('Первый', 'Лектор')
cool_lecturer.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('Второй', 'Лектор')
cool_lecturer_2.courses_attached += ['Python']
 
cool_reviewer.rate_hw(first_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Python', 1)

cool_reviewer.rate_hw(second_student, 'Python', 1)
cool_reviewer.rate_hw(second_student, 'Python', 1)
cool_reviewer.rate_hw(second_student, 'Python', 1)

first_student.lecturer_evaluate(cool_lecturer, 'Python', 10)
first_student.lecturer_evaluate(cool_lecturer, 'Python', 10)
first_student.lecturer_evaluate(cool_lecturer, 'Python', 5)

first_student.lecturer_evaluate(cool_lecturer_2, 'Python', 10)
first_student.lecturer_evaluate(cool_lecturer_2, 'Python', 10)
first_student.lecturer_evaluate(cool_lecturer_2, 'Python', 1)

print(middle_grade_lectures('Python', cool_lecturer, cool_lecturer_2))