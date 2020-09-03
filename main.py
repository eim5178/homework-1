# Author: Evelyn Moore
# Collaborator:
course1_grade = input("Enter your course 1 letter grade: ")
course1_credit = float(input("Enter your course 1 credit: "))
if course1_grade == 'A' or course1_grade =='a':
  gp_course1 = 4.0
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'A-' :
  gp_course1 = 3.67
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'B+' :
  gp_course1 = 3.33
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'B' :
  gp_course1 = 3.0
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'B-' :
  gp_course1 = 2.67
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'C+' :
  gp_course1 = 2.33
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'C' :
  gp_course1 = 2.0
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'C-' :
  gp_course1 = 1.67
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'D' :
  gp_course1 = 1.0
  print (f"Grade point for course 1 is: {gp_course1}")
elif course1_grade == 'F' :
  gp_course1 = 0.0
  print (f"Grade point for course 1 is: {gp_course1}")
else:
  gp_course1 = 0.0
  print (f"Grade point for course 1 is: {gp_course1}")
course2_grade = input("Enter your course 2 letter grade: ")
course2_credit = float(input("Enter your course 2 credit: "))
if course2_grade == 'A' or course2_grade =='a':
  gp_course2 = 4.0
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'A-' :
  gp_course2 = 3.67
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'B+' :
  gp_course2 = 3.33
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'B' :
  gp_course2 = 3.0
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'B-' :
  gp_course2 = 2.67
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'C+' :
  gp_course2 = 2.33
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'C' :
  gp_course2 = 2.0
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'C-' :
  gp_course2 = 1.67
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'D' :
  gp_course2 = 1.0
  print (f"Grade point for course 2 is: {gp_course2}")
elif course2_grade == 'F' :
  gp_course2 = 0.0
  print (f"Grade point for course 2 is: {gp_course2}")
else:
  gp_course2 = 0.0
  print (f"Grade point for course 2 is: {gp_course2}")
course3_grade = input("Enter your course 3 letter grade: ")
course3_credit = float(input("Enter your course 3 credit: "))
if course3_grade == 'A' or course1_grade =='a':
  gp_course3 = 4.0
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'A-' :
  gp_course3 = 3.67
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'B+' :
  gp_course3 = 3.33
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'B' :
  gp_course3 = 3.0
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'B-' :
  gp_course3 = 2.67
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'C+' :
  gp_course3 = 2.33
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'C' :
  gp_course3 = 2.0
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'C-' :
  gp_course3 = 1.67
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'D' :
  gp_course3 = 1.0
  print (f"Grade point for course 3 is: {gp_course3}")
elif course3_grade == 'F' :
  gp_course3 = 0.0
  print (f"Grade point for course 3 is: {gp_course3}")
else:
  gp_course3 = 0.0
  print (f"Grade point for course 3 is: {gp_course3}")
GPA = float(gp_course1 * course1_credit + gp_course2 * course2_credit + gp_course3 * course3_credit)/(course1_credit + course2_credit + course3_grade)
print(f"Your GPA is: {GPA}")
