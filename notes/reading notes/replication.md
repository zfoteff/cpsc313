# Replication reading notes

## Abstract

Transactional replication has unstable behavior as workload scales up.

* 10x increase in nodes and traffic gives a 1000x increase in deadlocks or reconcilications 

Master - Copy replication (primary copy) pattern reduces the complexity

## Replication Schemes

Data is replicated at multiple network nodes for performance and availability  
**Eager replication** keeps all replicas exactly syncronized at all nodes by updating all replicas in one atomic transaction  

* Reduces update performance and increases transacion response time due to extra updates and messages added to the payload
* Not an option for mobile devices

**Lazy replication** asyncronously propogate replica updates to other nodes after updating transactions conclude

* Can result in stale data
* Typically use locking schemes to regulate concurrent execution

Lazy  replication has  a  more  difficult  task  because  some  replica  updates  have already been committed when the serialization problem is first detected. There is usually no automatic way to reverse the committed replica  updates, rather a program or person must *reconcile* conflicting transactions

* Conflicts are reconciled by waiting or mutex deadlock

 ```plaintext
 To  make  this  tangible,  consider  a  joint  checking  account 
you share with your spouse.  Suppose it has $1,000 in it.  
This  account  is  replicated  in  three  places:  your  check-
book, your spouse’s checkbook, and the bank’s ledger.  
 
Eager  replication  assures  that  all  three  books  have  the 
same  account  balance.    It  prevents  you  and  your  spouse 
from writing checks totaling more than $1,000.  If you try 
to overdraw your account, the transaction will fail.   
 
Lazy replication allows both you and your spouse to write 
checks totaling $1,000 for a  total of $2,000 in withdraw-
als.  When these checks arrived at the bank, or when you 
communicated  with  your  spouse,  someone  or  something 
reconciles the transactions that used the virtual $1,000
```

Master - copy patterns automate the reconciliation by treating the Bank's master copy as the definitive source of data. Though this means that all copies are constantly working to catch up to the master, and can be greviously thrown of their calculations if their data is stale

## Non-Transactional Replication Schemes

Updates to real life databases (bibles, phone books) are typically updated in a lazy-master way

## Two-tier Replication

Ideal replication schemes should achive four goals

1. **Availability and Scalability**:  Provide  high  availability and scaleability through replication, while avoiding instability
1. **Mobility**: Allow mobile nodes to read and update the database while disconnected from the network
1. **Serializability**: Provide single-copy serializable transaction execution
1. **Convergence**: Provide convergence to avoid system delusion

Eager and Lazy replication systems are the safest, as they avoid system delusion. They have no reconciliation problems because there is not reconciliation. There are problems that have been expressed earlier

1. Mastered objects cannot accept updates if the master node is not accessible. This makes it difficult to use master replication for mobile applications.
1. Master systems are unstable under increasing load. Deadlocks rise quickly as nodes are added.
1. Only eager systems and lazy master (where reads go to the master) give ACID serializability.

The solution requires a modified mastered replication scheme

### The two-tier replication scheme

The two-tier replication scheme begins by assuming there are two kinds of nodes

1. **Mobile nodes**: Disconnected most of the time. Store replicas of the database and may act as source of *tentative transactions*.
    * The node may be the master of some data items

1. **Base nodes**: Always connected: They store a replica of the database. Most items are sourced from base nodes

Replicated data items have two versions at mobile nodes

1. **Master Version**: Most recent value recieved from object master. The version at the object master is the master version, but disconnected or lazy replica nodes may have older versions.
1. **Tentative Version**: The local object may be updated by tentative transactions. The most recent value, due to local updates, is maintained as a tentative version

There are two kinds of transactions in two-tier replication scheme

1. **Base transaction**: Work only on master data, and produce new master data and they produce new master data. They involve at most one connected-mobile node and may involve several base nodes
    * Has acceptance criterion: Tests the resulting outputs must pass for the slightly different base transaction results to be acceptable
      * If it fails, the origin node and th person who generated the transaction are informed it failed and why it failed
1. **Tentative transactions**: Work on local tentative data. They produce new tentative versions. They also produce a base transaction to be run at a later time on the base nodes
    * Must follow a score rule: The mobile node and all the base nodes will be in contact when the tentative transaction is processed as a real base transaction. The real transaction will be able to read the master copy of each item in the scope

## Summary

Replicating data at many nodes and letting anyone update the data is problamatic. Security and performace both suffer.  
The solution appears to include

* Using semantic tips: timestamps, commutative transactions
* Using two-tier replication scheme
  * Supports mobile nodes * combined benefits of eager-master-replication scheme and local update scheme