""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS,
        diabetes, TG, LDL-C, HDL-C, graduation, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """
# 仮のユーザデータ
# user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
#         'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcMentalRisk(object):
    """ メンタルのリスクを計算する """

    def __init__(self, id, q1, q2, q3, q4, q5):
        """ 初期化 """
        self.id = id
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5

    def make_answer_list(self):
        """ メンタルに関する質問回答を一つにまとめる """
        user_answer = [self.q1, self.q2, self.q3, self.q4, self.q5]
        return user_answer

    def calc_who_point(self):
        """ リスト内の数字の合計を計算する """
        answer = self.make_answer_list()
        who_point = sum(answer)
        print(who_point)
        return who_point

    def get_mental_point(self):
        answer = self.make_answer_list()
        if 0 in answer:
            mental_point = 1
        else:
            who_point = self.calc_who_point()
            if who_point < 13:
                mental_point = 1
            else:
                mental_point = 0
        return mental_point

    def get_mental_signal(self):
        mp = self.get_mental_point()
        if mp == 0:
            mental_signal = 0
        else:
            mental_signal = 2
        return mental_signal

#
# test = CalcMentalRisk(user[0], int(user[20]), int(user[21]), int(user[22]), int(user[23]), int(user[24]))
# answer_list = test.make_answer_list()
# mental_point = test.get_mental_point()
# print('####################')
# print(answer_list)
# print('メンタル', type(mental_point), mental_point)
# print('####################')
