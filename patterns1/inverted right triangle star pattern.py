'''
Pattern 
Inverted right triangle star pattern
Enter number of rows: 5
*****
****
***
**
*
'''
print('Inverted right triangle star pattern: ')
rows=int(input('Enter number of rows: '))
for i in range(1,rows+1):
	for j in range(i,rows+1):
		print('*',end=' ')
	print('\n',end="")

