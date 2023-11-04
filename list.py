
import random
myList=[]

Numberoflist=int(input("How Much Number u Want Be in List? :"))
range1=int(input("Enter Fist Range :"))
range2=int(input("Enter End Range : "))
my_list = list(random.sample(range(range1, range2), Numberoflist))

print(my_list)

