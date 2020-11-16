""" 読み込むCSVデータについて
user = [ID, name, birth_year, birth_month, birth_day, birthday, height, weight, SBP, DBP, highBP, HbA1c, FBS,
        diabetes, TG, LDL-C, HDL-C, graduation, activity, smoking, WHO-1, WHO-2, WHO-3, WHO-4, WHO-5] """
# 仮のユーザデータ
# user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
#         'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']


class CalcBloodPressureRisk(object):
    """ 血圧によるリスクを判定 """
    def __init__(self, id, sbp, dbp, high_bp):
        """ 初期化 """
        self.id = id
        self.sbp = sbp
        self.dbp = dbp
        self.high_bp = high_bp

    def calc_bp_point(self):
        if (self.sbp >= 140
                or self.high_bp == 'ある'):
            bp_point = 1
        else:
            bp_point = 0
        return bp_point

    def get_bp_signal(self):
        bp_p = self.calc_bp_point()
        if bp_p == 0:
            if (self.sbp < 130
                    or self.dbp < 85):
                bp_signal = 0
            else:
                bp_signal = 1
            return bp_signal
        else:
            bp_signal = 2
        return bp_signal