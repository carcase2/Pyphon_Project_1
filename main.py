# 2023-01-06 first project by kkd

import random
import time
start = time.time()  # 시작 시간 저장

print("숫자 야구 게임 입니다. by kkd")
print("3자리 야구 게임 입니다.")

# 전역 변수 설정

global input_Number
global temp
global try_Count
global check_Same
global homerun_Number
global s_Count
global b_Count

start_Numer = 1
end_Number = 9
check_Same = False
try_Count = 0
temp = [1, 2, 3]
homerun_Number = [0, 0, 0]
s_Count = 0
b_Count = 0

# 3자리 야구임을 확인하기 위한 변수값을 1000으로 함
input_Number = 1000

# 숫자 분리하는 함수
def check_Number_1(number):
    # print("숫자 분리하는 함수")
    temp[0] = int(number/100)
    temp[1] = int((number - temp[0]*100)/10)
    temp[2] = int((number - temp[0]*100 - temp[1] * 10))

# 동일한 숫자가 있는 확인 하는 함수
def check_Number_2():
    if temp[0] == temp[1]:
        return True
    if temp[0] == temp[2]:
        return True
    if temp[1] == temp[2]:
        return True
    else:
        return False

def check_Number_3():
    global b_Count
    global s_Count
    
    for i in range(3):
        for j in range(3):
            if(homerun_Number[i] == temp[j]):
                
                if(i==j):
                    s_Count = s_Count + 1
                else:
                    b_Count = b_Count + 1
while(1):
    homerun_Number[0] = random.randint(start_Numer, end_Number)
    homerun_Number[1] = random.randint(start_Numer, end_Number)

    while(homerun_Number[0] ==homerun_Number[1]):
        homerun_Number[1] = random.randint(start_Numer, end_Number)
    
    homerun_Number[2] = random.randint(start_Numer, end_Number)
    while((homerun_Number[0] ==homerun_Number[2]) or (homerun_Number[1] ==homerun_Number[2])):
        homerun_Number[2] = random.randint(start_Numer, end_Number)
    break

print("맞춰야 하는 숫자는: ", homerun_Number)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
while (s_Count != 3):
    while input_Number >= 1000:
        input_Number = int(input("3자리 입력하세요? (1~9)"))
        b_Count = 0
        s_Count = 0
        check_Number_1(input_Number)
        check = check_Number_2()
        if check == True:
            input_Number = 2000
            break
        else:
            try_Count = try_Count + 1
            check_Number_3()
            input_Number = 2000
            if(s_Count == 0 and b_Count == 0):
                print("                       시도횟수 : ",try_Count,"입력한 숫자 :",temp,"************OUT************")
            else:
                print("                       시도횟수 : ",try_Count,"입력한 숫자 :",temp, s_Count,"Strike ", b_Count,"Ball")
            break
print(try_Count,"번만에 맞췄군")