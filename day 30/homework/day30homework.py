#3) შექმენით ფუნქცია სახელად odd_index_sum რომელსაც გადაეცემა რიცხვების სია,
#თქენი დავალებაა შეკრიბოთ ყველა ის რიცხვი რომელიც დგას !!!!კენტ ინდექსზე!!!,
#მიღებული ჯამი დააბრუნეთ ფუნქციიდან









def odd_index_sum(numbers_list):
    sum_of_odd= 0

    for number in numbers_list:
        if number % 2 == 1 :
            sum_of_odd = sum_of_odd + number
    
    return sum_of_odd



result = odd_index_sum([1,2,3,4,5,6,7,8,9,10])

print(result)