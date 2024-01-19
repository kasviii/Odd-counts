def count_odd_numbers(low, high):
 """
 Counts the odd numbers between two numbers, like finding the puzzle pieces that don't match!

 Args:
     low: The first number, where we start looking for odd puzzle pieces.
     high: The second number, where we stop looking.

 Returns:
     The number of odd puzzle pieces we found!
 """

 
 if low > high:
   return 0  
 count = (high - low) // 2
 if low % 2 == 1:
   count += 1  
 return count

low = 1  
high = 20  

number_of_odds = count_odd_numbers(low, high)
print("There are", number_of_odds, "odd pieces between", low, "and", high)
