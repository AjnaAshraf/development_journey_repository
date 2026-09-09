def common_divisor_of_2_num(num1,num2):

    minimum = min(num1,num2)

    for i in range(1,minimum+1):

        if num1 % i == 0 and num2 % i == 0 :
            
            print(i,end = " ")


common_divisor_of_2_num(8,4)

