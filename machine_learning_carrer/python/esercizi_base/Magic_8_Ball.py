import random
name="Sabrina"
question="Will Mattia Answers to Lavinia?"
answer = ""
random_number=random.randint(1, 9);
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "Outlook not so good"
else :
  answer = "Very doubtful"
if name=="":
    print("Joe asks: Will Mattia Answers to Lavinia?")
else :
    print("Qeustion: Will Mattia Answers to Lavinia?")
if len(question)==0:
    print("no answer for no question")
else :
    print("Magic 8-Ball's answer: "+answer)
