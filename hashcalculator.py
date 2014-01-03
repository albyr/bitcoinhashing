#Import hashing library
import hashlib

# Logging output
print("Begin run")

# Define maximum nonce size for search
maxNonce = 1000000

for i in range(0,maxNonce+1):
    # Take base string and add nonce
    baseString = "Alby is cool!"
    hashString = baseString + str(i)
    # Convert string to bytes
    hashBytes = bytearray(hashString, 'utf-8')
    # Create hash object
    hashObject = hashlib.sha256(hashBytes)
    # Create hex hash
    hexHash = hashObject.hexdigest()
    # Create decimal representation of first four bytes
    # NOTE: Bitcoin looks at the actual *value* of the whole hash, not the first few bytes
    decimalFirstFour = int(hexHash[:4], 16)
    # If the value of the first four bytes is zero, output the string that created it and its hash
    if decimalFirstFour == 0:
        print("\"" + hashString + "\"" + " hashes to " + hexHash)

# Logging output
print("End run")
