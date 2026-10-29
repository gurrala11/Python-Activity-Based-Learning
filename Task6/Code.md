## 51. Bus Passenger Occupancy Simulation

### 1. Problem Statement

To calculate passenger counts at each bus stop using boarding and alighting numbers and check whether bus capacity is exceeded.

### 2. Algorithm

1. Read bus capacity and number of stops.
2. Read boarding and alighting counts.
3. Calculate current passengers.
4. Display passenger count and capacity status.

### 3. Flowchart 
```mermaid

flowchart TD
    A([Start]) --> B[/Enter capacity and stops/]
    B --> C[/Enter boarding and alighting/]
    C --> D[Update passenger count]
    D --> E{Count > capacity?}
    E -- Yes --> F[Capacity exceeded]
    E -- No --> G[Within capacity]
    F --> H{More stops?}
    G --> H
    H -- Yes --> C
    H -- No --> I([End])
```

### 5. Sample Input

Bus capacity: 40
Number of stops: 2
Boarding: 20
Alighting: 0
Boarding: 25
Alighting: 5


### 6. Sample Output

Passengers: 20
Within capacity
Passengers: 40
Within capacity

