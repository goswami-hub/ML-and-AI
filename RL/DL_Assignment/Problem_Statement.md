# Problem Statement
SuperCabs is a leading app-based cab provider in a large Indian metro city. The goal of our project is to build an RL-based algorithm which can help cab drivers maximise their profits by improving their decision-making process on the field. Thus, it is important that drivers choose the 'right' rides, i.e. choose the rides which are likely to maximise the total profit earned by the driver that day. 

## Assumptions:
 1. Taxis are electric cars. It can run non stop for 30 days (i.e. 720 hours). Then it needs to recharge itself.If the driver is completeing a trip at that time , he'll finish the trip and then stop for charging. Therefore, there is one and only ** Terminal state** that defines an **episode** at end of 720 hr ride (or after the last drive crossing 720th hour).
 2. There are only five locations where a driver can pick-up or drop 
 3. All decisisons are made at hourly intervals
 4. The time taken to travel from one place to other place depends on place (pick up/ drop), hour of the day and day of the week. The travel duration is given through **TM.npy** file.

 ## Important definitions
 ### State
 The state space is defined by the drivers current location along with the time components
 $$ S = X_{i} T_{j} D_{k} $$ 
 Xi = i th location $i= 0, 1 ,2 ,3, 4$ <br>
 Tj = j th hour of the day $j= 0, 1, 2, ...., 22, 23$ <br>
 Dk = kth day $k= 0, 1, 2, 3, ...., 29$<br>

 ### Action
 Action is a combination of pick up and drop
 $$ A = { (p,q): p= 0,1,2,..,4 \ and \ q=0,1,...,4 , \ p \neq q } $$
 However (0,0) is always an option to driver to rmail offline , i.e. take no request. <br>

 ### Requests
 The number of request received from a location follows a Poisson distribution: <br>


 |Location|λ|
 |---|---|
 |0|2|
 |1|12|
 |2|4|
 |3|7|
 |4|3|

 If the number of requests > 15 , then only first 15 requests are considered.
 If the number of requests is 0 , then driver stays offline (0,0).
 

    


