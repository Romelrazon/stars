
def main(n):
   i = 1
   while i <= n :
      j = 1
      while j <= i:
      
         print("*", end=" ")
         j = j + 1
      print()
      i = i + 1
 

n = int(input('Enter the number of rows: '))

# kapag lumabas po ang enter The number of rows ay lagay ninyo lang po ay 5 dahil ang nilagay ko pa 
#sa main ay 5 para lumabas ang upper_left triangle po 
main(5)