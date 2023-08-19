def more_frequent_item(my_list, item1, item2):
  count1 = my_list.count(item1)
  count2 = my_list.count(item2)
  if count1 > count2:
    return item1
  elif count1 < count2:
    return item2
  else:
    return item1

def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

def add_greetings(names):
  new_greetings = []
  for name in names:
    new_greetings.append("Hello, " + name)
  return new_greetings

def odd_indices(my_list):
  new_list = []
  index = 0
  while index < len(my_list):
    if index % 2 != 0:
      new_list.append(my_list[index])
    index += 1
  return new_list
