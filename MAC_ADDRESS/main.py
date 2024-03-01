import subprocess
import optparse

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

options = get_arguments()
change_mac(options.interface,options.new_mac)
