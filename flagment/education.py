""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS,
        diabetes, TG, LDL-C, HDL-C, education, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """

# 仮のユーザデータ
user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
        'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcEducationRisk(object):
    """ 教育歴によるリスクを算出 """

    def __init__(self, id, education):
        """ 初期化 """
        self.id = id
        self.education = education

    def get_education_point(self):
        """ 中学生までの教育歴はポイント加算 """
        if self.education == '中学校':
            education_point = 2
        else:
            education_point = 0
        return education_point


test = CalcEducationRisk(user[0], user[17])
education_point = test.get_education_point()
print('######################')
print('加算ポイント', type(education_point), education_point)
print('######################')