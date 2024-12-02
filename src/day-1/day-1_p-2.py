import input_day
right_count={}
for num in input_day.right_list:
    if num in right_count:
        right_count[num]+=1
    else:
        right_count[num]=1
similar=0
for num in input_day.left_list:
    if num in right_count:
        similar+=num*right_count[num]
print(similar)