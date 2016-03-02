import binascii
file = open("test.mp3");
read_data = file.read()
hexdecimal = binascii.hexlify(read_data);
decimal = int(hexdecimal,16);
binary = bin(decimal)[2:].zfill(8)
#Uncomment to verify output, should with any file
#take around 0.25 seconds to run
# print binary
