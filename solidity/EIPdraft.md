
ERC-TBD License Standard 

## Simple Summary
A tokenized key for limited release software licenses that allows for secondary markets. 

## Abstract 
The following standard allows for the implementation of a standard API for tokens within smart contracts. This standard provides basic functionality to transfer tokens, as well as allow tokens to be approved so they can be spent by another on-chain third party.



## Motivation
In the sneaker bot community software licenses are very limited. because of this there is a secondary market price for license keys. This secondary market is dependent on expensive 3rd party escrows for trading which run a risk of losing their keys. Bot developers commonly use centralized chat applications for their authentication of users, this places an uncessasary burden on developers and risk as the centralized service can ban the developer account and users lose their keys. 

# Specification 

## Token

### Methods

#### Name 

Returns the name of the license token - e.g. "MyBot"
OPTIONAL - This method can be used to improve usability, but interfaces and other contracts MUST NOT expect these values to be present.

```function name() public view returns (string) ```
