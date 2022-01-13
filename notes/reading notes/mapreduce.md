# Map Reduce

## Programming Model

Takes set of input k/v pairs and defines two functions

* Map: Takes input pair and produces a set of intermediate k/v pairs, and groups them all together by their intermediate key values
  * map(k1, v1) -> list(k2, v2)

* Reduce: Accepts intermediate key and sets values for that key. It then merges those values to form a possibly smaller set of values.
  * reduce(k2, list(v2)) -> list(v2)

## Implementation

Multiple implementations exist for different system requirements  
Book environment refers to computing environment that exists in wide use at Google

* Large clusters of commondity PC's connected with Ethernet
  
  1. Machines are typically dual-processor x86 processors running Linux, with 2-4 GB of memory per machine
  1. Commodity networking hardware is used – typically either 100 megabits/second or 1 gigabit/second at the machine level, but averaging considerably less in over-all bisection bandwidth
  1. A cluster consists of hundreds or thousands of machines
     * Machine failures are common
  1. Storage is provided by inexpensive IDE disks attached directly to individual machines. A distributed file system developed in-house is used to manage the data stored on these disks. The file system uses replication to provide availability and reliability on top of unreliable hardware
  1. Users submit jobs to the system. Jobs consist of a set of tasks, and is mapped by the scheduler to a set of available machines in the cluster

  