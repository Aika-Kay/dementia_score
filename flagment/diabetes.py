""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS,
        diabetes, TG, LDL-C, HDL-C, graduation, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """

# 仮のユーザデータ
# user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '5.3', '100',
#         'ない', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcDiabetesRisk(object):
    """ リスク要因「糖尿病」の判定 """

    def __init__(self, id, hba1c, fbs, diabetes):
        self.id = id
        self.hba1c = hba1c
        self.fbs = fbs
        self.diabetes = diabetes

    def get_diabetes_point(self):
        """ HbA1c, FBS, 糖尿病の問診からポイント算出 """
        if (self.hba1c >= 6.5
                or self.fbs >= 126
                or self.diabetes == 'ある'):
            diabetes_point = 1
        else:
            diabetes_point = 0
        return diabetes_point

    def get_diabetes_signal(self):
        """ 信号で表現するための値取得
            0: 青信号
            1: 黄色信号
            2: 赤信号 """
        dp = self.get_diabetes_point()
        if dp == 0:
            if (self.hba1c < 6.0
                    or self.fbs < 110):
                diabetes_signal = 0
            else:
                diabetes_signal = 1
            return diabetes_signal
        else:
            diabetes_signal = 2
        return diabetes_signal
#
#
# test = CalcDiabetesRisk(user[0], float(user[11]), float(user[12]), user[13])
# diabetes_point = test.get_diabetes_point()
# diabetes_signal = test.get_diabetes_signal()
#
# print('########################')
# print('糖尿病:', diabetes_point, type(diabetes_point))
# print('信号:', diabetes_signal)
# print('########################')