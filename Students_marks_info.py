def cal_marks(marks):
    s = sum(marks)
    return s
def cal_per(total):
  return (total/500)*100

def assign_grades(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75 and percentage <=90:
        return "B"
    elif percentage >= 60 and percentage < 75:
        return "C"
    elif percentage >= 40 and percentage < 60:
        return "D"
    else:
        return "F"
def display_students(roll_no, info):
  """  Details of Students---- """
  print('Roll no. : ', roll_no)
  print('Name : ', info['name'])
  print('total : ', info['total'])
  print('Marks : ', info['marks'])
  print('Percentage : ', info['percentage'])
  print('Grade : ', info['grade'])
def main():
  students = {}
  n = int(input('Enter the number of students : '))
  for i in range(n):
    roll_no = int(input('Enter the roll no. : '))
    name = input('Enter the name : ')
    marks_list = []
    for s in range(5):
      marks = int(input(f'Enter the marks for subject {s+1} : '))
      marks_list.append(marks)
    total = cal_marks(marks_list)
    percentage = cal_per(total)
    grade = assign_grades(percentage)
    students[roll_no] = {'name': name, 'marks': marks_list, 'total': total, 'percentage': percentage, 'grade': grade}

  for roll_no, info in students.items():
    display_students(roll_no, info)
  if students:
    topper_roll = max(students, key=lambda x: students[x]['percentage'])
    topper_name = students[topper_roll]['name']
    print(f'The topper is {topper_name} with a percentage of {students[topper_roll]["percentage"]}')
if __name__ == '__main__':
  main()