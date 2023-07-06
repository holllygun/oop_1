lecturers_list = []
students_list = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_st_rate(self):
        total = 0
        count = 0
        if not self.grades:
            return 0
        for grades in self.grades.values():
            if len(grades) > 0:
                for grade in grades:
                    total += grade
                    count += 1
        return total / count

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


    def __lt__(self,other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.get_average_st_rate() < other.get_average_st_rate()
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания: {round(self.get_average_st_rate(), 2)} \nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers_list.append(self)

    def average_rate(self):
        overall_grade = 0
        grades_count = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:
                    for grade in grades:
                        overall_grade += grade
                        grades_count += 1
            return overall_grade / grades_count

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {round(self.average_rate(), 2)}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    pass
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}'
        return res
def avg_grade_all_lecturers(lecturers_list, course_name):
    av_grade = 0
    lecturers_count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached:
            av_grade += lecturer.average_rate()
            lecturers_count += 1
        if lecturers_count == 0:
            return 'Ошибка'
        return round(av_grade / lecturers_count, 2)


def avg_grade_all_students(students_list, course_name):
    av_grade = 0
    count = 0
    for student in students_list:
        if isinstance(student, Student) and course_name in student.courses_in_progress:
            av_grade += student.get_average_st_rate()
            count +=1
        if count == 0:
            return 'Ошибка'
        return round(av_grade / count, 2)

best_student = Student('Dipper', 'Pines', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.add_courses('C++')

bad_student = Student('Mabel', 'Pines', 'female')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Java']
bad_student.add_courses('C++')

cool_reviewer = Reviewer("Waddles", "Pig")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']

cool_reviewer = Reviewer("Dale", "Cooper")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']

cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Java', 4)
cool_reviewer.rate_hw(best_student, 'Java', 5)
cool_reviewer.rate_hw(best_student, 'Java', 4)

cool_reviewer.rate_hw(bad_student, 'Java', 5)
cool_reviewer.rate_hw(bad_student, 'Java', 5)
cool_reviewer.rate_hw(bad_student, 'Java', 5)
cool_reviewer.rate_hw(bad_student, 'Python', 4)
cool_reviewer.rate_hw(bad_student, 'Python', 5)
cool_reviewer.rate_hw(bad_student, 'Python', 3)

cool_lecturer = Lecturer('Lora', 'Palmer')
cool_lecturer.courses_attached += ['Python']
lecturers_list.append(cool_lecturer)

def_lecturer = Lecturer('Log', 'Lady')
def_lecturer.courses_attached += ['Python']
lecturers_list.append(def_lecturer)

best_student.rate_lecturer(cool_lecturer, "Python", 5)
best_student.rate_lecturer(cool_lecturer, "Python", 5)
best_student.rate_lecturer(cool_lecturer, "Python", 5)

bad_student.rate_lecturer(def_lecturer, "Python", 4)
bad_student.rate_lecturer(def_lecturer, "Python", 3)
bad_student.rate_lecturer(def_lecturer, "Python", 4)

print(cool_lecturer)
print()
print(cool_reviewer)
print()
print(best_student)
print()
print(best_student > bad_student)
print(def_lecturer > cool_lecturer)
print(avg_grade_all_lecturers(lecturers_list, 'Python'))
print(avg_grade_all_students(students_list, 'Python'))

