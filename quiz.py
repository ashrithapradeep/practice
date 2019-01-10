import random
f=open("quix.txt","r")
a=0
questions=[]
answers=[]
for i in f:
 	if a%2==0:
 		questions.append(i)
 	else:
 		answers.append(i)
 	a=a+1
x=[i for i in range(0,12)]
random.shuffle(x)
score=0
for i in x:
	print(questions[i])
	uanswer=input("enter your answer")
	answer1=answers[i].rstrip()
	if answer1==uanswer.capitalize():
		print("correct")
		score=score+1
	else:
		print("incorrect ")


print(score)
if score<4:
	print("poor performance")
elif score<8:
	print("medium performance")
else:
	print("excellent performance")