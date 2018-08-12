"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given scores.
Store them in a list and find the score of the runner-up.

Example:
Sample Input
[2, 3, 6, 6, 5]

Output:
5

Explanation: In the above given list 5 is the second highest score.
"""

def find_runner_up_score(arr):

    # Get current max value in the array
    max_value = max(arr)
    i = 0  # set up variable i to iterate through elements of the array

    while i < len(arr):
        if max_value == max(arr):
            arr.remove(max(arr))
        i = i + 1
    return max(arr)

if __name__ == '__main__':
    print(find_runner_up_score([2, 3, 6, 6, 5]))
