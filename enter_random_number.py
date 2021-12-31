import random
#creating a new function
def run_guess(number,result):
  if type(result) == int:
    if (0 < result < 11):
      if (result == number):
        print('bingo')
        return True
    else:
      print('I said enter a number between 1-10')
      return False
  else:
    False


if __name__ == '__main__':
  number = random.randint(1, 10)
  print(number)

  while (True):
    try:
      result = int(input('Please enter a number between 1-10:'))
      if (run_guess(number, result)):
        break
    except ValueError:
      print("invalid input")
      continue



