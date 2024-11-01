# O(n²)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
      
        
print_items(10)

# quadratic time complexity! 
# Here, as the input size n grows, the time it takes grows by n×n. 
# This usually happens with algorithms involving nested loops (e.g., bubble sort) where each element is compared with every other element.
