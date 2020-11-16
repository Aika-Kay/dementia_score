""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS,
        diabetes, TG, LDL-C, HDL-C, graduation, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """

# 仮のユーザデータ
# user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
#         'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcActivityRisk(object):
    """ 運動量のリスクを計算する """
    
    def __init__(self, id, activity):
        self.id = id
        self.activity = activity

    def get_activity_point(self):
        user_activity = str(self.activity)
        if user_activity == '0 ~ 1回':
            activity_point = 1
        else:
            activity_point = 0
        return activity_point

    def get_activity_signal(self):
        ap = self.get_activity_point()
        if ap == 0:
            activity_signal =0
        else:
            activity_signal = 2
        return activity_signal
#
#
# test = CalcActivityRisk(user[0], user[18])
# activity_point = test.get_activity_point()
# print('########################')
# print('活動量:', activity_point, type(activity_point))
# print('########################')