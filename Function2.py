def calculate_total(marks):
    t = sum(marks)
    return t
def calculate_percentage(total,num_subjects):
    per = (total/num_subjects)
    return per
def assign_grades(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75 and percentage <= 90:
        return "B"
    elif percentage >= 60 and percentage <= 75:
        return "C"
    elif percentage >= 40 and percentage <= 60:
        return "D"
    else:
        return "E"
marks_lst = []
for i in range(5):
    m = int(input(f"enter the marks for subject {i+1} here - "))
    marks_lst.append(m)
total_marks = calculate_total(marks_lst)
print(" Total Marks are : ", total_marks)
num_subjects = len(marks_lst)
percents = calculate_percentage(total_marks,num_subjects)
print(" Percentage :- ", percents)
grade = assign_grades(percents)
print(" Final Grade is :- ", grade)
