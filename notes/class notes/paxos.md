Paxos made simple 
=================
# The consensus algorithm
## The problem
Assume a collection of processes that can propose values exists. The consensus algorithm ensures that a single one among the values should be chosen
* If no value has been proposed, then no value should be chosen
* If a value has been chosen, then processes should be able to learn the chosen value

Safety requirements for the algorithm are as follows:
* Only a value that has been proposed may be chosen
* Only a single value is chosen
* A process never learns a value that has been chosen unless it actually has been

### Agents
Let there be three roles in the consensus algorithm that are performed by three kinds of agents
* **Proposers**
* **Acceptors**
* **Learners**

A single process may act as more that one agent  
Assume agents communicate with each other by sending messages using an asynchronous, non-Byzantine model (Byzantine fault tolerance can be achieved if the correctly working processes in the network reach an agreement on their values, we're not worried about agreement)

In this non-Byzantine model
* Agents 
  * operate at arbitrary speed
  * may fail after value has been chosen
  * may fail by stopping
  * may restart
* Messages
  * Take arbitrarily long to delivered
  * Can be duplicated
  * Can be lost
  * Are Not corrupted

A solution is impossible unless some information can be remembered by an agent that has failed and restarted

## Choosing a value
**Approach one**  
The easiest way to choose a value is to have a single acceptor agent. A proposer sends a proposal to the acceptor, who chooses the first proposed value it receives.
* This isn't the best because a failing acceptor makes any further progress impossible

**Approach two**
Use multiple acceptor agents. A proposer sends a proposed value to a set of acceptors. An acceptor agent may accept the proposed value if a large enough set of acceptors have also accepted this value  
How large of acceptance rate is large enough?  
In the absence of failure or message loss, we want a value to be chosen even if only one value is proposed by a single proposer  
This creates a new requirement ***P1***: An acceptor must accept the first proposal it receives

This requirement raises a problem: several values could be prosed by different proposers at about the same time  
***P1*** and the requirement that a value is chosen only when it is accepted by a majority of acceptors imply that an acceptor must be allowed to accept more than one proposal. We keep track of different proposals that an acceptor can accept by assigning a number to each proposal, creating a key-value pair.

A value is chosen when a single proposal with that value has been accepted by a majority of the acceptors. *This is the case in which we say a value has been accepted*

We can allow multiple proposals to be chosen, but we must guarentee that all chosen proposals have the same value. This guarantees:
* If a a proposal with the value v is chosen, then every high-numbered proposal that is chosen has value v (***P2***)

Because communication is async, a proposal could be chosen with some acceptor c having never received any proposal

## Implementation

### Phase 1
A proposer selects a proposal number n and sends a prepare request with n to a majority of acceptors
* If an acceptor receives a prepare request with number n greater than that of any prepare request it which it has already responded, then it responds with a promise not to accept more proposals numbered less than n

### Phase 2
If the proposer receives a response to its prepare requests from most acceptors, then it sends an accept request to each acceptor for a proposal numbered n with the value v of the hightest numbered proposal amoung the responses  
If an acceptor recieves an accept request for a proposal, it accepts the proposal unless it has already responsed to a prepare request with a higher sequence number  
