print("Hello python world!")
first_name = "sukriti"
last_name = "mishra"
full_name = f"{first_name} {last_name}"
print(full_name)
first_name = "sukriti"
last_name = "mishra"
print(f"Hello,{full_name.title()}!")
first_name = "sukriti"
last_name = "mishra"
message = f"Hello, {full_name.title()}!"
print(message)
first_name = "sukriti"
last_name = "mishra"
message = f"Hello, {full_name.title()}!"
print(message)

print("Python")
print("\tPYTHON")
print("Languages:\nPython\nC\nJava")
print("Languages:\n\tPython\n\tC\n\tJava")

favorite_language = 'english '
favorite_language
favorite_language.rstrip()
print(favorite_language)
favorite_language = '  python  '
favorite_language.strip()
print()
 

bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)

message = f"My favorite bicycle is {bicycles[0].title()}."
print(message)
motorcycles= ['audi', 'honda', 'bmw', 'mercedes']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('subaru')
print(motorcycles)

magicians = ['alice', 'david','carolina', 'berry']
for magician in magicians:
	print(magician)

	print(f"{magician.title()}, that was a great trcik!")
	print(f"{magicians[1].title()}, that was my favorite.")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everone.")	
print(f"I can't wait to see your next trick, {magicians[2].title()}.\n")

for value in range(1, 5):
	print(value)

even_numbers = list(range(2, 20, 2))
print(even_numbers)

squares = []
for value in range(1, 20):
	square = value ** 2
	squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5]	
min(digits)

max(digits)
sum(digits)

numbers = []
for value in range(0, 20):
	sum = value + 1
	numbers.append(sum)
print(numbers)


odd_numbers = [value % 2 !=0 for value in range(0, 20)]
print(odd_numbers)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
	if num % 2 != 0:
		print(num, end = " ")



numbers = []
for value in range(3, 30):
	result = value * 3
	numbers.append(result)
print(numbers)

players = ['sachin', 'yuvraj', 'kohli', 'dhoni', 'gambhir']
print(players[0:3])
print(players[2:4])
print(players[:3])
print(players[2:])
print(players[-2:])
print()

cars = ['bmw', 'toyota', 'mercedes', 'honda', 'subaru']

for car in cars:
	if car == 'bmw':
		print(car.upper())

	else:
		print(car.title())

car = 'bmw'
car == 'bmw'
car

requested_topping = 'mushrooms'
if requested_topping != 'olives':
	print("pizza!")
if requested_topping == 'mushrooms':
	print("burger")

age = 17
age < 21


age = 25
if age < 4:
	print("your admission cost is $0.")
elif age < 18:
	print("your admission fee is $20.")
else:
	print("your admission fee is $30.")
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 15
else:
	price = 20

print(f"your admission cost is ${price}.")	

age = 90
if age < 5:
	price = 10
elif age < 25:
	price = 20

elif age < 65:
	price = 30
else:
	price = 40

print(f"your admission cost is ${price}.")	

age = 67
if age < 5:
	price = 0
elif age < 20:
	price = 10
elif age < 65:
	price = 20
elif age >= 65:
	price = 30
print(f"your admission fee is ${price}.")	

lst1 = [2, 3, 4, 5, 7, 8, 10]
lst2 = [3, 5, 11, 8, 12, 10,]
def intersection (list1, list2):
	lst3 = [value for value in lst1 if value in lst2] 
	return lst3
print(intersection(lst1, lst2))

import csv

def writeTallyScore(file_name):
	
	tally_scores = {}

	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if row[1] in tally_scores:
				tally_scores[row[1]] = tally_scores[row[1]] + int(row[2])
			else:
				tally_scores[row[1]] = int(row[2])

	with open('results.txt', mode='w') as output_file:
		writer = csv.writer(output_file, delimiter=',')
		for klass in tally_scores:
			writer.writerow([klass, tally_scores[klass]])

writeTallyScore('input.txt')


a = {}
a ={'color':'green', 'fruit':'mango'}
print(a['color'])
print(a['fruit'])
print(a)
a['color'] = 'yellow'
a['fruit'] = 'mango'
print(a)

b = {}
b = {'car': 'audi'}
print(f"my favorite car is {b['car']}.")
a = dict(one = 1, two = 2, three = 3)

b = {'one': 1, 'two': 2, 'three': 3}
a==b

z = {'fruit': 'banana', 'car': 'audi'}
z['fruit']
z['fruit'] = 'orange'
print(z)
z.keys()

z.keys()
z.values()
z.items()


a = 6
b = 7
print(a + b)

a = '6'
b = '7'
print(int(a)+int(b))


price  = 67

price = float(price)
if price >= 1.00:
	tax = 0.70
	print('tax rate is: '+ str(tax))
else:
	tax = 0
print('tax rate is: ' + str(tax))

x = 0 
while True:
	if x == 42:
		break
	x = x + 1
print(f"Count is {x}")

 


country = 'India'
province = 'Haryana'

if country == 'India':
	if province in('Karnataka', 'Delhi', 'Kerala'):
		tax = 0.05
	elif province == 'Haryana':
		tax = 0.13

	else:
		tax = 0.15
else:
	tax = 0.0

print(tax)


from array import array
scores = array('d')
scores.append(97)
scores.append(99)
print(scores)
print(scores[1])


names = ['sukriti', 'rahul', 'pihu', 'ted']
print(len(names))
names.insert(0, 'pandey')
names.sort()
print(names)
name = names[0::2]
print(name)


names = ['herry', 'berry', 'cherry', 'harry']
index = 2
while index < len(names):
	print(names[index])
	index = index + 1

	people = ['sukriti', 'mishra']

	for name in people:
		print(name)


from datetime import datetime
def print_time(first_name):
	print('first_name')
	print(datetime.now())
	print('well done')
	print()



first_name ='sukriti'
print_time('sukriti')

for x in range(0, 9):
	print(x)
print_time('task_completed')


def get_initial(name, force_uppercase=True):
	if force_uppercase:
		initial = name[0:1].upper()
	else:
		initial = name[0:1]
		return initial
first_name = 'Sukriti'	
first_name_initial = get_initial(first_name,False)

last_name = 'mishra'
last_name_initial = get_initial(last_name,True)

print(first_name_initial)

x = 10.0
y = (x < 100.0) and isinstance(x, float)


a = 100
b = 200
c = a and b
print(c)


x = -100
from math import sqrt
c = x > 0 and sqrt(x)
print(c)




c = 1 + 2** 3 * 4
print(c)


s = 'foo'
t = 'bar'
print('barf' in 2 * (s +t))



'hello'.isalpha()
'123'.isdigit()
c = 'some,csv,values'.split(',')
print(c)

name = 'sukriti'
machine = 'harry'
c = f'nice to meet you {name}. i am {machine}'
print(c)
python_course = True
java_course = False
c = int(python_course)
print(c)
c = int(java_course)
print(c)

number = 10
number += 5
print(number)


number = 7
if number == 5:
	print('number is 5')
else:
	print('number is NOT 5')


python_course = None
if python_course:
	print('value')

aliens_found = None
if aliens_found:
	print('NOT execute')	

number = 6
if number != 5:
	print('value')

python_course = False
if not python_course:
	print('not value')

number = 4
python_course = True
if number == 3 and python_course:
	print('value')


number = 4
python_course = True
if number == 3 or python_course:
	print('value')




for letter in "Python":     # break Example
   if letter == "h":
      break
   print(f"Current Letter: {letter}")


   x = 0
   while True:
   	if x == 10:
   		break
   	print(f'count is {x}')	
   	x += 1




l = [9, 10, 11]
print(max(l))




a = 1
b= 2
c = 3
if c > b and c > a:
	print(c)
elif b > a:
	print(b)
else:
	print(a)	

for i in range(10, 15, 3):
	print(i, end =',')



sampleset = {'jodi', 'a','harry'}
sampleset.add('pihu'[2])
print(sampleset)


x = 36 / 4 * (3 + 2) * 4 + 2
print(x)

def calculate(num1, num2=4):
	res = num1 * num2
	print(res)
calculate(6)




def Foo(x):
  if (x==1):
    return 1
  else:
    return x+Foo(x-1)
print(Foo(2))

language = ['P', 'y', 't', 'h', 'o', 'n']
print(language[:-4])



print((1, 2) + (3, 4))

names = "{1}, {2} and {0}".format('John', 'Bill', 'Sean')
print(names)



squares = {1:1, 2:4, 3:9, 4:16, 5:25}  
print(squares.pop(4))  
print(squares)




import re
sentence = 'Learn Python Programming'
test = re.match(r'(.*) (.*?) (.*)', sentence)
print(test.group())






x = 2
def foo(y):
	z = 5 
	print(locals())
	print(globals()['x']) 
	print(x, y, z)


foo(3) 

def print_twice(bruce):
   print(bruce)
   print(bruce)

def cat_twice(part1, part2):
   cat = part1 + part2
   print_twice(cat)
line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

def print_two(a, b):
	print("Arguments: {0} and {1}".format(a, b))
#print_two()
print_two(4,1)
#print_two (41)
print_two (a=4, b=1)
print_two(b=1, a=4)


def keyword_args(a, b=1, c='X', d=None):
	print("a:", a) 
	print("b:", b) 
	print("c:", c) 
	print("d:", d)
keyword_args(5)
keyword_args(a=5)
keyword_args(5, 8)	
keyword_args(5, 2, 0, "")

my_string = 'this is a python klass'
c = my_string[3]
print(c)

c = my_string[10:16]
print(c)
c = 'python klass'.find('klass')
print(c)


c = "  python klass   "
print(c.rstrip())


my_string = "This is a python class"
# print the numbers
for letter in my_string:
   print(letter, end=' ')


numbers = [ 1, 3, 5, 7, 9, 10, 11, 12, 3, 3, 3, 3]
print(numbers[1:-2])
numbers[-2] = 200
print(numbers)
c = numbers.clear()
print(c)



numbers = list(range(1, 15, 3))
for number in numbers:
	print(number)
for index, number in enumerate(numbers):
	print(index, number)




d = {'one': 1, 'two': 2, 'three': 3}
for key in d:
	print(key, d[key])
for key, value in d.items():
	print(key, value)





def sqrt(x):
   if not isinstance(x, (int, float)):
       raise TypeError("x must be numeric")
   elif x < 0:
       raise ValueError("x cannot be negative")
       x = 5
       print(sqrt(x))
   # do the real work here...


try:  
    a = 10/0
    print (a)
except ArithmeticError:  
        print ("Arithmetic exception raised." )
else:  
    print ("Success.")

    try:
    	a=10
    	b=20
    	assert a==b, "Value mismatch"
    except AssertionError as e:
    	print(e)

try:
   	something
except:
   	pass

def askForNumber ():
    while True:
        try:
            return int(input('Please enter a number: '))
        except ValueError:
            pass

def sqrt(x):
   if not isinstance(x, (int, float)):
       raise TypeError("x must be numeric")
   elif x < 0:
       raise ValueError("x cannot be negative")
       print(-5)

try:
	10 / 0
except ZeroDivisionError:
	print('not execute')


#for city in ["San Jose", "Redwood City", "Sunnyvale"]:
 # print(city)

 # for city in iter(["San Jose", "Redwood City", "Sunnyvale"]):
    #print(city)


   # do the real work here...               	
  	
    	
#age = -1
 
#while age <= 0:
	#try:
	# age = int(input("Enter your age in years:"))
	 #3if age <= 0:
	  #print("Your age must be positive")
	#except (ValueError, EOFError):
		#print("Invalid response")



def avg(numbers):
    assert len(numbers) != 0, 'Number list should not be empty'
    return round(sum(numbers)/len(numbers), 2)



numbers = [62, 65, 75]
print(avg(numbers))



numbers = [1, 3, 5, 7, 8, 9, 19, 11, 12, 13, 14]
c = numbers[1:-3]
print(c)



cities = [a, b, c, d, e]
d = iter(cities)
print(next(d))


#metaweather/api/location/2487956

class myclass:
	x = 5
print(myclass)

scores = [[77, 68, 86, 73],
          [96, 87, 89, 81],
          [70, 90, 86, 85]]
scores[2]



























 















	



 













	



















