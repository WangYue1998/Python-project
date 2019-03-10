odd_sum = 0
even_sum =0
odd_count =0
even_count =0
positive_int_count =0

n_str = input("Input an integer (0 terminates): ")
n_int= int(n_str)

while n_int!=0:
    if n_int%2==0 and n_int>0:
        even_count+=1
        even_sum += n_int
        positive_int_count+=1
         
    if n_int%2==1 and n_int>0:
        odd_count+=1
        odd_sum += n_int
        positive_int_count+=1
   
        
    n_str = input("Input an integer (0 terminates): ")
    n_int= int(n_str)
        
print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
    
