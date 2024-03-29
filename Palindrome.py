# O(n) complexity and space is O(1)....
def isPalindrome(string):
    # Write your code here...
    right = -1
    for i in range(len(string)):
        if(string[i] != string[right]):
            return False
        else:
            right = right - 1
    return True
