'''Marks = [12,13,43,54,67,34, "subham tewatia",True,False, "vicky", -23, 4.56,-6.8 ]
print(Marks)
print(type(Marks))
print(Marks[2]) #43

#print(Marks[78]) #IndexError: list index out of range
#Slicing index
print(Marks[-3]) #54
print(Marks[3:]) #[12, 13, 43, 54, 67, 34, 'subham tewatia', True, False, 'vicky', -23, 4.56, -6.8]
print(Marks[3:3])#[]
print(Marks[:3])
print(Marks[-4::-1])
print(Marks[0:-1])'''

'''
#create the list of 6 exams score of your choosing
#print : the full list first score and the last score
#the middle 4 scores (Slice ) , and the total count
scores =[34,30,45,43,50,48,38,36]
print (scores)
print (scores[0])
print (scores[-1])
print(len(scores))
print (scores[1:7])

# ask the user for 5 marks one at a time and store  them in a list
# use append in this and append help to add a value in the last

lst = []
print (lst)
for i in range(1,5):
     marks = int(input("enter marks: "))
     lst.append(marks)
     print (lst)


# functions
print (lst)
print (type(lst))
print (max(lst))
print (min(lst))
print (sum(lst))
print(reversed(lst))

#wap to n number of values  in a list
# print all even number nos
# count all odd nos
Size = int(input("enter size: "))
lst=[]
for i in range(Size):
    marks = int(input("enter marks: "))
    lst.append(marks)

for i in range(Size):
    if lst[i]%2==0:
        print (lst[i])

# without using index value
ctr=0
for i in lst:
    if 1 % 2 == 0:
        ctr +=1
# Wap to accept n no values in a list  and ask the user which value has to be remove
# remove all is instances
#Wap program to accept n no of user from the teacher , how many student of you except name and mark parallel and display al the students name those who have passed the exam
names = []
marks = []

for i in range(n):
    name = input("  Enter name: ")
    mark = float(input("  Enter mark: "))
    names.append(
        name)  # dono me saath-saath append
    marks.append(
        mark)  # isliye index match karta hai

for i in range(len(names)):
    if marks[i] >= PASS_MARK:

     print(names[i], "-", marks[i], "marks"),'''

#sets
#numbers = { "Man","child","boy", "father","223"}
#print(numbers)
#print(type(numbers))
#print(len(numbers))

a = {1,2,3,4,4,4}
b = {1,2,4,5,6,7,8}
print(a|b)# Union
print(a&b)# Intersection
print(a^b)# Intersection compliment
print(a-b)# Difference
print(b-a)


numbers= (1,2,3,4,4,4,1,2,3,4,5,6,7,8)
print(numbers)
unnique = set(numbers)
print(unnique)

