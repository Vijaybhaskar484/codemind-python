n = int(input()) 
oddcount = n//100%2 + n//10%10%2 + n%10%2 
if oddcount==3: 
	print("Odd") 
elif oddcount==0: 
	print("Even") 
else: 
	print("Mixed") 