# Everythings in the python is an 'Object'
# Ex:-
# l=[1,2,3]
# l.upper()
# error:-
# Traceback (most recent call last):
#   File "c:\Users\hello\Desktop\OOPs-in-python\Basic-OOPs.py", line 4, in <module>
#     l.upper()
# AttributeError: 'list' object has no attribute 'upper'



# OOPs:-
#OOPs concept includes class,object,Encapsulation,Inheritance,Polymorphism,Abstraction.

# Class:-
# it is a blueprint,it explains how a object is behave.
# it have data or property or attributes,and function or behavior.
# ex:-car,  --data:-no of wheels,color,engine,brands
# ---behaviour;mileage,gps navigation.
# Basic Structure:-
# class Car:  #CamelCase
#      color='blue' #data
#      models='sports'  #data
#      def calculate_avg_speed(km,time):  #snake_case
        # some code
# 
 
# Objects:-
# Generality to specificity.
# Objects is the instance of the class. 
# The object is an entity that has a state and behavior associated with it. It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.

# bmw=Car()  #bmw is objects,Car is class


# Constructor:- it is special method ,it is called automatically when the objects of that class is created, constructor is not called manually.
# How to use it:-
# Those feature which are not given to user ,directly those method can be used in the constructor.It's control is not given to the user.