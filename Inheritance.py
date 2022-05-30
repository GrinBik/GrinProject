class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        if numScores == 1:
            self.scores = scores[0]
        else:
            tmp_score = 0
            for i in range(numScores):
                tmp_score += scores[i]
            self.scores = tmp_score / numScores
        
    def calculate(self):
        if self.scores < 40:
            return "T"
        elif 40 <= self.scores < 55:
            return "D"
        elif 55 <= self.scores < 70:
            return "P"
        elif 70 <= self.scores < 80:
            return "A"
        elif 80 <= self.scores < 90:
            return "E"
        elif 90 <= self.scores <= 100:
            return "O"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())