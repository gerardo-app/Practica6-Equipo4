from nornir import InitNornir
from normir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command

nr = InitNornir(
	config_file="config.yaml",  dry_run=True
	)
	# open NX-OS Nexus 3000 and 9000 family of swithches
	next1=nr.run(netmiko_send_config, config_file = "Nexus")
	next2=nr.run(netmiko_send_config, config_file = "vlan")
	next3=nr.run(netmiko_send_config, config_commands = ["Interface lo 6","description config con Nornir 3.1.0","ip add 6.6.6.6/32"])
	next4=nr.run(netmiko_send_config, config_string = "show ip int brief")
	next5=nr.run(netmiko_send_config, config_string = "show vlan b")
	print_result(Next1)
	print_result(Next2)
	print_result(Next3)
	print_result(Next4)
	print_result(Next5)

