from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

QB = QuizBrain(question_bank)
while QB.still_has_questions():
    QB.next_question()
    print("")
else:
    print("Quiz Completed!")
    print(f"Your final score is: {QB.user_score}/{QB.question_number}")
