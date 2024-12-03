import re
with open("src\day-3\input.txt","r") as file:
    courp_mem=file.read()
pattern=r"mul\((\d{1,3}),(\d{1,3})\)"
matches=re.findall(pattern,courp_mem)
print(matches)
res_sum=0
for x,y in matches:
    res_sum+=int(x)*int(y)
print(res_sum)