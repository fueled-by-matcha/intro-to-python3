def exponents(bases, powers):
  raised = []
  for base in bases:
    for power in powers:
      raised.append(base ** power)
  return raised

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 > sum2:
    return lst1
  elif sum1 < sum2:
    return lst2
  else:
    return lst1

def over_nine_thousand(lst):
  count = 0
  if len(lst) == 0:
    return 0
  for number in lst:
    count += number
    if count > 9000:
      break
  return count

def max_num(nums):
  maxNum = nums[0]
  for num in nums:
    if num > maxNum:
      maxNum = num
  return maxNum

def same_values(lst1, lst2):
  index = []
  i = 0
  j = 0
  while i < len(lst1):
    while j < len(lst2):
      if lst1[i] == lst2[j]:
        index.append(j)
      j += 1
    i += 1
  return index

def tenth_power(num):
  return num ** 10

def square_root(num):
  return num ** 0.5

def win_percentage(wins, losses):
  return (wins / (wins + losses)) * 100

def average(num1, num2):
  return (num1 + num2) / 2

def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

def tip(total, percentage):
  return total * (percentage / 100)


