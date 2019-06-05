import sys

sex = input('Input sex of a patient(m/f): ')
while sex != 'm' and sex != 'f':
    print('Not correct input. Try one more time.')
    sex = input('Input sex of a patient(m/f): ')

age = int(input('Input age of a patient (years): '))

def age_checker(age):
    if age <0:
        print('Некоректний тип данних.')
        sys.exit(1)
    elif age <= 2:
        print('\n Вік пацієнта занадто малий. Використовуйте кліренс інуліну для визначення ШКФ!')
        sys.exit(1)
    elif age <= 18:
        print('\n Будьте уважними! Дані про ШКФ можуть бути не точними, через неповноліття пацієнта.')
    
   
if age > 2:
    weight = int(input('Input weight of a patient (kg): '))
#creatinine = int(input('Input creatinine of a patient (μmol/L): '))
    scr = int(input('Input serum creatinine of a patient (μmol/L): '))

def ckd_epi(age, weight, creatinine):
    men = ((140 - age) * 1.23 * weight) / creatinine
    print('CKD-EPI: {}'.format(men))

'''The CKD-EPI equation, expressed as a single equation, is:

GFR = 141 * min(Scr/κ,1)α * max(Scr/κ, 1)-1.209 * 0.993Age * 1.018 [if female] * 1.159 [if black]'''

#1 mg/dL  =  	  88.4 µmol/L
#Scr is serum creatinine (mg/dL), κ is 0.7 for females and 0.9 for males, α is -0.329 for females and -0.411 for males, min indicates the minimum of Scr/κ or 1, and max indicates the maximum of Scr/κ or 1.

if sex == 'm':
    patient_sex = 'male'
elif sex == 'f':
    patient_sex = 'female'


def gfr_count(scr, age):
    '''CKD-EPI Calculator for Adults
    
Input variables:
1. scr is serum creatinine in µmol/L,
2. Age (in years)
    
Calculated variables:
1. k = 79.6 for male, and 61.9 for female
2. α = -0.411 for male and -0.329 for female 
    
minimal indicates the minimum of serum_creatinine/κ or 1, and
maximus indicates the maximum of serum_creatinine/κ or 1'''
    if sex == 'm':
        k = 79.6
        α = -0.411
    elif sex == 'f':
        k = 61.9
        α = -0.329
    
    minimal = min((scr/k), 1)
    maximus = max((scr/k), 1)

    gfr_male_white = 141 * (minimal ** α) * (maximus ** -1.209) * (0.993 ** age)
    
    gfr_female_white = gfr_male_white * 1.018
    gfr_male_black = gfr_male_white * 1.159 # Not in use
    
    gfr_female_black = gfr_female_white * 1.159 # Not in use

    

    if sex == 'm':
        gfr = gfr_male_white
    elif sex == 'f':
        gfr = gfr_female_white

    return gfr

def renal_failure(gfr):
    '''Determines the degree of renal failure by Glomerular Filtration Rate '''

    mark = '\n Якщо у хворого має місце ШКФ, що відповідає стадіям І або ІІ, але не має маркерів ураження нирок, діагноз ХХН не встановлюють.'

    if sex == 'm' and age <= 40 and 100 <= gfr <= 130:
        disease = 'Нормальна ШКФ для чоловіків віком до 40 років.'
    elif sex == 'm' and gfr > 130:
        disease = 'Підвищена ШКФ для чоловічої статі.'
    elif sex == 'f' and gfr > 120:
        disease = 'Підвищена ШКФ для жіночої статі.'
    elif sex == 'f' and age <= 40 and 90 <= gfr <= 120:
        disease = 'Нормальна ШКФ для жінок віком до 40 років.'
    elif gfr >= 90:
        disease = 'Нормальна або підвищена ШКФ. ХХН І стадії.'
        disease += mark
    elif gfr >= 60:
        disease = 'Помірно знижена ШКФ. ХХН ІІ стадії.'
        disease += mark
    elif gfr >= 30:
        disease = 'Середній ступінь зниження ШКФ. Початкова ниркова недостатність. ХХН ІІІ стадії.'
    elif gfr >= 15:
        disease = 'Значний ступінь зниження ШКФ. Виражена ниркова недостатність. ХХН ІV стадії.'
    elif gfr < 15:
        disease = 'Термінальна ниркова недостатність. ХХН V стадії. '

    return disease

def main():
    age_checker(age)
    #except:
    gfr_count(scr, age)
    print('Your patient: \n', 'Sex: {}'.format(patient_sex),
    'Age: {} years'.format(age), 
    'Serum creatinine: {} μmol/L \n'.format(scr), 
    'CKD-EPI is: {}'.format(gfr_count(scr, age)), sep='\n')

    print(renal_failure(gfr_count(scr, age)))

if __name__ == "__main__":
    main()
