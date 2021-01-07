new_list=['1','2','3','4','6']
new_list_1='12346'
def reverse(num):
    num_new=num[::-1]
    if num_new==num:
        print('the message is palindrome')
    else:
        print('the message is not palindrome')
reverse('12332')

for i in range(len(new_list)):
    print(new_list[i])# this works because we call elements by their indexes
print('---------------')
for b in new_list_1:
    print(new_list_1(b))#this part of the code will not work as it will not have the index to call