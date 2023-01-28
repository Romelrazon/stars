def main(n):
   i = n
   while i>=1:
      print(" "*(n-i) + "*" * i)
      i-=1 
      
n = int(input('Enter the number of rows: '))


main(5)