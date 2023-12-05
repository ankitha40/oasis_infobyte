calcuate = True
while calcuate:
    user_height = float(input('please enter your height:'))
    user_weight = float(input('please enter your weight:'))
    bmi = user_weight/(user_height*user_height)
    if bmi<18.5 :
        print(f'you are underweight and your bmi is {bmi}')
    elif bmi <24.9:
        print(f'you are normalweight and your bmi is {bmi}')
    elif bmi<29.9:
        print(f'you are overweight and your bmi is {bmi}')
    elif bmi<34.9:
        print(f'you are mildly obese and your bmi is {bmi}')
    elif bmi<39.9:
        print(f'you are moderately obese and your bmi is {bmi}')
    else:
       print(f'you are highly obese and your bmi is {bmi}')
    answer = input('Do you want to continue?(y/n)')
    if answer == 'y':
        calcuate = True
    else:
        calcuate = False
