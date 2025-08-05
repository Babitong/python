# WORKING WITH LIST

my_list = []
number = 10
while number < 50:
    my_list.append(number)
    number += 10 
print(my_list)

my_list.insert(1, 15)  # Insert 15 at the second position
print(my_list)

other_list = [50, 60, 70]
my_list.extend(other_list)  # Extend my_list with other_list
print(my_list)

my_list.pop()  # Remove and return the last item
print(my_list)

my_list.sort()  # Sort the list in ascending order
print(my_list)

index = my_list.index(30)  # Find the index of the first occurrence of 30
print(f"The index of 30 is: {index}")