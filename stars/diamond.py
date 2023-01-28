
def main(n):
   
   i = 1
   while i<n:
 
      print(" "*(n-i) + "* " * i)
      i+=1 


   i = n
   while i>=1:
    
      print(" "*(n-i) + "* " * i)
      i-=1
 

n = int(input('Enter the number of rows: '))
# pag lumabas po yung enter number : ilagay lang ang number 5

main(5)