Sharding 
========

Sharding and replication are one of the key ways to build software at scale. 

##  Why services slow down at scale
Lock contention: The more concurrent taasks the more likely that they will try to accesss the same object (birthday paradox) and will have to wait for mutex locks to unlock. Now and then, apps must disconnect and retry in an abort/retry sequence

## Sharding: Key ideas
All of the data is in the service, but spread out
* No single place has all of the data. Every item is a key-value pair with a unique name (id)
* Any specific data item is in some single shard, probably with 2 - 3 identical replicas holding it. 
* Applications need to be coded in  aspecial way in order to efficiently compute on sharded data

Say we have n servers, Organize them into n/s 'shards' w/ s servers each
* Normally, s = 3 | 5, N can be extremely large

Define some rule for deterministically mapping each key-value data item to a shard. Now all the data will be in the application, but will be spread out across multiple shards

## Sharding difficulties
* Sharding does not permit "multi-sharding transactions"
* Each shard must be self contained, and able to do whole job of singular database
* Cross-shard interactions reintroduce many costs that we are trying to avoid by scaling

Paging
====
3 options
1. Server state machine
1. Part of the request
1. Client state machine
   * Browser storage
     * Session state (lose when session is terminated)
     * Local store (lose when browser is terminated)
   * Cookies

State Machine Replication
====
State machine replication on shards doesn't support arbitrary transactions
* Transactions touching multiple shards require complexx locking. As we scale up, performace collapses

Replication in which each shard is totally independant works fine
* If updates and queries are done entirely on one shard

Determinism
========

Each program as code that reads input, computes the input, then produces outputs
* Always behaves identically
Non-deterministic programs might do different things on identical input

Byzantine Model
======

Everything works well if all commanders are in agreement

Without consistancy chaos ensues