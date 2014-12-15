my_input = [int(x) for x in input("Enter the number list here: ").split()]

def bubble_sort(bad_list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(bad_list)-1):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
                
bubble_sort(my_input)
print("The Sorted List is: " + str(my_input))
