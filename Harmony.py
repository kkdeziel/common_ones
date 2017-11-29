#Used for Harmony problem in Microsoft team competition, September 2017
#finds how many binary 1's two given numbers have in common

import sys


#powers of 2, 0 - 31
powersOfTwo = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648]



check = 0
with open(sys.argv[1], "r") as inp:
	with open(sys.argv[2], "w") as outp:
		for line in inp:
			if check == 0:
				check = 1
				continue

			nums = line.split(",")
			numOne = int(nums[0])
			numTwo = int(nums[1])

			i = 31
			total = 0
			while i > -1:
				a = numOne - powersOfTwo[i]
				b = numTwo - powersOfTwo[i]

				#if both numbers contained a '1' at this power position:
				if a >= 0 and b >= 0:
					total+=1

				#only set numbers if subtracting this power resulted in a number higher than zero
				if a >= 0:
					numOne = a
				if b >= 0:
					numTwo = b
				i -= 1
			strTotal = str(total)
			outp.write(strTotal)
			outp.write('\n')

