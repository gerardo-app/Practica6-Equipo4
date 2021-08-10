from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command

nr = InitNornir(
	config_file="config.yaml",  dry_run=True
	)
	# open NX-OS Nexus 3000 and 9000 family of swithches
Nex1=nr.run(netmiko_send_config, config_file = "Nexus.txt")
Nex2=nr.run(netmiko_send_config, config_file = "vlan.txt")
Nex3=nr.run(netmiko_send_config, config_commands = ["Interface lo 8","description config con Nornir 3.1.0","ip add 8.8.8.8/32"])
Nex4=nr.run(netmiko_send_command, config_string = "show ip int brief")
Nex5=nr.run(netmiko_send_command, config_string = "show vlan b")
print_result(Nex1)
print_result(Nex2)
print_result(Nex3)
print_result(Nex4)
print_result(Nex5)