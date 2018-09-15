"""
Task
Read a given string, change the character at a given index and then print the modified string.

Input Format
The first line contains a string, .
The next line contains an integer , denoting the index location and a character  separated by a space.

Output Format
Using any of the methods explained above, replace the character at index  with character .

Sample Input:
abracadabra
5 k
Sample Output: abrackdabra
"""
def mutate_string(string, position, character):
    if len(string) < 1:
        return string

    if len(string) == 1:
        return character

    arr = list(string)

    for i in range(len(arr)):
        if i == position:
            arr[i] = character
        else:
            pass

    val= ''
    for j in arr:
        val = val+ ''.join(j)

    return val
