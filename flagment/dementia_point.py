from flagment.activity import CalcActivityRisk as Activity
from flagment.birthday import CalcAgeRisk as Age

user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
        'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


# 最終成果物：user_list = [ID, name, dementia_risk, activity_signal, BMI_signal, BS_signal, T-CHOL_signal,
#                         smoking_signal, BP_signal, mental_signal]


class ImportAgePoint(Age):
    def __init__(self, id, birth_year, birth_month, birth_day):
        super().__init__(id, birth_year, birth_month, birth_day)

    def import_age_point(self):
        age_point = self.get_age_point()
        return age_point


test = ImportAgePoint(user[0], int(user[2]), int(user[3]), int(user[4]))
dp = test.calc_dementia_point()
print(dp)
