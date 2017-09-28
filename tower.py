poles = [[-1,4,3,2,1],[-1],[-1]]
middle=0
left=2
right=1
print(1,poles)
tall=len(poles[0])-1
while True:
  #distribution
  if len(poles[middle]) > 2:
    if poles[left][-1] == -1 and poles[right][-1] == -1:
      if tall % 2 == 0:
        poles[right].append(poles[middle].pop())
        poles[left].append(poles[middle].pop())
      else:
        poles[left].append(poles[middle].pop())
        poles[right].append(poles[middle].pop())
      print(2,poles)
    else:
      leftdiff = abs(poles[left][-1] - poles[middle][-1])
      rightdiff = abs(poles[right][-1] - poles[middle][-1])
      if poles[left][-1] > -1 and poles[left][-1] > poles[middle][-1] and leftdiff == 1:
        poles[left].append(poles[middle].pop())
      elif poles[right][-1] > -1 and poles[right][-1] > poles[middle][-1] and rightdiff == 1:
        poles[right].append(poles[middle].pop())
      elif len(poles[middle]) == 3 and poles[left][-1] == -1:
        poles[left].append(poles[middle].pop())
      elif len(poles[middle]) == 3 and poles[right][-1] == -1:
        poles[right].append(poles[middle].pop())
      elif len(poles[middle]) > 3 and poles[left][-1] > -1 and poles[left][-1] > poles[middle][-1]:
        poles[left].append(poles[middle].pop())
      elif len(poles[middle]) > 3 and poles[right][-1] > -1 and poles[right][-1] > poles[middle][-1]:
        poles[right].append(poles[middle].pop())
      elif poles[left][-1] > -1 and poles[right][-1] > -1:
        if leftdiff > rightdiff and poles[left][-1] > poles[middle][-1]:
          poles[left].append(poles[middle].pop())
        elif rightdiff > leftdiff and poles[right][-1] > poles[middle][-1]:
          poles[right].append(poles[middle].pop())
          
      leftdiff = abs(poles[left][-1] - poles[middle][-1])
      rightdiff = abs(poles[right][-1] - poles[middle][-1])
      if poles[left][-1] > -1 and poles[left][-1] > poles[middle][-1] and leftdiff == 1:
        poles[left].append(poles[middle].pop())
      elif poles[right][-1] > -1 and poles[right][-1] > poles[middle][-1] and rightdiff == 1:
        poles[right].append(poles[middle].pop())
      elif len(poles[middle]) > 2 and poles[left][-1] == -1:
        poles[left].append(poles[middle].pop())
      elif len(poles[middle]) > 2 and poles[right][-1] == -1:
        poles[right].append(poles[middle].pop())
      elif poles[left][-1] > -1 and poles[right][-1] > -1:
        if leftdiff > rightdiff and poles[left][-1] > poles[midlle][-1]:
          poles[left].append(poles[middle].pop())
        elif rightdiff > leftdiff and poles[right][-1] > poles[middle][-1]:
          poles[right].append(poles[middle].pop())
      print(3,poles)  
  
  #transfer-1
  if poles[left][-1] == -1 and poles[right][-1] != -1:
    poles[left].append(poles[right].pop())
  elif poles[right][-1] == -1 and poles[left][-1] != -1:
    poles[right].append(poles[left].pop())
  elif poles[left][-1] > -1 and poles[left][-1] < poles[right][-1]:
    poles[right].append(poles[left].pop())
  elif poles[right][-1] > -1 and poles[right][-1] < poles[left][-1]:
    poles[left].append(poles[right].pop())  
  print(4,poles)

  if poles[0][-1] == -1 and poles[1][-1] == -1:
    break

  #rotate
  if middle == 0:
    if tall % 2 == 0:
      middle = 1
      left = 0
      right = 2
    else:
      middle = 2
      left = 1
      right = 0
  elif middle == 1:
    if tall % 2 == 0:
      middle = 2
      left = 1
      right = 0
    else:
      middle = 0
      left = 2
      right = 1
  else:
    if tall % 2 == 0:
      middle = 0
      left = 2
      right = 1
    else:
      middle = 1
      left = 0
      right = 2
  #print("middle=",middle,"left=",left,"right=",right)
  #transfer-2
  if poles[left][-1] == -1 and poles[right][-1] != -1:
    poles[left].append(poles[right].pop())
  elif poles[right][-1] == -1 and poles[left][-1] != -1:
    poles[right].append(poles[left].pop())
  elif poles[left][-1] > -1 and poles[left][-1] < poles[right][-1]:
    poles[right].append(poles[left].pop())
  elif poles[right][-1] > -1 and poles[right][-1] < poles[left][-1]:
    poles[left].append(poles[right].pop())  
  print(5,poles)
