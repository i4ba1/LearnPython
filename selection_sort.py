def selection_sort(number_list):
    for i in range(0, len(number_list)-1, 1):
        min_index = i
        for j in range(1, len(number_list), 1):
            if(number_list[j] < number_list[j-1]):
                min_index = j
                
        temp = number_list[i]
        number_list[i] = number_list[min_index]
        number_list[min_index] = temp
    
    return number_list


def main():        
    number_list = [64,25,12,22,11]
    print(selection_sort(number_list))
    
main()