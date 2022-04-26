Geo Scaling 
=====

## Beyond the datacenter
How do we approach global-scale application design? This is often solved by *geo-replication* - replicating compute/data across geographies

## Availability Zones
Early in cloud build out companies face two major problems
1. Servicing a data center can require turning it off
1. Deploying solutions to a single datacenter that can fail results in reliability/availability issues

Why does this happen?
* Some hardware components are too critical to service while active, like the datacenter power and cooling systems 

## Models for high-availability Replication 

W/in a datacenter yo can just make TCP connections and build replication solutions

B/w datacenters, communication is tricky for several reasons. Those same approaches might not work well, or at all
* Every datacenter has its own unique firewall that prevents applications from passing data to it w/out AUTHN
* Direct connections via TCP would probably be blocked, it is easy to connect from inside but it is very hard to connect from outside

## Why restrict outgoing TCP

* Datacenter networks manage millions of ip addresses inside each single datacenter
* None of these are unique, they are only unique to each datacenter or a private cloud
* Therefore, a computer in datacenter A often won't have a visible IP address to any computer in datacenter B

## Geo-replication
Geo-replication blocks code from connecting to itself

### Benefits
* Region recovery sequence
* Sequential updating
* Physical isolation
* Data residency

### Major types of storage
Locally redundant storage (LRS): Synchronously copies data across Azure availability zones