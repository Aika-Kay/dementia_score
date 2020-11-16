from datetime import date

from dateutil.relativedelta import relativedelta


""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS, 
        diabetes, TG, LDL-C, HDL-C, graduation, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """

# 仮のユーザデータ
# user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
#         'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcAgeRisk(object):
    """ アンケート結果より、年齢リスクを計算する """
    def __init__(self, id, birth_year, birth_month, birth_day):
        """ 初期化 """
        self.id = id
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day

    def get_full_birthday(self):
        """ 生年月日を取得 """
        year = self.birth_year
        month = self.birth_month
        day = self.birth_day
        birthday = date(year, month, day)
        return birthday

    def get_age(self):
        """ 今日の日付と生年月日から年齢を取得 """
        today = date.today()
        birthday = self.get_full_birthday()
        # 経過時間を計算
        dy = relativedelta(today, birthday)
        # 年齢だけ取り出し
        age = dy.years
        return age

    def get_age_point(self):
        """ 年齢のリスクを取得 """
        age = self.get_age()
        # 年齢によって場合わけ
        if age < 47:
            age_point = 0
        elif age < 54:
            age_point = 3
        else:
            age_point = 4
        return age_point

# test = CalcAgeRisk(user[0], int(user[2]), int(user[3]), int(user[4]))
# full_birthday = test.get_full_birthday()
# get_age = test.get_age()
# age_point= test.get_age_point()
# print('######################')
# print(full_birthday)
# print('年齢', type(get_age), get_age)
# print('加算ポイント', type(age_point),age_point)
# print('######################')
