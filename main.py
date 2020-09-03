#Author: Evelyn Moore eim5178@psu.edu
#Collaborators: none
calc_num = 0
total_course_credit = 0 
for i in range (3):
  course_grade = input(f"Enter your course {i+1} letter grade: ")
  course_credit = input(f"Enter your course {i+1} credit: ")
  course_credit = float(course_credit)
  if course_grade == 'A' :
    gp_course = float(4.0)
    print (f"Grade point for course {i+1} is: {gp_course}")
  elif course_grade == 'A-' :
    gp_course = float(3.67)
    print (f"Grade point for course {i+1} is: {gp_course}")
  elif course_grade == 'B+' :
    gp_course = float(3.33)
    print (f"Grade point for course {i+1} is: {gp_course}")
  elif course_grade == 'B' :
    gp_course = float(3.0)
    print (f"Grade point for course {i+1} is: {gp_course}")
  elif course_grade == 'B-' :
    gp_course = float(2.67)
    print (f"Grade point for course {i+1} is: {gp_course}")
  elif course_grade == 'C+':
    gp_course = float(2.33)
    print (f"Grade point for course {i+1} is: {gp_course}")
  elif course_grade == 'C' :
    gp_course = float(2.0)
    print (f"Grade point for course {i+1} is: {gp_course}")
  elif course_grade == 'D' :
    gp_course = float(1.0)
    print (f"Grade point for course {i+1} is: {gp_course}")
  elif course_grade == 'F' :
    gp_course = float(0.0)
    print (f"Grade point for course {i+1} is: {gp_course}")
  else:
    gp_course = float(0.0)
    print (f"Grade point for course {i+1} is: {gp_course}")
  calc_num = course_credit * gp_course + calc_num
  total_course_credit = total_course_credit + course_credit
calc_total = calc_num/total_course_credit
print(f"Your GPA is: {calc_total}")