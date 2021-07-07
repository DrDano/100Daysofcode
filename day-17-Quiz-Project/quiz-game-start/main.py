from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)


QB = QuizBrain()
QB.next_question(question_list=question_bank)
