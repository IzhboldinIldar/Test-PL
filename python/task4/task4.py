file4 = open(r"C:\python\task4\file4.txt", "r")
nums = file4.read().split('\n')
m = sorted(nums)[len(nums) // 2]
print(sum(abs(int(v) - int(m)) for v in nums))