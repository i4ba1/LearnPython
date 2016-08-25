def bubble_sort(number_list):
    for i in range(0, len(number_list)-1, 1):
        for j in range(1, len(number_list)-i, 1):
            if(number_list[j] < number_list[j-1]):
                temp = number_list[j]
                number_list[j] = number_list[j-1]
                number_list[j-1] = temp
    print(number_list)
    return number_list


def main():        
    number_list = [13,5,7,1,0]
    bubble_sort(number_list)    
    print(number_list)
    
main()