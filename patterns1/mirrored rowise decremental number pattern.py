print('mirroired rowise decremental number pattern: ')
number_rows=int(input('Enter number of rows: '))
print('',end='')
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print('  ',end=' ')
	for column in range(row,number_rows+1):
		if row < 10:
			print(f'0{row}',end=' ')
		else:
			print(row,end=' ')
	print()