
    def bubble_sort(number_list):
        
        for i in range(0, len(number_list)-1, 1):
            for j in range(0, len(object)):
                if(number_list[j] > number_list[j+1]):
                    temp = number_list[j]
                    number_list[j] = number_list[j+1]
                    number_list[j+1] = temp
        return number_list

        
    