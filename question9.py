# Question 9
# 1lb = 0.453592kg
number_of_students = int(input("Enter number of students: "))
weight_of_students_lbs = list()  # to store weights in lbs
weight_of_students_kgs = list()  # to store weights in kgs

for each in range(number_of_students):
    weight_lb = int(input("Enter weight of {} student in lbs: ".format(each + 1)))
    weight_of_students_lbs.insert(each, weight_lb)
    # converting lbs to kg and adding to separate list
    weight_kg = float("%.2f" % (weight_lb * 0.453592))
    weight_of_students_kgs.insert(each, weight_kg)

print("weight of students in lbs: ", weight_of_students_lbs)
print("weight of students in kgs: ", weight_of_students_kgs)