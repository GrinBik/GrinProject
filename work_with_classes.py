class Student:
    
    def __init__(self, name, surname, gender):
        
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.course_middle_grades = {}
        self.middle_grade = float

    def lecturer_evaluate(self, lectur, course: str, grade: dict):
        
        if isinstance(lectur, Lecturer):
            if course in lectur.courses_attached:
                if course in lectur.grades:
                    lectur.grades[course] += [grade]
                else:
                    lectur.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return "Ошибка"

    def course_middle_grade(self, course: str):

        course_grades = list(self.grades[course])

        if course in list(self.course_middle_grades.keys()):
            self.course_middle_grades[course] += sum(course_grades) / len(course_grades)
        else:
            self.course_middle_grades[course] = sum(course_grades) / len(course_grades)

    def all_middle_grades(self):

        self.middle_grade = 0

        for course in list(self.grades.keys()):
            course_middle_grade(self, course)
            self.middle_grade += course_middle_grades[course]

        self.middle_grade = self.middle_grade / len(list(self.grades.keys()))

    def __str__(self):

        all_middle_grades()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        
        if isinstance(other, Student):
            if self.middle_grade < other.middle_grade:
                return False
            else:
                return True
        else:
            return "Ошибка"
        
class Mentor:
    
    def __init__(self, name, surname):
        
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        
        super().__init__(name, surname)
        self.grades = {}
        self.course_middle_grades = {}
        self.middle_grade = float

    def __str__(self):
        
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_grade}'
        return res

    def course_middle_grade(self, course: str):

        course_grades = list(self.grades[course])

        if course in list(self.middle_grades.keys()):
            self.course_middle_grades[course] += sum(course_grades) / len(course_grades)
        else:
            self.course_middle_grades[course] = sum(course_grades) / len(course_grades)

    def all_middle_grades(self):

        self.middle_grade = 0

        for course in list(self.grades.keys()):
            course_middle_grade(self, course)
            self.middle_grade += self.course_middle_grades[course]

        self.middle_grade = self.middle_grade / len(list(self.grades.keys()))

    def __lt__(self, other):
    
        if isinstance(other, Lecturer):
            if self.middle_grade < other.middle_grade:
                return False
            else:
                return True
        else:
            return 'Ошибка'

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

first_student.lecturer_evaluate(cool_lecturer, 'Python', 10)
first_student.lecturer_evaluate(cool_lecturer, 'Python', 10)
first_student.lecturer_evaluate(cool_lecturer, 'Python', 10)

second_student.lecturer_evaluate(cool_lecturer_2, 'Python', 10)
second_student.lecturer_evaluate(cool_lecturer_2, 'Python', 10)
second_student.lecturer_evaluate(cool_lecturer_2, 'Python', 5)
 
first_student.course_middle_grade('Python')
print(first_student.course_middle_grades['Python'])
first_student.all_middle_grades()
print(first_student)

# cool_lecturer.middle_grades('Python')
# print(cool_lecturer.middle_grades)