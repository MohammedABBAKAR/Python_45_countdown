#  Making a Countdown
#  ? Create a function where given the number n to count down from, and some words txt, 
#  ? return a countdown sequence as a string leading up to the words at the end.

#  ? Put a full stop after each number and uppercase and add an exclamation mark to the word. 
#  ? See the examples below for clarification!

#  ! Examples
#  todo countdown(10, "Blast Off") ➞ "10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!"

#  todo countdown(3, "go") ➞ "3. 2. 1. GO!"

# todo countdown(5, "FIRE") ➞ "5. 4. 3. 2. 1. FIRE!"
# todo Notes
# todo n will be a number greater than 0.
# todo txt won't already include an exclamation mark.
# * Don't include 0 in the countdown.



def countdown(n, txt):
    # Create the countdown sequence
    countdown_sequence = [f"{i}." for i in range(n, 0, -1)]
    
    # Append the uppercase text with an exclamation mark
    countdown_sequence.append(txt.upper() + "!")
    
    # Join the sequence into a single string
    return " ".join(countdown_sequence)

# Test cases
print(countdown(10, "Blast Off"))  
print(countdown(3, "go")) 
print(countdown(5, "FIRE")) 
