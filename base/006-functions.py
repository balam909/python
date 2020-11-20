print("To define a new function, you use 'def+<your_function_name>+(+<your_params_comma_separated>+)', example: 'def myFunction(param1, param2, ..., paramn)'")
# Creating a simple function and calling it
print("Creating simple function and calling it")
def sayHello(name):
	print("Hello",name)

sayHello("balam909")

# Defining a simple function with default params
print("Creating a simple function with default params")
def giveMeTwoNumbersAndAText(number1, number2, myText="This is my default text"):
	print("number1:",number1,"number2:",number2,"myText:",myText)

print("This function receive 3 parameters, if we have 'default values' defined, we can call this function without send the parameter(s) that has a default value asigned")
print("The function 'giveMeTwoNumbersAndAText' has 2 parameters with non default value and 1 parameter with a default value")
print("The function looks like this: 'giveMeTwoNumbersAndAText(number1, number2, myText=\"This is my default text\")'")
print("This is a call with the 3 parameters: giveMeTwoNumbersAndAText(1,2,\"Look at this awesome value\")")
giveMeTwoNumbersAndAText(1,2,"Look at this awesome value")
print("This is a call with 2 parameters: giveMeTwoNumbersAndAText(1,2)")
giveMeTwoNumbersAndAText(1,2)
print("If you do not have a default value for a param, you can not call the function without it")
print("For example: 'giveMeTwoNumbersAndAText(1)' will result in an error")
print("The default value is evaluated only once, when we define the function, so it not possible to change it arround the execution")
print("In python we can follow the argument order, or we can add the 'key,value' pair")
print("A valid example could be giveMeTwoNumbersAndAText(1, myText=\"Some Text\", number2=10)")
giveMeTwoNumbersAndAText(1, myText="Some Text", number2=10)
print("Once we use the 'key/value' definition, we have to use the 'key/value' for the next elements, an invalid call for this case looks like this: giveMeTwoNumbersAndAText(1, myText=\"Some Text\", 10)")

# Defining a function receiving pocitional arguments

print("Defining a function receiving pocitional arguments")
def sayAbunchOfWords(*args):
	for arg in args:
		print(arg)

print("A call with cero arg")
sayAbunchOfWords()
print("A call with one arg")
sayAbunchOfWords("one")
print("A call with two args")
sayAbunchOfWords("one","two")
print("A call with three arg")
sayAbunchOfWords("one","two","three")

# Defining a function receiving a dictionary

print("Defining a function receiving a dictionary")
def printMyDictionary(**myDictionary):
	for key in myDictionary.keys():
		print("The key:",key+"_k",",","The value:",myDictionary[key]+"_v")
print("This is the function call with a dictionary as an input")
printMyDictionary(param1="param1", param2="param2", param3="param3")
