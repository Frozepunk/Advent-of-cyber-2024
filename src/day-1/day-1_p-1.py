import input_day
res1 = sorted(input_day.list1)
res2 = sorted(input_day.list2)


print(res1)
print(res2)

final_res = list(map(lambda x: x[1] - x[0], zip(res1, res2)))
for diff in final_res:
    print(diff)
print(sum(final_res))
