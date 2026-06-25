def calculate_hra(Basic_salary):
    Hra = (Basic_salary*20)/100
    return Hra
def calculate_da(Basic_salary):
    da = (Basic_salary*10)/100
    return da
def calculate_net_salary(Basic_salary):
    hra_val = calculate_hra(Basic_salary)
    da = calculate_da(Basic_salary)
    net_salary = Basic_salary + hra_val + da
    print("net salary is",net_salary)
    return net_salary
calculate_net_salary(19000)

