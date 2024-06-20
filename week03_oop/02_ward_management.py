from typing import List, Union


class Student():
    def __init__(self, name: str, yob: int, subject: str) -> None:
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self) -> None:
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Teacher():
    def __init__(self, name: str, yob: int, subject: str) -> None:
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self) -> None:
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor():
    def __init__(self, name: str, yob: int, specialist: str) -> None:
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self) -> None:
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward():
    def __init__(self, name: str, persons: List[Union[Student, Teacher, Doctor]] = None) -> None:
        self.name = name
        self.persons = persons or []

    def add_person(self, person: Union[Student, Teacher, Doctor]) -> None:
        self.persons.append(person)
        
    def count_docter(self) -> int:
        return sum(1 for person in self.persons if isinstance(person, Doctor))
    
    def sort_age(self) -> List[Union[Student, Teacher, Doctor]]:
        self.persons.sort(key=lambda person: person.yob, reverse=True)
        
    def compute_average(self) -> float:
        teachers = [person for person in self.persons if isinstance(person, Teacher)]
        if not teachers:
            return 0.0
        return sum(teacher.yob for teacher in teachers) / len(teachers)
        
    def describe(self) -> None:
        print(f"Ward: {self.name}")
        for person in self.persons:
            person.describe()


if __name__ == "__main__":
    print("2(a)")
    student1 = Student(name="studentA", yob=2010, subject="7")
    teacher1 = Teacher (name="teacherA", yob=1969, subject="Math")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    student1.describe()
    teacher1.describe()
    doctor1.describe()

    print("\n2(b)")
    teacher2 = Teacher(name="teacherB", yob =1995, subject="History")
    doctor2 = Doctor(name ="doctorB", yob=1975 , specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(doctor1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor2)
    ward1.describe()

    print("\n2(c)")
    print(f"Number of docters: {ward1.count_docter()}")

    print("\n2(d)")
    print(f"After sorting Age of {ward1.name} people")
    ward1.sort_age()
    ward1.describe()

    print("\n2(e)")
    print(f"Average year of birth (teachers): {ward1.compute_average()}")
