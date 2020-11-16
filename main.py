from flagment.activity import CalcActivityRisk
from flagment.blood_pressure import CalcBloodPressureRisk
from flagment.bmi import CalcBmiRisk
from flagment.diabetes import CalcDiabetesRisk
from flagment.smoking import CalcSmokingRisk
from flagment.t_chol import CalcCholesterolRisk
from flagment.mental import CalcMentalRisk

user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
        'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']
# 最終成果物：user_list = [ID, name, dementia_risk, activity_signal, BMI_signal, diabetes_signal, T-CHOL_signal,
#                         smoking_signal, BP_signal, mental_signal]

user_list = [user[0], user[1]]

# dementia_riskをアペンド

# 活動量表記をアペンド
user_act = CalcActivityRisk(user[0], user[18])
act_sig = user_act.get_activity_signal()
user_list.append(act_sig)
# BMI表記をアペンド
user_bmi = CalcBmiRisk(user[0], float(user[6]), float(user[7]))
bmi_sig = user_bmi.get_bmi_signal()
user_list.append(bmi_sig)
# 血糖値表記をアペンド
user_dm = CalcDiabetesRisk(user[0], float(user[11]), float(user[12]), user[13])
dm_sig = user_dm.get_diabetes_signal()
user_list.append(dm_sig)
# 総コレステロール表記をアペンド
user_chol = CalcCholesterolRisk(user[0], float(user[14]), float(user[15]), float(user[16]))
chol_sig = user_chol.get_chol_signal()
user_list.append(chol_sig)
# 喫煙表記をアペンド
user_smo = CalcSmokingRisk(user[0], user[19])
smo_sig = user_smo.get_smoking_signal()
user_list.append(smo_sig)
# 血圧表記をアペンド
user_bp = CalcBloodPressureRisk(user[0], float(user[8]), float(user[9]), user[10])
bp_sig = user_bp.get_bp_signal()
user_list.append(bp_sig)
# メンタル表記をアペンド
user_men = CalcMentalRisk(user[0], int(user[20]), int(user[21]), int(user[22]), int(user[23]), int(user[24]))
men_sig = user_men.get_mental_signal()
user_list.append(men_sig)

print('user_list:', user_list)


