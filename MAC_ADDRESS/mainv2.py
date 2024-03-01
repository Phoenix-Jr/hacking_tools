import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option('-i','--interface',dest='interface',help='Interface to change its MAC adress')
    parser.add_option('-m','--MAC',dest='new_mac',help='New Mac address')
    (options,get_arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info.')
    elif not options.new_mac:
        parser.error('[-] Please specify an new mac, use --help for more info.')
    return options

def change_mac(interface,new_mac):
    print(f"[+] changing MAC address for {interface} to {new_mac} ")
    subprocess.call(['ifconfig',interface,'down'],shell=True)
    subprocess.call(['ifconfig',interface,'down','hw','ether',new_mac],shell=True)
    subprocess.call(['ifconfig',interface,'up'],shell=True)

def get_current_mac_address(interface):
    ifconfig_result = subprocess.check_output(['ifconfig',options.interface])
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read a MAC address")

options = get_arguments()
current_mac = get_current_mac_address(options.interface)
print('Current MAC',str(current_mac))
change_mac(options.interface,options.new_mac)
if current_mac == options.new_mac:
    print(f"[+] MAC address was successfully changed to {current_mac} ")
else:
    print('[-] Mac address did not get changed.')