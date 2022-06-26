# EasyRoman
A simple library written for python to interchange Roman and Integer Numbers

==============================================================================================================
Usage:

#import the library:
from EasyRoman import RomanNumber

#Create an object:
num = RomanNumber()

#Print the result with valid input:
print(num.convert("M"))
print(num.convert(1234))

==============================================================================================================
Output:
1000
MCCXXXIV
==============================================================================================================

Exception:
Error, cannot compute -> Could be any ambigious input.
Expected Roman string, Got an invalid input  -> Invalid Roman Input.
Expected Integer, got { the type of input } -> Invalid Input type when trying to convert integer to Roman.
