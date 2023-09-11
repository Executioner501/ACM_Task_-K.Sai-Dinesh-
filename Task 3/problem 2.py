input("enter no of cases: ")
input_string = input(" ")
input_list = input_string.split()
input_array = []
for element in input_list:
    try:
        input_array.append(int(element))
    except ValueError:
        print(f"Skipping '{element}' as it is not a valid integer.")
sum_of_elements = sum(input_array)

print("", sum_of_elements)
