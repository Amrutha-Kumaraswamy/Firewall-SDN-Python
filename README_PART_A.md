# Firewall-SDN-Python

PART A : 
	1.	Login into Mininet
						username : mininet 
						password : mininet
	2.	run " sudo dhclient eth1 " to enable to allow network access in the VM
	3.	Open 2 SSH terminals and login using same credentials as above with X11 forwarding (i.e ssh -X mininet@192.168.x.x) or use putty to login (with X11 forwarding)
	4. run "sudo mn --topo single,3 --mac --switch ovsk --controller remote" to create and start the topology.
	5. The topology would be made and the prompt would be " mininet > "
	6. On another terminal , login using step 1,2 and 3. Copy of_tutorial.py into ./pox/pox/misc
	7. cd ../.. and run ./pox.py log.level --DEBUG misc.of_tutorial to start the controller (currently works as hub)
	8. Go to mininet> console and type " mininet> xterm h1 h2 h3" to open the terminals for the 3 hosts 
	9. Run the tcp dump on h2 and h3 by following steps
	10. In terminal of h2 :  # tcpdump -XX -n -i h2-eth0
		In terminal of h3 :  # tcpdump -XX -n -i h3-eth0
	11. In terminal of h1 :  # ping -c1 10.0.0.2 to see reply from existing hosts
	12. In terminal of h1 :  # ping -c1 10.0.0.100 to see reply from non-existing hosts
	13. close the xterms
	13. Exit the controller and kill all its instances by finding the pid using "ps -eaf | grep "controller" " and kill -9 <pid>
	
	Act As Switch : 
	
	13. copy the file  of_tutorial_switch.py into mininet/pox/pox/misc
	14. cd ../.. and run ./pox.py log.level --DEBUG misc.of_tutorial_switch to start the controller (currently works as switch)
	15. repeat steps 8-12
	16. Close the three xterm terminals and run iperf in the mininet> shell, to view the bandwidth
	17. Exit the controller and kill all its instances by finding the pid using "ps -eaf | grep "controller" " and kill -9 <pid>
	
	Act As Router :
	
	18. Login into Mininet
						username : mininet 
						password : mininet
	19.	run " sudo dhclient eth1 " to enable to allow network access in the VM
	20.	Open 2 SSH terminals and login using same credentials as above with X11 forwarding (i.e ssh -X mininet@192.168.x.x) or use putty to login (with X11 forwarding)
	21. In one, copy the modified topology file "mytopo.py" into mininet/pox/pox/misc
	22. execute "sudo mn --custom mytopo.py --topo mytopo --mac --controller remote" to start the topology
	23. now that terminal will show "mininet >" prompt 
	24. type  mininet> pingall to check connectivity . Without controller ping will fail. 
	25. Copy the of_router.py file into folder mininet/pox/pox/misc
	26.cd ../.. (go to mininet/pox directory)
	27. In other terminal execute " ./pox.py log.level --DEBUG misc.of_tutorial_router" to start the controller and now ping all would be successfull for if step 24 is repeated
	28. execute "h1 ping -c1 h2" to ping host h2 from h1 in mininet terrminal 
	29. Note the packtes and ping statistics on the controller terminal
	30. Attempt to ping known host my typing "h1 ping -c1 10.0.2.100" on the mininet terminal and Note the packtes and ping statistics on the controller terminal
	31. Attempt to ping unknown host my typing "h1 ping -c1 10.0.100.100" on the mininet terminal and Note the packtes and ping statistics on the controller terminal
	32. Run iperf in the mininet> shell, to view the bandwidth

