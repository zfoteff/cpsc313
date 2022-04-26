Block Chain
=====

# Gossip Protocol
W/in a cloud computing environment we need to manage large pools of computers / services
* What is thie

## Gossip Basics
Suppose that Anne tells me something. I'm sitting next to Fred, and I tell him. Later, he tells Mimi and I tell Frank.

Each round doubles the number of people who know the secret
* A round is a generation of people sharing the secret to a decendant group of people

This is an example of a *push epidemic*

## Push - Pull Gossip
Sometimes, the basic model is expanded to include multiple channels of communication

* Process P decides to gossip with process Q
* P sends Q some form of concise "digest" of available information
* Q sends back its own digest, plus a list of items it wants from P
* P reponds with the requested items, plus a list of items it wants from Q
* Q sends the requested information

This avoids large object duplication

# Gossip Protocols at Scale

This describes the movement of information access across a p2p network
* Similar to the spread of a virus through a population
* Tends to run in very consistant and decentralized manner

Nodes must choose other Nodes at random with which to communicate

Advantages
* Fault tolerance - Nodes distribute information with multiple other nodes
* Scalability - Infomation is spread efficiently across large networks
* Robustness - No node in the network plays a specific role
  * Failed nodes willnot prevent other nodes from continuing to send messages

# Types of Gossip Protocol

Dissemination (rumor mongering): Spread information through the network by flooding agents in a manner that produces bounded worst-case loads
* Background data dissemination: continuous and rapid
* Even dissemination: multicast

Aggregation: Calculate aggregates by sampling nodes and extrapolating system-wide metric

Anti-entropy: Nodes choose a random partner with which to share data
* Used mainly in systems without strong consistancy requirements
* Repair data and reconcile missing records to keep the nodes in sync 

# Gossip in distributed systems
We can gossip about membership
* This may require a bootstrap mechanism, then discuss failures and new members

Gossip to repair faults in replicated data
* "I have 6 updates from charlie"

# Gossip Limitations
Gossip is robust, but LogN time may not be fast enough

# Blockchain
Blockchain: P2P, decentralized, immutable, shared electronic transactional ledger

Digital information (blocks) are stored together to form a database (chain)
