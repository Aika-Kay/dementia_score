""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS, 
        diabetes, TG, LDL-C, HDL-C, graduation, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """
# 仮のユーザデータ
# user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
#         'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcBmiRisk(object):
    """ BMIから、リスクを求める"""

    def __init__(self, id, height, weight):
        self.id = id
        self.height = height
        self.weight = weight

    def calc_bmi(self):
        """ BMIを計算するメソッド """
        # 身長(cm)を身長(m)に変換
        height_m = self.height / 100.0
        # BMIを計算
        bmi = self.weight / height_m ** 2
        # 少数第一位表記に変更
        fix_bmi = float(round(bmi, 1))
        return fix_bmi

    def get_bmi_point(self):
        """ BMI値から加算ポイント算出 """
        user_bmi = self.calc_bmi()
        if user_bmi < 26.1:
            bmi_point = 0
        else:
            bmi_point = 2
        return bmi_point

    def get_bmi_signal(self):
        """ 信号で表現するための値取得
            0: 青信号
            1: 黄色信号
            2: 赤信号 """
        user_bmi = self.calc_bmi()
        if user_bmi < 25.0:
            bmi_signal = 0
        elif user_bmi < 26.1:
            bmi_signal = 1
        else:
            bmi_signal = 2
        return bmi_signal


# TODO: 健康診断結果にID付与が可能か確認。

#
# test = CalcBmiRisk(user[0], int(user[2]), int(user[3]), int(user[4]), float(user[6]), float(user[7]))
# user_bmi = test.calc_bmi()
# bmi_point = test.get_bmi_point()
# bmi_signal = test.get_bmi_signal()
# print('####################')
# print('BMI:', user_bmi, type(user_bmi))
# print('point:', bmi_point, type(bmi_point))
# print('signal:', bmi_signal, type(bmi_signal))
# print('####################')
