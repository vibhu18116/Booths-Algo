from auxFunctions import *
import os.path

from os import path


def main():
	success = takeUserInput()

	if type(success) == int and success == -1:
		return

	num1 = decimalToTwosComplement(success[0])
	num2 = decimalToTwosComplement(success[1])

	padFactor = max(len(num1), len(num2))

	num1 = padNum(num1, padFactor)
	num2 = padNum(num2, padFactor)

	multiplication = boothsMultiplication(num1, num2)
	print(multiplication)

	multiplication_int = binaryToDecimal(multiplication)
	print(multiplication_int)

	division_flag = True

	if checkZero(num2):
		print("Attempt of division by zero.")
		division_flag = False

	else:
		division = divisionOperation(num1, num2)

		q = division[0]
		r = division[1]

		print(q, r)

		q_int = binaryToDecimal(q)
		r_int = binaryToDecimal(r)

		print(q_int, r_int)


	output_file = "output.txt"

	with open(output_file, "w") as f:
		f.write("Numbers: " + str(success[0]) + " and " + str(success[1]) + "\n")
		f.write("Multiplication result: \n")
		f.write("\tBinary: " + multiplication + "\n")
		f.write("\tInteger: " + multiplication_int + "\n")
		f.write("Division result: \n")

		if not division_flag:
			f.write("\tAttempt to divide by zero.n\n")

		else:
			f.write("\tBinary: \n")
			f.write("\t\tQuotient " + q + "\n")
			f.write("\t\tRemainder " + r + "\n")
			f.write("\tInteger: \n")
			f.write("\t\tQuotient " + q_int + "\n")
			f.write("\t\tRemainder " + r_int + "\n")

	print("Output written to output.txt")

def takeUserInput():
	print("Welcome to Multiplication and Division Calculator\n")
	print("This calculator uses Booth's algorithm to generate the results.")
	print("If two numbers a and b are provided, a*b and a/b will be evaluated.")
	print("The first two lines of output have result of multiplication in binary and decimal format.")
	print("The next lines have quotient and remainder respectively in binary and decimal format,\
	 obtained on division of first number by second number.\n")

	print("Choose an option:")
	print("1. Give two space separated numbers through the prompt.")
	print("2. Read numbers from a file (the file should have numbers in a space separated format).")

	try:
		choice = int(input())

	except ValueError:
		print("Invalid Input. Terminating.")
		return -1
	

	if choice == 1:
		numbers = terminalInput()

	elif choice == 2:
		numbers = fileInput()

	else:
		print("Invalid Input. Terminating.")
		return -1

	return numbers


def terminalInput():
	return tuple(map(int,input().split()))


def fileInput():
	print("Provide filename: ")
	filename = input()

	if not path.exists(filename):
		print("No such file exists. Terminating.")
		return -1

	with open(filename, "r") as f:
		line = f.readline()

	numbers = tuple(map(int, line.split()))
	return numbers


def boothsMultiplication(num1, num2):

	a = num1 + "0"*(len(num1) + 1)
	s = negativeOfBinary(num1) + "0"*(len(num1) + 1)
	p = "0"*len(num1) + num2 + "0"


	count = len(num2)

	for i in range(count):

		if (p[-2] == "0" and p[-1] == "1"):
			p = addTwoBinary(p, a)

		elif (p[-2] == "1" and p[-1] == "0"):
			p = addTwoBinary(p, s)


		p = rightShift(p)

	ans = p[:-1]

	return ans


def divisionOperation(dividend, divisor):

	m = divisor
	a_q = dividend[0]*(len(dividend)) + dividend

	count = len(dividend)

	for operation in range(count):

		a_q = leftShift(a_q)

		if (a_q[0] != m[0]):
			a = addTwoBinary(a_q[:len(dividend)], m)
		else:
			a = subtractTwoBinary(a_q[:len(dividend)], m)

		success = False

		if a[0] == a_q[0]:
			success = True

		if success or (checkZero(a) and checkZero(a_q[len(dividend):])):
			a_q = a_q[:-1] + "1"
			a_q = a + a_q[len(dividend):]

		elif not success and (not checkZero(a) or not checkZero(a_q[len(dividend):])):
			a_q = a_q[:-1] + "0"


	remainder = a_q[:len(dividend)]

	if divisor[0] == dividend[0]:
		quotient = a_q[len(dividend):]

	else:
		quotient = negativeOfBinary(a_q[len(dividend):])

	return (quotient, remainder)

if __name__ == "__main__":
	main()