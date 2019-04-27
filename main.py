
# While loop
# Exception w/ Break
while True:
    try:
        user_input = float(input('Enter a number '))
        if user_input > 0:
            print('number is positive')
        elif user_input < 0:
            print('number is negative')
        else: 
            print('number is zero')
        break
    except ValueError:
        print('input must be a real number')
            
# Erik
# 3.4
# 2
# -1
# is string_value a float? if so run this
# print(int(string_value))



# if isinstance(string_value,int) == True:
#     num_value = int(string_value)
#     print(num_value)
#     if num_value == 0:
#         print("num_value is 0!")
#     elif num_value < 0:
#         print("num_value is negative")
#     else:
#         print("number is positive")
# # elif isinstance(string_value, int) == False:
# #     num_value = int(string_value)
# #     if num_value == 0:
# #         print("num_value is 0!")
# #     elif num_value < 0:
# #         print("num_value is negative")
# #     else:
# #         print("number is positive")
# else:
#         print("Wrong Value Try Again")