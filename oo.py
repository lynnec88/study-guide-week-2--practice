# Part 1: Classes and Init Methods
class student:
    def __init__(self,first_name,last_name,address):
        self.first_name = first_name
        self.last_name = last_name
        self.address =address

class question:
    def __init__(self,question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

class exam:
    def __init__(self,name):
        self.name = name
        self.questions = []

alberta_capital = question("What is the capital of Alberta?","Edmonton")
python_author = question("Who is the author of Python?","Guido Van Rossum") 
ubermelon_competitor = question("What is Ubermelon's top copetitor?","Lyft") 
balloonicorn_color = question("What color is a Balloonicorn?","Pink")

midterm = exam("Midterm")
midterm.questions.append(alberta_capital)
midterm.questions.append(python_author)

final = exam("Final")
final.questions.append(ubermelon_competitor)
final.questions.append(balloonicorn_color)


# Part 2: Methods
class exam:
    def __init__(self,name):
        self.name = name
        self.questions = []

    def add_question(self,question):
        self.questions.append(question)

    def administer(self):
        """ create administer method inside Exam class
initialize a variable called score --- set it to zero
loop through each of the questions in the exam
  for each question, call the question's method --- ask_and_evaluate
  if it returns True, increment score
calculate and return the percentage score """
        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
             score += 1
        percentage = (score/len(self.questions)) * 100
        print(f"Your score:{percentage}%")
        return percentage
class question:
    def __init__(self,question,answer):
        self.question =question
        self.answer = answer
    
    def ask_and_evaluate(self):
        user_answer = input(self.question + ">")
        return user_answer == self.answer

set_q = question("What is the method for adding an element to a set?",".add()")
pwd_q = question("What does pwd stand for?","print working directory")
list_q = question("Python lists are mutable, iterable, and what?","ordered")

exam = exam("midterm")
exam.add_question(set_q)
exam.add_question(pwd_q)
exam.add_question(list_q)

exam.administer()
# Output:
# What is the method for adding an element to a set? > .add()
# What does pwd stand for? > print working directory
# Python lists are mutable, iterable, and what? > ummm...
# Your score: 66.66666666666666%

exam.add_question(question('What is the method for removing a string\'s whitespace?', '.strip()'))


exam.administer()
# Output:
# What is the method for adding an element to a set? > .add()
# What does pwd stand for? > print working directory
# Python lists are mutable, iterable, and what? > ordered
# What is the method for removing a string's whitespace? > .strip()
# Your score: 75.0%

# Part 3: Create an Exam for a Student
class StudentExam:
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        self.score = self.exam.administer()
        print(f"{self.student.name} scored {self.score} on the {self.exam.name} exam.")


def example():
    # create exam
    exam = exam("Math Test")

    # add questions to the exam
    exam.add_question("What is 2+2?", ["a. 4", "b. 5", "c. 6"], "a")
    exam.add_question("What is the square root of 16?", ["a. 2", "b. 4", "c. 8"], "b")
    exam.add_question("What is the value of pi?", ["a. 3.14", "b. 2.71", "c. 1.618"], "a")

    # create student
    student = student("John Doe")

    # administer exam for student
    student_exam = StudentExam(student, exam)
    student_exam.take_test()

# Part 4: Inheritance
class Exam:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers

    def administer(self, student_answers):
        score = sum([1 for i in range(len(self.questions)) if self.answers[i] == student_answers[i]])
        return score / len(self.questions)

class Quiz(Exam):
    def administer(self, student_answers):
        score = sum([1 for i in range(len(self.questions)) if self.answers[i] == student_answers[i]])
        return 1 if score >= len(self.questions) / 2 else 0

class StudentExam:
    def __init__(self, exam, student_answers):
        self.exam = exam
        self.student_answers = student_answers

    def grade(self):
        return self.exam.administer(self.student_answers)

class StudentQuiz(StudentExam):
    def grade(self):
        return self.exam.administer(self.student_answers)


