from flagment.activity import CalcActivityRisk as class_act
from flagment.birthday import CalcAgeRisk as class_age

user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
        'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']

param_age = [user[0], int(user[2]), int(user[3]), int(user[4])]
param_act = [user[0], user[18]]

# 最終成果物：user_list = [ID, name, dementia_risk, activity_signal, BMI_signal, BS_signal, T-CHOL_signal,
#                         smoking_signal, BP_signal, mental_signal]


class CalcDementiaScore(object): #param_age=[,,,]
    def __init__(self, param_age):
        self.param_age = param_age

    def calc_dementia_score(self):
        age_point = class_age.get_age_point()
        # act_point = self.get_activity_point()
        dementia_point = age_point
        print('メソッド内', dementia_point)
        return dementia_point


test = CalcDementiaScore(param_age)
dp = test.calc_dementia_score()
print(dp)
