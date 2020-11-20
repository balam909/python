# Creating commnts for functions
def myDocumentedFunction():
	"""This is a comment describing the functionality of this function

	Actually it does nothing, but we need to ilustrate how to comment
	"""
	pass

print("Calling <your_function_name>+.__doc__ you can take a look into the documentation")
print("A call to the documentation function for myDocumentedFunction function will be something like: myDocumentedFunction.__doc__")
print("This is how our documented function looks like: ")
print(myDocumentedFunction.__doc__)
