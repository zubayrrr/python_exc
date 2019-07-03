#exercise one

print "hello world"
print "hello again"
print "I like typing this"
print "This is fun"
print "Yay! I'm priniting"
print "I'd much rather you not"
print "I said do not touch this"

#exercise two

#welcome to comments

#print "this is ignored by python because its written after a pound(#)"
#everything written after # is ignored by python
print "this is not a comment this is not ignored by python"
print "this will run"

#numbers and math

print "I will now count my chickens: "
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs: "
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that  3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7

print "What is 3 + 2 ?", 3 + 2

print "What is 5 - 7 ?", 5 - 7

print "Oh, that's why it's false."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal ?", 5 <= -2

#exercise 4

#variables and names

cars = 100
space_in_cars = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven = space_in_cars
average_passenger_per_car = passengers / cars_driven

print 'There are ', cars, 'cars available.'
print 'There are only', drivers, 'drivers available.'
print "There will be ", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "we need to put about", average_passenger_per_car, "in each car."

#exercise 5

#more variable, python formatters %s, %d, %r

my_name = "Zed You Be A Why Are"
my_age = 19 #not a lie
my_height  = 74
my_weight = 180
my_eyes = "Brownish-black"
my_teeth = "yellowish-white"
my_hair = "Black"

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "he's %d pounds heavy" % my_weight
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)


# additional practice 

print"hello"
print "." * 10

#this will be escaped by the python because its a comment

print "hello world" #I'm using "print" to print out hello world

print 10 + 2
eggs = 3
name = "zubayr ali"
print "i've %d eggs."% eggs
print "My name is " + name + " ."
print "my name is %s, I've %d eggs" % (name, eggs)


x = "there are %d types of people," % 10
#print x
binary = "binary"
do_not = "don't"
y = "those who understand %s and those who %s" % (binary, do_not)

print x + y

print 12 * 2
print 3 - 7
print 9 % 3
print 5 < 3
print 8 > 2
