#example client implementation of a bot license as an NFT
#By @yoloGorilla yoloGorilla#0703
from tokenLicense import tokenLicense

#contract address for bot license nft
addr = "0x0165878A594ca255338adfa4d48449f69242Eb8F"
#user address using the bot
user = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

license = tokenLicense(addr,user)
license.initializeContract()
botName = license.getBotName()
validKey = license.userValid()

print(f'user {user} has a valid key for {botName}: {validKey}')
