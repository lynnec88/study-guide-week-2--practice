# Part 1: Classes and Init Methods
class student:
    def __init__(self,first_name,last_name,address):
        self.first_name = first_name
        self.last_name = last_name
        self.address =address

class question:
    def __init__(self,text, answer):
        self.text = text
        self.answer = answer

class Exam:
    def __init__(self,name):
        self.name = name
        self.questions = []

    def add_question(self,question):
        self.questions.append(question)

# Part 2: Methods
class Exam:
    def add_question(self,question):
        self.questions.append(question)

    def prompt_question(self,student):
        print(question, text)

    def administer_exam(self,student):
        score = 0

        for question in self.questions:
            self.prompt_question(question)
            answer = input()
            if answer == question.answer:
                score += 1
        print(f"{student.name} scored {score} out of {len(self.questions)} on the {self.name} exam.")


# Part 3: Create an Exam for a Student
class StudentExam:
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam

    def take_exam(self):
        self.exam.administer_exam(self.student)

def example():
    # create a student
    s = Student("Alice", 1)

    # create a question
    q = Question("What is the capital of France?", "Paris")

    # create an exam and add the question
    e = Exam("Geography")
    e.add_question(q)

    # create a StudentExam and administer the exam
    se = StudentExam(s, e)
    se.take_exam()

# Part 4: Inheritance
class MathExam(Exam):
    def __init__(self, name):
        super().__init__(name)
        self.questions = [
            Question("What is 2+2?", "4"),
            Question("What is the square root of 64?", "8"),
            Question("What is 10% of 50?", "5")
        ]

class ScienceExam(Exam):
    def __init__(self, name):
        super().__init__(name)
        self.questions = [
            Question("What is the boiling point of water in Fahrenheit?", "212"),
            Question("What is the largest planet in our solar system?", "Jupiter"),
            Question("What is the chemical symbol for gold?", "Au")
        ]

# create MathExam and ScienceExam objects and add them to StudentExam objects to administer them to students.
        
