# First the Naive solution
# O(N^2) time and O(N) Space
def for_one_pos(array, pos):
    current_product = 1
    for i in range(len(array)):
       if(i == pos):
           continue
       else:
           current_product *= array[i]
           print(current_product)
    return current_product
        


def arrayOfProducts(array):
    product_array = []
    for i in range(len(array)):
        product_array.append(for_one_pos(array, i))
    return product_array
            

# Second the optimal complexity solution


