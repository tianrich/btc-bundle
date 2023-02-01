import os
import random
import binascii
import mnemonic

# Number of wallets to create
num_wallets = 1000000

# Open a file to write the wallets
with open('wallets.txt', 'w') as f:
    for i in range(num_wallets):
        entropy = os.urandom(16)
        m = mnemonic.Mnemonic('english')
        wallet = m.to_mnemonic(entropy)
        f.write(wallet + '\n')

print('Done creating wallets. Check the wallets.txt file for the generated wallets.')
