import hashlib
import codecs

test_input = "abcdef"
real_input = "iwrupvqb"

num = 0
while True:
    input = str.encode(real_input + str(num))
    result = hashlib.md5(input).digest()
    # codecs.decode(result, "hex")
    print(result)

    if result[0] == 0:
        if result[1] == 0:
            if result[2] == 0:
                print("Found!")
                print(num)
                break

    num += 1