import math
import pandas as pd
def woe_iv_gender(data):

    attrition = data[(data['Attrition'] == 'Yes')]
    no_attrition = data[(data['Attrition'] == "No")]
    number_with_feature1 = len(attrition[attrition["Gender"]== "Male"]) #Attririon = Yes, Gender = Male
    number_with_feature2 = len(attrition[attrition["Gender"]== "Female"]) #Attririon = Yes, Gender = Female
    number_without1 = len(no_attrition[no_attrition["Gender"]== "Male"]) #Attririon = No, Gender = Male
    number_without2 = len(no_attrition[no_attrition["Gender"]== "Female"]) #Attririon = No, Gender = Female

    # for gender = Male:

    x_dw = number_with_feature1/ len(attrition)
    x_up = number_without1/ len(no_attrition)
    woe_men = math.log1p(x_up/x_dw)


    # for gender = Female:

    x_dw2 = number_with_feature2/ len(attrition)
    x_up2 = number_without2/ len(no_attrition)
    woe_women = math.log1p(x_up2/x_dw2)


    # calculating IV:

    iv_men = (x_up - x_dw) * woe_men
    iv_women = (x_up2 - x_dw2) * woe_women
    iv = iv_men + iv_women

    return iv

def woe_iv_edu(data):
    attrition = data[(data['Attrition'] == 'Yes')]
    no_attrition = data[(data['Attrition'] == "No")]
    number_with_feature1 = len(attrition[attrition["Education"] == 1]) #Attririon = Yes, edu = 1
    number_with_feature2 = len(attrition[attrition["Education"]== 2])#Attririon = Yes, edu = 2
    number_with_feature3 = len(attrition[attrition["Education"]== 3])#Attririon = Yes, edu = 3
    number_with_feature4 = len(attrition[attrition["Education"]== 4])#Attririon = Yes, edu = 4
    number_with_feature5 = len(attrition[attrition["Education"]== 5])#Attririon = Yes, edu = 5

    number_without1 = len(no_attrition[no_attrition["Education"] == 1]) #Attririon = No, edu = 1
    number_without2 = len(no_attrition[no_attrition["Education"]== 2]) #Attririon = No, edu = 2
    number_without3 = len(no_attrition[no_attrition["Education"]== 3]) #Attririon = No, edu = 3
    number_without4 = len(no_attrition[no_attrition["Education"]== 4]) #Attririon = No, edu = 4
    number_without5 = len(no_attrition[no_attrition["Education"]== 5]) #Attririon = No, edu = 5

    #education = 1

    x_dw1 = number_with_feature1/ len(attrition)
    x_up1 = number_without1/ len(no_attrition)
    woe1 = math.log1p(x_up1/x_dw1)

     #education = 2

    x_dw2 = number_with_feature2/ len(attrition)
    x_up2 = number_without2/ len(no_attrition)
    woe2 = math.log1p(x_up2/x_dw2)

     #education = 3

    x_dw3 = number_with_feature3/ len(attrition)
    x_up3 = number_without3/ len(no_attrition)
    woe3 = math.log1p(x_up3/x_dw3)

     #education = 4

    x_dw4 = number_with_feature4/ len(attrition)
    x_up4 = number_without4/ len(no_attrition)
    woe4 = math.log1p(x_up4/x_dw4)

     #education = 5

    x_dw5 = number_with_feature5/ len(attrition)
    x_up5 = number_without5/ len(no_attrition)
    woe5 = math.log1p(x_up5/x_dw5)


    # calculating IV:

    iv1 = (x_up1 - x_dw1) * woe1
    iv2 = (x_up2 - x_dw2) * woe2
    iv3 = (x_up3 - x_dw3) * woe3
    iv4 = (x_up4 - x_dw4) * woe4
    iv5 = (x_up5 - x_dw5) * woe5
    iv = iv1+iv2+iv3+iv4+iv5


    return iv

def woe_iv_edufield(data):
    attrition = data[(data['Attrition'] == 'Yes')]
    no_attrition = data[(data['Attrition'] == "No")]
    number_with_feature = list()
    number_without = list()
    iv = 0

    number_with_feature.append(len(attrition[attrition["EducationField"] == 'Life Sciences']))
    number_with_feature.append(len(attrition[attrition["EducationField"]== 'Other']))
    number_with_feature.append(len(attrition[attrition["EducationField"]== "Medical"]))
    number_with_feature.append(len(attrition[attrition["EducationField"]== 'Marketing']))
    number_with_feature.append(len(attrition[attrition["EducationField"]== "Technical Degree"]))
    number_with_feature.append(len(attrition[attrition["EducationField"]== "Human Resources"]))

    number_without.append(len(no_attrition[no_attrition["EducationField"] == 'Life Sciences']))
    number_without.append(len(no_attrition[no_attrition["EducationField"]== 'Other']))
    number_without.append(len(no_attrition[no_attrition["EducationField"]== "Medical"]))
    number_without.append(len(no_attrition[no_attrition["EducationField"]== 'Marketing']))
    number_without.append(len(no_attrition[no_attrition["EducationField"]== "Technical Degree"]))
    number_without.append(len(no_attrition[no_attrition["EducationField"]== "Human Resources"]))


    for i in range(5):
        x_dw = number_with_feature[i]/len(attrition)
        x_up = number_without[i]/len(no_attrition)
        woe = math.log1p(x_up/x_dw)
        iv += (x_up - x_dw) * woe

    return(iv)

def woe_iv_department(data):

    attrition = data[(data['Attrition'] == 'Yes')]
    no_attrition = data[(data['Attrition'] == "No")]
    number_with_feature = list()
    number_without = list()
    iv = 0

    number_with_feature.append(len(attrition[attrition["Department"]== "Sales"]))
    number_with_feature.append(len(attrition[attrition["Department"]== "Research & Development"]))
    number_with_feature.append(len(attrition[attrition["Department"]== "Human Resources"]))

    number_without.append(len(no_attrition[no_attrition["Department"]== "Sales"]))
    number_without.append(len(no_attrition[no_attrition["Department"]== "Research & Development"]))
    number_without.append(len(no_attrition[no_attrition["Department"]== "Human Resources"]))

    for i in range(3):
        x_dw = number_with_feature[i]/len(attrition)
        x_up = number_without[i]/len(no_attrition)
        woe = math.log1p(x_up/x_dw)
        iv += (x_up - x_dw) * woe

    return iv



with open('/Users/kseniayakunina/Downloads/WA_Fn-UseC_-HR-Employee-Attrition.csv', newline='') as csvfile:
    data = pd.read_csv(csvfile, delimiter=",")
    no_attrition = data[(data['Attrition'] == "No")]
    print(woe_iv_department(data))




