

input_string = "mamam"
is_palindrome = False
length_of_string = len(input_string)
if length_of_string == 1 : 
	is_palindrome = True 
if length_of_string == 0:
	is_palindrome = False
i = 0
j = length_of_string - 1
while (i < length_of_string/2):
	if (input_string[i] != input_string[j]):
		is_palindrome = False
		break;
	else:
		i= i+1 
		j = j -1
		is_palindrome = True 	
	
print is_palindrome





