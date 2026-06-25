file = open("Attendence.txt ", "w+")
cont = file.write("Karan : P \n Harnoor : A \n Nidhish : P \n Simran : P \n Jaskaran : A ")
file.close()

file0 = open("Attendence.txt ", "r")
cont1 = file0.read()
print(cont1)
file0.close()

with open("Attendence.txt ", "r") as file1:
    for i in file1:
        ab_count = 0 
        name, attendence = i.split(":")
        name = name.strip()
        attendence = attendence.strip()
        if attendence == "A":
            print(name," is absent as the marked attendence is : ", attendence)
            ab_count += 1
        else:
            print(name," is present ")
file1.close()

print("Total No. of absent students are : ", ab_count)
