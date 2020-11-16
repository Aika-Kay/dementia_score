""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS,
        diabetes, TG, LDL-C, HDL-C, graduation, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """

# 仮のユーザデータ
# user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
#         'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcSmokingRisk(object):
    """ リスク要因「喫煙」の判定 """
    def __init__(self, id, smoking):
        self.id = id
        self.smoking = smoking

    def get_smoking_point(self):
        """ 喫煙の有無によりリスクポイントの取得 """
        if self.smoking == '吸っている':
            smoking_point = 1
        else:
            smoking_point = 0
        return smoking_point

    def get_smoking_signal(self):
        """ 信号で表記するための値取得 """
        sp = self.get_smoking_point()
        if sp == 0:
            smoking_signal = 0
        else:
            smoking_signal = 2
        return smoking_signal

#
# test = CalcSmokingRisk(user[0], user[19])
# smoking_point = test.get_smoking_point()
#
# print('########################')
# print('喫煙:', smoking_point, type(smoking_point))
# print('########################')