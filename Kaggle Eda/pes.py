
from datetime import datetime

class Student:
    def __init__(self, student_id, name, age, grade_level):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade_level = grade_level
        self.subjects = {}
        self.attendance = []

    def add_subject_marks(self, subject, marks):
        self.subjects[subject] = marks

    def mark_attendance(self, status):
        self.attendance.append(status)

    def average_marks(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def attendance_percentage(self):
        if not self.attendance:
            return 0
        present = self.attendance.count("Present")
        return (present / len(self.attendance)) * 100

    def display_info(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade_level}")
        print("Subjects and Marks:")
        for subject, marks in self.subjects.items():
            print(f"  {subject}: {marks}")
        print(f"Average Marks: {self.average_marks():.2f}")
        print(f"Attendance: {self.attendance_percentage():.2f}%")

class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def display_info(self):
        print("\nTeacher Information")
        print(f"ID: {self.teacher_id}")
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_school_info(self):
        print("\n================================")
        print("PAKISTAN EDUCATION SYSTEM REPORT")
        print("================================")
        print(f"School Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Total Students: {len(self.students)}")
        print(f"Total Teachers: {len(self.teachers)}")

    def student_report(self):
        print("\n------ STUDENT REPORT ------")
        for student in self.students:
            student.display_info()

    def teacher_report(self):
        print("\n------ TEACHER REPORT ------")
        for teacher in self.teachers:
            teacher.display_info()

    def school_average(self):
        if not self.students:
            return 0

        total = 0
        count = 0

        for student in self.students:
            total += student.average_marks()
            count += 1

        return total / count

class MinistryEducationPakistan:
    def __init__(self):
        self.schools = []

    def register_school(self, school):
        self.schools.append(school)

    def national_report(self):
        print("\n===================================")
        print("PAKISTAN NATIONAL EDUCATION REPORT")
        print("===================================")

        print(f"Total Registered Schools: {len(self.schools)}")

        total_students = 0
        total_teachers = 0

        for school in self.schools:
            total_students += len(school.students)
            total_teachers += len(school.teachers)

        print(f"Total Students: {total_students}")
        print(f"Total Teachers: {total_teachers}")

        print("\nSchool Performance Summary")

        for school in self.schools:
            print(
                f"{school.name} ({school.city}) "
                f"Average Score: {school.school_average():.2f}"
            )
            
def main():

    school1 = School("Government High School", "Lahore")

    t1 = Teacher(101, "Ahmed Khan", "Mathematics")
    t2 = Teacher(102, "Fatima Ali", "Physics")
    t3 = Teacher(103, "Usman Shah", "English")

    school1.add_teacher(t1)
    school1.add_teacher(t2)
    school1.add_teacher(t3)

    s1 = Student(1, "Ali Raza", 15, "Grade 10")
    s2 = Student(2, "Ayesha Noor", 16, "Grade 10")
    s3 = Student(3, "Bilal Ahmed", 15, "Grade 10")

    s1.add_subject_marks("Mathematics", 88)
    s1.add_subject_marks("Physics", 81)
    s1.add_subject_marks("English", 90)

    s2.add_subject_marks("Mathematics", 95)
    s2.add_subject_marks("Physics", 89)
    s2.add_subject_marks("English", 92)

    s3.add_subject_marks("Mathematics", 76)
    s3.add_subject_marks("Physics", 72)
    s3.add_subject_marks("English", 80)

    attendance_data = [
        "Present", "Present", "Absent",
        "Present", "Present"
    ]

    for status in attendance_data:
        s1.mark_attendance(status)
        s2.mark_attendance("Present")
        s3.mark_attendance(status)

    school1.add_student(s1)
    school1.add_student(s2)
    school1.add_student(s3)

    ministry = MinistryEducationPakistan()
    ministry.register_school(school1)

    school1.display_school_info()
    school1.teacher_report()
    school1.student_report()

    print("\nSchool Average Score:",
          round(school1.school_average(), 2))

    ministry.national_report()

    print("\nReport Generated:",
          datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()