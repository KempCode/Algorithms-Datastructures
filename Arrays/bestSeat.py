# With left and right pointer types of array questions use while loops, where L and R are indexes.
# O(N) time O(1) space...
def bestSeat(seats):
    # find the most contiguous 0's in a row, then the middle of that space
    best_seat = -1
    left = 0
    highest_run = 0
    current_run = 0
    
    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1 # Loop through all the 0s until the 1

        current_run = right - left - 1
        if current_run > highest_run:
            highest_run = current_run
            best_seat = (right + left) // 2
        left = right
    return best_seat


# when 2 equally good seats, sit in lower index
# if no seat return -1 - ie no 0's
# array at least 1 in size
# first and last seats are taken

def bestSeat(seats):
    best_seat = -1
    max_space = 0
    left = 0

    while left < len(seats):
        right = left + 1
        # Count the number of 0's until the next 1
        while right < len(seats) and seats[right] == 0:
            right += 1
            
        current_space = right - left - 1
        if current_space > max_space:
            max_space = current_space
            best_seat = (left + right) // 2  # Choose the middle seat
            
        # Move left pointer to where right is
        left = right
    return best_seat


# With left and right pointer types of array questions use while loops, where L and R are indexes.