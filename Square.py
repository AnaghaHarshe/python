#The provided code stub reads an integer,n, from STDIN. For all non-negative integers i<n, print i*i .

def print_squares(n):
  for i in range(n):
    print(i ** 2)

if __name__ == "__main__":
  n = int(input())
  print_squares(n)
