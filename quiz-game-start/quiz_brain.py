class QuizBrain:
    def __init__(self, q_list):
        self.current_q_no = 0
        self.score = 0
        self.q_list = q_list

    def question_rem(self):
        if self.current_q_no < len(self.q_list):
            return True
        else:
            return False

    def next_question(self):
        new_q_dict = self.q_list[self.current_q_no]
        self.current_q_no += 1
        answer = input(f"Q.{self.current_q_no} {new_q_dict.text} (True/False): ")
        return answer

    def answer_checker(self, u_answer):
        curr_q_dict = self.q_list[self.current_q_no -1]
        if curr_q_dict.answer.lower() == u_answer.lower():
            self.score += 1
            print(f"Answer is correct. Current Score: {self.score}\{self.current_q_no}")
            return True
        else:
            print(f"Incorrect answer. Your final score: {self.score}\{self.current_q_no}")
            return False

