"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1. polymorphism - flexibility of types without using conditional statements,
      behavior depends on the data types used in operation
   2. encapsulation - data lives close to its functinality, storing data and 
      methods in a single class, only the methods in that class can access that data
   3. inheritance - objects can inherit from each other, once parent class is created, 
      child classes can acquire their attributes, methods, easy to make interchangable
      types of classes
   4. abstraction -knowledge of the object is not necessary for its use

2. What is a class?
   Class is a construct, type of thing like list or file, or string.

3. What is an instance attribute?
   The attribute lives only in the instance.


4. What is a method?
   Method is a function inside a class, methods can be applied to the data inside that class.

5. What is an instance in object orientation?
   Instance is an occurance of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   Class attribute lives on that class of objects, instance attribte only lives on that instance.
   If all instances of that class share an attribute I would make it a class attribute, 
   if the attribute is different depending on the instance I would set it to instance attribute.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print self.question
        user_answer  =raw_input("Your answer:\n>>> ")
        if user_answer == self.correct_answer:
            return True
        return False


class Exam(object):
    def __init__(self, name):
        self.name = name
        self.questions = []


    def add_question(self, question, correct_answer):
        Question(question, correct_answer)
        self.questions.extend([question, correct_answer])

    def administer(self):
        score = 0
        for question,correct_answer in zip(self.questions[::2],self.questions[1::2]):
            if Question(question, correct_answer).ask_and_evaluate():
                score += 1

            else:
                print "Wrong answer"
        return score


class Quiz(Exam):

    def administer(self):
        score = super(Quiz, self).administer()
        if score >= (len(self.questions)/2.)/2.:
            return True
        else:
            return False










# the instructions on these two functions are unclear, they seem to do the same thing,
# I am assuming you want us to use take_test() in example(), but instructions dont say that

def take_test(exam, student):
    """Function that takes the exam as based on above classes"""

    test = exam
    student_instance = student
    student_instance.score = test.administer()

    print student_instance.score



def example():
    """Fucntion that creates a sampple exam and administers is 
        using the above take_test()"""

    test = Exam("civics exam")

    student = Student("anka","kondraska","683 sutter street")

    test.add_question("Who is in charge of the executive branch?", "the President")
    test.add_question("What does the Constitution do?", "defines the government")
    test.add_question("The idea of self-government is in the first three words of the Constitution. What are these words?", "We the People")
    test.add_question("The dream that is most often crashed in the United States", "the American dream")
    test.add_question("How many amendments does the Constitution have?", "27")
    test.add_question("WWhat is the economic system n the United States?", "capitalist economy")

    take_test(test, student)

# example()

    
























        

