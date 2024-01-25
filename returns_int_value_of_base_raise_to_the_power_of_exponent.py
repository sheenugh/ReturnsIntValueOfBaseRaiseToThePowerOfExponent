


# ----- FUNCTIONS ------
def case1_exponent(base,exp):
    number = exp
    result = 1
    while number > 0:
        result = result * base
        number = number - 1
    print(base, "raises to the power of", exp, "is:", result, "i.e", "(2 * 2 * 2 * 2 * 2 = 32)")

def case2_exponent(base,exp):
    result = base ** exp
    return result

# >>>>>>>>> PSEUDO CODE <<<<<<<<<
# ----- ACTUAL CODES -----
# - Given: Case 1
base1_value= 2
exponent1_value = 5 

# - Given: Case 2
base2_value= 5
exponent2_value= 4 


# - Caller of the def function/s
case1_exponent(base1_value, exponent1_value)
result = case2_exponent(base2_value, exponent2_value) # - Case 2: Printing the result
print(f"{base2_value} raises to the power of {exponent2_value} is: {result} i.e (5 * 5 * 5 * 5 = 625)")

