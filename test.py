num_list = [5,0,2]

for ele in num_list:
    try:
        result = 5/ele
        print("Result 5/:",ele," is ",result)
    except ZeroDivisionError:
        print("Oops! An error")