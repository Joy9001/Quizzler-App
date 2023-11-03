import html


class QuizBrain:
    def __init__(self, ques_bank):
        self.q_no = 0
        self.q_list = ques_bank
        self.score = 0

    def next_question(self):
        curr_ques = self.q_list[self.q_no]
        self.q_no += 1
        ques = html.unescape(curr_ques.question)
        return f"Q.{self.q_no}: {ques}"
        # user_ans = input(f"Q.{self.q_no}: {ques} (True/False)?: ")
        # self.check_answer(user_ans, curr_ques.answer)

    def still_has_question(self):
        return self.q_no < len(self.q_list)

    def check_answer(self, user_ans):
        corr_ans = self.q_list[self.q_no - 1].answer
        if user_ans.lower() == corr_ans.lower():
            return True
        else:
            return False
