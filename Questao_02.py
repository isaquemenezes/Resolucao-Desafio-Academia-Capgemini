def passwordString(password):

  cond1 = "!@#$%^&*()-+"
  count_cond = [0,0,0,0]

  for char in password:
    if char.isdigit():
      count_cond[0] = 1
    elif char.islower():
      count_cond[1] = 1
    elif char.isupper():
      count_cond[2] = 1
    elif char in cond1:
      count_cond[3] = 1
      
  return max(6 - len(password), 4- sum(count_cond))
