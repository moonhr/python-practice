test_model = input("어떤 타입을 검사할까요? : ")

def typeTest():
    try :
        print(int(type(test_model)))
    except :
        print(float(type(test_model)))
        try : 
            print(str(type(test_model)))
        except :
            print("타입몰라")
print(typeTest())



# test_model = input("어떤 타입을 검사할까요? : ")
# print(type(test_model) ,"입니다.")
