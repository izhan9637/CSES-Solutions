def generateGray(n):
	if (n <= 0):
		return ["0"]
	if (n == 1):
		return [ "0", "1" ]

	recAns = generateGray(n - 1)

	mainAns = []

	for i in range(len(recAns)):
		s = recAns[i]
		mainAns.append("0" + s)

	for i in range(len(recAns) - 1, -1, -1):
		s = recAns[i]
		mainAns.append("1" + s)

	return mainAns

def generateGrayarr(n):
	arr = generateGray(n)
	print(*arr, sep = "\n")

n = int(input())
generateGrayarr(n)
