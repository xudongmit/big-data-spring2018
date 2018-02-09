# A. lIST
# Create a list containing any 4 strings.
A_l = ['1','2','3','4']
# Print the 3rd item in the list - remember how Python indexes lists!
print(A_l[2])
# Print the 1st and 2nd item in the list using [:] index slicing.
print(A_l[0:2])
# Add a new string with text “last” to the end of the list and print the list.
A_l.append('last')
print(A_l)
# Get the list length and print it.
print(len(A_l))
# Replace the last item in the list with the string “new” and print
A_l[-1] = 'new'
print(A_l)

# B. STRING
# Given the following list of words stored as strings, complete the following tasks:

sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']

# Convert the list into a normal sentence with join(), then print.
sentence_s = ' '.join(sentence_words)
print(sentence_s)
# Reverse the order of this list using the .reverse() method, then print. Your output should begin with [“them”, ”visualize”, … ].
sentence_words_copy = sentence_words.copy()
print(sentence_words)
sentence_words.reverse()
print(sentence_words)
# Now user the .sort() method to sort the list using the default sort order.
sentence_words.sort()
print(sentence_words)
# Perform the same operation using the sorted() function. Provide a brief description of how the sorted() function differs from the .sort() method.
sentence_words_sorted = sorted(sentence_words_copy)
print(sentence_words_sorted)
print(sentence_words_copy)

#_______________________________________________________________________
### sorted() returns a new sorted list, leaving the original list unaffected; list.sort() sorts the list in-place, mutating the list indices, and returns None
#_______________________________________________________________________

# Extra Credit: Modify the sort to do a case case-insensitive alphabetical sort.
extra_credit_sort = sorted(sentence_words_copy, key=str.lower)
print(extra_credit_sort)
extra_credit_sort1 = sorted(sentence_words_copy, key=lambda x: x.lower())
print(extra_credit_sort1)

# C. RANDOM FUNCTION
# returning an integer between a low and a high number supplied by the user, but that can be called with the low number optional (default to 0).
from random import randint

def my_random(high, low = 0):
    try:
        num = randint(low , high)
        return num
    except TypeError:
        print("Oops!  That was no valid number.  Try again...")



assert(0 <= my_random(100) <= 100)
assert(50 <= my_random(100, low = 50) <= 100)

my_random(5)
my_random('1')

# D. STRING FORMATTING FUNCTION
# Write a function that expects two inputs. The first is a title that may be multiple words, the second is a number. Given these inputs, print the following string (replacing n and title with dynamic values passed to the script).



def str_format(title, n):
    title1 = title.title()
    str = 'The number {} bestseller today is: {}'.format(n, title1)
    print(str)

str_format('string formatting function', '6')

# E: PASSWORD VALIDATION FUNCTION
# Ask the user to input a password that meets the criteria listed below. You can either use the Python input built-in function, or just pass the password as a function argument. Validate that the user’s password matches this criteria. If password is valid, print a helpful success message.

def password_validation():
    password = input('Enter your password: ')
    special_chars = ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
    n = len(password)
    num_digits = sum(char.isdigit() for char in password)
    num_upletter = sum(char.isalpha() and char.isupper() for char in password)
    num_spchar = sum(char in special_chars for char in password)

    if n>=8 and n<=14 and num_digits>=2 and num_upletter>=1 and num_spchar>=1:
        print('Success')
        return True
    else:
        print('Fail')
        return False

password_validation()

# EXPONENTIATION FUNCTION
# Create a function called exp that accepts two integers and then returns an exponentiation, without using the exponentiation operator (**). You may assume these are positive integers. Use at least one custom-defined function.
def exp(a , b):
    if b>1:
        return exp(a, b-1) * a
    else:
        return a

exp(2,3)
exp(5,4)

# G. EXTRA CREDIT
# Write your own versions of the Python built-in functions min() and max(). They should take a list as an argument and return the minimum or maximum element. Assume lists contain numeric items only.
def my_min(l):
    n_min = l[0]
    for i in range(len(l)):
        if l[i]<n_min:
            n_min = l[i]
    return n_min

def my_max(l):
    n_max = l[0]
    for i in range(len(l)):
        if l[i]>n_max:
            n_max = l[i]
    return n_max

test = [67,45,3,656,23,6,9,345,786,3,8,23,234,56]
min(test) == my_min(test)
max(test) == my_max(test)
