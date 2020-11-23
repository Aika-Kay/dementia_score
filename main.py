from flagment.activity import CalcActivityRisk
from flagment.birthday import CalcAgeRisk
from flagment.blood_pressure import CalcBloodPressureRisk
from flagment.bmi import CalcBmiRisk
from flagment.diabetes import CalcDiabetesRisk
from flagment.education import CalcEducationRisk
from flagment.smoking import CalcSmokingRisk
from flagment.t_chol import CalcCholesterolRisk
from flagment.mental import CalcMentalRisk

user = ['HB00003', '栢森藍佳', '1961', '11', '29', '19611129', '165.4', '88.2', '140', '86', 'ある', '6.7', '140',
        'ある', '100', '145', '40', '専門学校・大学', '0 ~ 1回', '吸っていない', '4', '3', '2', '0', '3']
# 最終成果物：user_list = [ID, name, dementia_risk, activity_signal, BMI_signal, diabetes_signal, T-CHOL_signal,
#                         smoking_signal, BP_signal, mental_signal]

# 各メソッドに必要なパラメーターを指定
param_act = [user[0], user[18]]
param_age = [user[0], int(user[2]), int(user[3]), int(user[4])]
param_bmi = [user[0], float(user[6]), float(user[7])]
param_cho = [user[0], float(user[14]), float(user[15]), float(user[16])]
param_dia = [user[0], float(user[11]), float(user[12]), user[13]]
param_edu = [user[0], user[17]]
param_smo = [user[0], user[19]]
param_blo = [user[0], float(user[8]), float(user[9]), user[10]]
param_men = [user[0], int(user[20]), int(user[21]), int(user[22]), int(user[23]), int(user[24])]

# 最終出力するものをuser_listに格納していく
user_list = [user[0], user[1]]

# 各クラスを呼び出し
user_act = CalcActivityRisk(*param_act)
user_age = CalcAgeRisk(*param_age)
user_bmi = CalcBmiRisk(*param_bmi)
user_bp = CalcBloodPressureRisk(*param_blo)
user_cho = CalcCholesterolRisk(*param_cho)
user_dm = CalcDiabetesRisk(*param_dia)
user_edu = CalcEducationRisk(*param_edu)
user_smo = CalcSmokingRisk(*param_smo)
user_men = CalcMentalRisk(*param_men)

# dementia_riskをアペンドをを計算するために.get_point()を読み込んでいく
act_p = user_act.get_activity_point()
age_p = user_age.get_age_point()
bmi_p = user_bmi.get_bmi_point()
bp_p = user_bp.get_bp_point()
cho_p = user_cho.get_cholesterol_point()
edu_p = user_edu.get_education_point()
smo_p = user_smo.get_smoking_point()
men_p = user_men.get_mental_point()

dementia_p = act_p + age_p + bmi_p + bp_p + cho_p + edu_p + smo_p + men_p
user_list.append(dementia_p)

# 活動量表記をアペンド
act_sig = user_act.get_activity_signal()
user_list.append(act_sig)
# BMI表記をアペンド
bmi_sig = user_bmi.get_bmi_signal()
user_list.append(bmi_sig)
# 血糖値表記をアペンド
dm_sig = user_dm.get_diabetes_signal()
user_list.append(dm_sig)
# 総コレステロール表記をアペンド
cho_sig = user_cho.get_chol_signal()
user_list.append(cho_sig)
# 喫煙表記をアペンド
smo_sig = user_smo.get_smoking_signal()
user_list.append(smo_sig)
# 血圧表記をアペンド
bp_sig = user_bp.get_bp_signal()
user_list.append(bp_sig)
# メンタル表記をアペンド
men_sig = user_men.get_mental_signal()
user_list.append(men_sig)

print('user_list:', user_list)


