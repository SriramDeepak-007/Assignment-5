"""Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list"""



#List of numbers from 1 to 10
numbers = list(range(1,11))


# Extracting the first five elements
first_five_elements = numbers[0:5]


# Reversing the extracted elements
reverse_list = first_five_elements[::-1]



print(f"Original list:{numbers}")
print(f"Extracted first five elements: {first_five_elements}")
print(f"Reversed extracted elements: {reverse_list}")