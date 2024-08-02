## step 1:
On line 351 change value of **bool tracing** to **true**.
## step 2:
On line 345, you can change value of **std::string transport_prot** to any of the protocol from lines 366 to 369 (or leave it to "TcpWestwoodPlus").
## step 3:
Run the ns3 program (no need of visualizer i.e. *--vis*).
## step 4:
Go to ns3 folder and find a **.cwnd** file, paste all the values from the file in a spreadsheet (Libre-Office) and generate its graph (click insert -> chart -> preferably line graph).
## step 5:
Repeat **step 4** for a **.rtt** file.
## step 6:
On line 345 change value of **std::string transport_prot** to some other protocol and and repeat steps 3, 4 and 5 again.
#### Finally you will have 4 graphs as observation/output