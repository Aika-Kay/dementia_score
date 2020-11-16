""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS,
        diabetes, TG, LDL-C, HDL-C, graduation, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """
# 仮のユーザデータ
# user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
#         'ある', '200', '200', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcCholesterolRisk(object):
    """ 総コレステロールのリスクを計算する """

    def __init__(self, id, tg, ldl, hdl):
        """ 初期化 """
        self.id = id
        self.tg = tg
        self.ldl = ldl
        self.hdl = hdl

    def calc_total_cholesterol(self):
        """ 総コレステロールを計算 """
        total_cholesterol = self.ldl + self.hdl + self.tg / 5
        return total_cholesterol

    def get_cholesterol_point(self):
        """ 総コレステロールから加算ポイント算出 """
        t_chol = self.calc_total_cholesterol()
        if t_chol < 251.3:
            t_chol_point = 0
        else:
            t_chol_point = 2
        return t_chol_point

    def get_chol_signal(self):
        """ 信号で表現するための値取得
            0: 青信号
            1: 黄色信号
            2: 赤信号 """
        user_chol = self.calc_total_cholesterol()
        if user_chol < 200:
            chol_signal = 0
        elif user_chol < 251.3:
            chol_signal = 1
        else:
            chol_signal = 2
        return chol_signal


# test = CalcCholesterolRisk(user[0], float(user[14]), float(user[15]), float(user[16]))
# user_chol = test.calc_total_cholesterol()
# chol_point = test.get_cholesterol_point()
# chol_signal = test.get_chol_signal()
# print('####################')
# print('Cholesterol:', user_chol, type(user_chol))
# print('point:', chol_point, type(chol_point))
# print('signal:', chol_signal, type(chol_signal))
# print('####################')