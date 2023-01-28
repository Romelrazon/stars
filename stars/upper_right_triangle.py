# Python star pattern to print right half pyramid

def main(n):
   i = 1
   while i<=n:
     
      print("  "*(n-i) + "* " * i)
      i+=1 
 

n = int(input('Enter the number of rows: '))


main(5)