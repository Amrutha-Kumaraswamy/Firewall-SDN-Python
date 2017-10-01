# Firewall-SDN-Python

Advanced Topology
PART B:
	1.	Login into Mininet
						username : mininet 
						password : mininet
	2.	run " sudo dhclient eth1 " to enable to allow network access in the VM
	3.	Open 2 SSH terminals and login using same credentials as above with X11 forwarding (i.e ssh -X mininet@192.168.x.x) or use putty to login (with X11 forwarding)
	4. run "sudo mn --topo single,3 --mac --switch ovsk --controller remote" to create and start the topology.
	5. The topology would be made and the prompt would be " mininet > "
	6. In one, copy the modified topology file "advtopo.py" into mininet/pox/pox/misc
	7. execute "sudo mn --custom advtopo.py --topo mytopo --mac --controller remote" to start the topology
	8. The topology is now created and the shell shows mininet> prompt
	9. Copy the controller code to mininet/pox/pox/misc as adv_tut.py
	10. change to directory mininet/pox (alternatively do cd ../..)
	11. Execute " ./pox.py log.level --DEBUG misc.adv_tut " to start the controller
	12. In the mininet terminal , execute "h3 ping -c1 h5" to ping host h5 from h3 and check the flow of packet on the controller
	13. In the mininet> prompt in the shell, execute "pingall" to ping every host from every other host.
	14. from mininet terminal which has mininet> prompt in the shell, execute "h3 ping -c1 10.0.2.2" to ping the router from h3.
	15. in the controller terminal. we can see the ICMP reply sent.
	16.from mininet terminal which has mininet> prompt in the shell, execute "h3 ping -c1 10.0.100.2" to ping the router from h3.
	18. in the controller terminal. we can see the unreachable destination message
	19. mininet terminal shows the ping statistics, which says that the packet has been lost as host is unreachable
	20.Run iperf in the mininet> shell, to view the bandwidth
	21. Exit the controller and kill all its instances by finding the pid using "ps -eaf | grep "controller" " and kill -9 <pid>

	FIREWALL : 
	
	22. On "mininet >" ,open terminal h3 and h5
	23. on h3 terminal "iperf -s"
	24. on terminal h5, "iperf -c 10.0.1.2"
	24. observe the normal working before implementing firewall
	25. Close the terminals - xterm
	26. On the mininet terminal , type "h3 ping -c1 h4"
	27. Note the sucessful ping in the controller terminal
	26. Exit the controller and kill all its instances by finding the pid using "ps -eaf | grep "controller" " and kill -9 <pid>
	27.  Copy the modified topology file "of_tutorial2_fw.py" into mininet/pox/pox/misc with firewall to block IP 10.0.1.2
	28. change to directory mininet/pox (alternatively do cd ../..)
		Execute " ./pox.py log.level --DEBUG misc.of_tutorial2_fw " to start the controller
	29. On "mininet >" ,open terminal h3 and h5 using "xterm h3 h5"
	30. on h3 terminal "iperf -s"
	31. on terminal h5, "iperf -c 10.0.1.2"
	32. observe the firewall bloking the pings
	33. exit the xterms
	34. On the mininet terminal , type "h3 ping -c1 h4"
	35. Note the blocking on the controller terminal


