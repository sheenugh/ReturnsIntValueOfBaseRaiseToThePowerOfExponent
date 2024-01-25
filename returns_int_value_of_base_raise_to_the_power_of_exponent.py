


# ----- FUNCTIONS ------
def case1_exponent(base,exp):
    number = exp
    result = 1
    while number > 0:
        result = result * base
        number = number - 1
    print(base, "raises to the power of", exp, "is:", result, "i.e", "(2 * 2 * 2 * 2 * 2 = 32)")

# >>>>>>>>> PSEUDO CODE <<<<<<<<<
# - Given: Case 1
base1 = 2
exponent1 = 5 

# - Given: Case 2
base2 = 5
exponent2 = 4 

# - Caller of the def function/s
case1_exponent(base1, exponent1)
# ----- ACTUAL CODES -----
