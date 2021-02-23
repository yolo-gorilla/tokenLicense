# tokenLicense
Ethereum powered standard for software licenses. Makes authentication, reselling and activation of keys easy, simpole and safe




# Token Licenses 1.0:

## Token Properties
Tokens are minted by issuer (Bot Dev). The issuer is the owner and can define a token to have the following properties:
#### Supply: How many tokens are created
#### Divisible: No (no point in divisible licenses)
#### Locked Supply aka Max supply: Can devs create new keys 
#### Subscription time: Month / year (this is done by calculating block height) callable as this.subscription.active returns bool
#### Transfer Fee: Devs can take a transfer Fee so tokens sold can pay a % to the dev automatically (optional)
#### Transfer Lock: Optional Lock preventing token transfer for x amount of time 
#### Subscription Rate: This is a standard rate for payment per block time added 
#### Subscription Payment: Contract address or identifier for base currency to use (dai, ether, usdc etc) 

## Token actions
Tokens are :
Transferable from party to party 
Can be used on any ethereum compatible wallet 
Standardized to make them compatible across different bots and to allow marketplaces to come about 
#### activate 

#### renew 
This lets us renew a key by sending a specified amount of $$$ to the parent contract. The money sent translates to a specific number of blocks added to the subscription time. 

Infrastructure needed:

Client libraries :
    Client libraries are important to allow bot developers to quickly integrate into the standard. I am a python dev so first integration will be a python library followed by a nodeJs library. This will be plug and play and allow devs to point to contract address and quickly plug into the built in auth for bots all on the network

### Future integration:
Anti crack protection 
  Client libraries can be bundled with additional anti-cracking libraries. Potential token standard improvements in the future could allow for OnChain challenges to force on chain activation.
Open Marketplace
  Like uniswap but for bots 
Tokenized proxies? 
  Why not go full mile and allow the same but for metered billing products like proxy traffic etc. This would have to be layer 2 for sure but the tech is ready 
