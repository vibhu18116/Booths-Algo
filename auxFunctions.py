def binaryToDecimal(num):

	if num[0] == "0":
		return str(int("0b" + num, 2))

	return "-" + str(int("0b" + negativeOfBinary(num), 2))


def padNum(num, i):
	return num[0]*(i-len(num)) + num

def decimalToTwosComplement(num):

	isNumNeg = False

	if num<0:
		isNumNeg  = True
		num = num * (-1)

	binary = bin(num)
	binary = binary[2:]
	binary = "0" + binary

	if not isNumNeg:
		return binary

	onesComp = onesComplement(binary)

	twosComp = addOne(onesComp) 

	return twosComp


def onesComplement(binary):

	comp = []

	for bit in binary:

		if bit == "0":
			comp.append("1")

		else:
			comp.append("0")


	return "".join(comp)


def addOne(oneCompNum):

	result = []

	carry = 1

	for bit in oneCompNum[::-1]:

		if carry == 0:
			result.append(bit)


		else:

			if bit == "0":
				result.append("1")
				carry = 0

			else:
				result.append("0")
				carry = 1


	return "".join(result[::-1])


def addTwoBinary(num1, num2):

	result = ""

	carry = 0

	for bit in range(len(num1)-1, -1, -1):

		b1 = int(num1[bit])
		b2 = int(num2[bit])

		toAdd = (not b1)&(b2^carry) | b1&(not(b2^carry))

		result = str(toAdd) + result
		carry = ((not b1)&b2&carry) | (b1&(b2 | carry))

	return result

def negativeOfBinary(num):
	return addOne(onesComplement(num))


def subtractTwoBinary(num1, num2):
	return addTwoBinary(num1, negativeOfBinary(num2))

def rightShift(num):
	return num[0] + num[:-1]

def leftShift(num):
	return num[1:] + "0"

def checkZero(num):

	for i in num:

		if i!="0":
			return False

	return True