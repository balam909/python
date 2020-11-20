a=["Juan", "Pedro", "Pablo", "Luis", "Gerardo"]
b=0
# A simple iteration arround the list
print("Starting simple iterarion for",a)
for x in a:
	print("Element[",b,"]=",x)
	b+=1

# An itteration modifying the elements into the original list
print("Starting to modify the original list")
b=0
for x in a[:]:
	a[b]=x+" D."
	b+=1
print("Now the list contains those elements",a)
print("You can use 'break' or 'continue' when you are working with iterators in the same way you use it in another languages")
print("The instruction 'pass' do nothing, it is usefull to set a functionality into a flow we don't want to implemet yet, but mainatain a correct structure into the code you can think on this like a similar function for a '//TODO:' comment in Java")
