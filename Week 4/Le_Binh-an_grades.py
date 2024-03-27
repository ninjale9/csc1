mylist= [ 83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]
highest_grade= max(mylist)
lowest_grade= min(mylist)
average_grade= sum(mylist) / len(mylist)

print(f'{len(mylist)} students took the exams')
print(f'The highest grade was a {highest_grade}')
print (f'The lowest grade was a {lowest_grade}')
print(f'The average grade for the exam was a {average_grade}')

print()

Day1= { 'Mary', 'Jake', 'Sam', 'Alex', 'Percy', 'Jessica', 'Trent', 'Mahmoud'}
Day2= {'Jake', 'Sam', 'Alex', 'Percy', 'Mahmoud', 'Trent', 'Caleb','Zayne'}
\
both_days = Day1.union(Day2)
total_students= len(both_days)
both_classes = Day1.intersection(Day2)
one_day= Day1.symmetric_difference(Day2)


print(f'{total_students} students attended the classes ')
print(f'{both_classes} attended both class days')
print(f'{one_day} only attended class for 1 day')