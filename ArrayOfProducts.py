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
# time complexity is O(3N) space complexity is O(N)
def arrayOfProducts(array):
    # at pos i in left array, the value is all product of all values to left of pos i in original array
    left_array = [1 for _ in range(len(array))]
    # at pos i in right array, the value is all product of all values to right of pos i in original array
    right_array = [1 for _ in range(len(array))]
    #output array
    products = [1 for _ in range(len(array))]

    # fill left array
    left_product = 1
    for i in range(len(array)):
        left_array[i] = left_product
        left_product *= array[i]

    # fill right array
    right_product = 1
    for i in reversed(range(len(array))):
        right_array[i] = right_product
        right_product *= array[i]

    for i in range(len(array)):
        products[i] = left_array[i] * right_array[i]

    return products



