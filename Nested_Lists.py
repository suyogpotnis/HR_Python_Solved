"""
Given the names and grades for each student, print the name(s) of any student(s)
 having the second lowest grade. If multiple students have the same grade order
 their names alphabeticallyself.

 Example:
 Sample Input:
 [['Bob', 36.21], ['Sam', 36.21], ['Rob', 37.2], ['Sameer', 41], ['Gina', 39]]

 Output: ['Rob']

"""

def find_second_lowest(arr):

    second_min = sorted(set(v[1] for v in arr))[1]

    arr = sorted([v[0] for v in arr if v[1] == second_min])
    return arr

if __name__ == '__main__':
    print(find_second_lowest([['Bob', 36.21], ['Sam', 36.21], ['Rob', 37.2], ['Sameer', 41], ['Gina', 39]]))
