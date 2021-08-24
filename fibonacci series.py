def fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    for i in range(num):
      print(series, end='')

      num1 = num2
      num2 = series
    series = num1 + num2
    num = int(input("enter how many numbers needed in fibonacci series-"))
    fibonacci(num)
