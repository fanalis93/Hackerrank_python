#print("{0:.2f}".format(n))
n = int(input())
student_marks = {}
for _ in range(n):
    name, line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
# print(student_marks)
# print(scores)
query_name = input()
sum=0
#print(student_marks[query_name])
for x in student_marks[query_name]:
    sum += x
print("{0:.2f}".format(sum/3))
