print('Mirrored triangular rowise incremental number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(number_rows,0,-1):
	for column in range(number_rows,row,-1):
		print('  ',end=' ')
	for column in range(1,row+1):
		if row < 10:
			print(f'0{row}',end=' ')
		else: 
			print(row,end=' ')
	print()