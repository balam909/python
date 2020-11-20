import functools

print("We have three helpful functions; filter(), map() y reduce()")
print("All of them receive a function and one or more secuences (depending of the number of paramaters that the function receive)")
def return_some_prime_numbers(x): return x%2!=0 and x%3!=0
print("For a function like this 'def return_some_prime_numbers(x): return x%2!=0 and x%3!=0' we can use the next call: filter(return_some_prime_numbers,range(2,25))")
result=filter(return_some_prime_numbers,range(2,25))
print(list(result))
print("The map() function help us to execute one task to all the elements contained into a list")
print("If we want to know the cube for each element into a list, we can create a function like this: def return_cube(x): return x**3")
def return_cube(x): return x**3
print("And then, call it using something like this: map(return_cube,range(1,11))")
result=map(return_cube,range(1,11))
print(list(result))
print("reduce() is another function, it take the first two elements into the sequence, execute the operation for them, and then execute the function again taking the result for the previous operation and the next value into the sequence")
print("If we want to sum all the numbers from 0 to 10, we can create a function that sum two numbers like this: def sum(x,y): return x+y")
def sum(x,y): return x+y
print("Now we can call it with an expresion like this: functools.reduce(sum,range(1,11))")
result=functools.reduce(sum,range(1,11))
print(result)
print("We can also apply operations without the previous mentioned functions, this kind of implementation al call LC's, example:")
print("We can create a sequence like this: fruits=['fresa  ','  uva  ','  durazno'] and apply the function strip() to each element with the next instriction: [fruit.strip() for fruit in fruits] -> the brackets are mandatory")
fruits=['fresa  ','  uva  ','  durazno']
result=[fruit.strip() for fruit in fruits]
print(result)
print("We can also delete elements from a sequence, using the reserved word: 'del', from the previous sequence:",result)
print("We can delete an element, for example, using a this call: del result[1], we wll delete the second element into the sequence")
del result[1]
print(result)
