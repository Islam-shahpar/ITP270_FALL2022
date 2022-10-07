#!/bin/python3

#Task-1
subjects = ["physics", "calculus", "poetry", "history"]

#Task-2
grades = [98, 97, 85, 88]

#Task-3
gradebook = [[subjects[0], grades[0]],[subjects[1], grades[1]]] 

#Task-4
gradebook.append(["computer science", 100])

gradebook[2][1] = 90

gradebook[1].remove(97)

gradebook[1].append("Pass")

last_semester_gradebook = [["Subject1", 90]]

full_gradebook = last_semester_gradebook + gradebook

print(gradebook)

print(full_gradebook)
