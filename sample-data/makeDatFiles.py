# allows user to write binary to a file by typing in the bytes as hex values
import binascii

fileName = "machine.dat"
data = b"\x04\x02\x00\x01\x03\x02\x03\x03\x01\x01\x02"

print("WRITING TO FILE...")
outputFile = open(fileName, "wb")
outputFile.write(data)
outputFile.close()