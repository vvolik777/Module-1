students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_students=sorted(students)
print(sort_students)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_1=[sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
          sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
          sum(grades[4])/len(grades[4])]
print(grades_1)
student_grades={sort_students[i]: grades_1[i] for i in range(len(sort_students))}
print(student_grades)

#так же можно через функцию zip
#dict1 = dict(zip(sort_students, grades_1))
#print(dict1)
