import hashlib

def mass_seed_to_address(seedkey):
    # Hash the seedkey using sha256
    sha = hashlib.sha256()
    sha.update(seedkey.encode())
    hash = sha.hexdigest()
    # Hash the result again using ripemd160
    ripemd = hashlib.new('ripemd160')
    ripemd.update(hash.encode())
    hash = ripemd.hexdigest()
    # Add the version byte to the start of the hash
    version_byte = '00'
    hash = version_byte + hash
    # Hash the result again using sha256 twice
    sha = hashlib.sha256()
    sha.update(bytes.fromhex(hash))
    hash = sha.hexdigest()
    sha = hashlib.sha256()
    sha.update(bytes.fromhex(hash))
    hash = sha.hexdigest()
    # Take the first 4 bytes of the hash as the checksum
    checksum = hash[:8]
    # Add the checksum to the end of the hash
    hash = hash[8:] + checksum
    # Base58 encode the result to get the bitcoin address
    bitcoin_address = ''
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    num = int(hash, 16)
    while num > 0:
        bitcoin_address = alphabet[num % 58] + bitcoin_address
        num = num // 58
    return bitcoin_address

# Read the seedkeys from the wallets.txt file
with open("wallets.txt", "r") as f:
    seedkeys = f.readlines()

# Convert each seedkey to a bitcoin address
addresses = [mass_seed_to_address(seedkey.strip()) for seedkey in seedkeys]

# Write the addresses to the generated.txt file
with open("generated.txt", "w") as f:
    f.write("\n".join(addresses))
