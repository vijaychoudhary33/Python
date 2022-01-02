num_list = [1, 2, 3, 4, 5]

print(f'Current Numbers List {num_list}')

num = int(input("Please enter a number to add to list:\n"))

index = int(input(f'Please enter the index between 0 and {len(num_list) - 1} to add the number:\n'))

num_list.insert(index, num)

print(f'Updated Numbers List {num_list}')
