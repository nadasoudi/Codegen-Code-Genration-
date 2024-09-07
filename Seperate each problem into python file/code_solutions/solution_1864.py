class Solution:
    def countInstance(self, arr, x):
        count = 0
        for i in arr:
            if i == x:
                count += 1
        return count

# { 
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

# } Driver Code Ends
# User function Template for Python 3

# Function to check if x is present in arr
def isPresent(arr, x):
    for i in arr: