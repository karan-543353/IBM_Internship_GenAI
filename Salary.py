file = open("Salary.txt", "w+")
cont = file.write(" Harnoor : 75000 \n Nidhish : 45000 \n Simran : 67000 \n gurmannat : 23000 \n Karan : 89000")
file.close()

file1= open("Salary.txt", "r")
salary_count = 0
for i in file1:
    name, salary = i.split(":")
    salary = int(salary.strip())
    if salary > 50000:
        salary_count += 1
        print(name , " has a high salary of", salary)
    else:
        print(name, "has a low salary of ", salary )
file1.close()

print(" The no. of Employees satisfy the condition are : ", salary_count)

