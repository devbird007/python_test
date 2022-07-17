from myquestionsclass import Questions
#A test on identifying colors

question_prompts = [
	"What color are bananas?\n(a) Blue\n(b) Yellow\n(c) Teal\n\n",
	"What color are apples?\n(a) Green\n(b) Purple\n(c) Brown\n\n", 
	"What color are coconuts?\n(a) Blue\n(b) Brown\n(c) Green\n\n"
	"What color are strawberries?\n(a) Gold\n(b) White\n(c) Red\n\n",
]

questions = [
	Questions(question_prompts[0], "b"),
	Questions(question_prompts[1], "a"),
	Questions(question_prompts[2], "b"),
	Questions(question_prompts[3], "c")
]

def mytest(questions):
	score = 0
	for questio in questions:
		answer = input(questio.prompt)
		if answer == questio.answer:
			score += 1
	print("You scored "+ str(score) + "/" + str(len(questions)) + " correct.")
	

mytest(questions)
		
	
