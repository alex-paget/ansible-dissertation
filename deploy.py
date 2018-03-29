#!/usr/bin/python
import subprocess
import re

# Function that prompts users for yes or no response
def yes_no(answer):
    # Expected 'yes' formats
    yes = set(['yes', 'y'])
    # Expected 'no' formats
    no = set(['no', 'n'])

    # Prompt user for input until they answer either 'yes' or 'no'
    while True:
        choice = raw_input(answer).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        elif choice == "":
            return True
        else:
            print("Please respond with 'yes' or 'no'")

# Function that will write user input to file
def write_line(file, string):
    with open(file, 'a') as the_file:
        the_file.write(string)
        the_file.write("\n")

def ip_network(answer, default):
    # Validates the input of any IP network addresses
    while True:
        input = raw_input(answer)
        print(input)
        # if the input matches the format expected return it
        if re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}$", input):
            return input
        # if the input is blank use the default value
        elif input == "":
            return default
        # for anything else reprompt the user
        else:
            print("Please give the IP in this format: 192.168.0.")

def ip_client(answer, default):
    # Validates the input of any IP host addresses
    while True:
        input = raw_input(answer)
        print(input)
        # if the input matches the format expected return it
        if re.match("^(([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4]))$", input):
            return input
        # if the input is blank use the default value
        elif input == "":
            return default
        # for anything else reprompt the user
        else:
            print("Please give the host address in this format: 255")

def netmask(answer, default):
    # Validates the input of any netmasks
    while True:
        input = raw_input(answer)
        print(input)
        # if the input matches the format return it
        if re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", input):
            return input
        # if the input is blank return the default value
        elif input == "":
            return default
        # for anything else reprompt the user
        else:
            print("Please give the netmask in this format: 255.255.255.0")

def is_alphanumeric(answer, default):
    # Validates the input is alphanumeric
    while True:
        input = raw_input(answer)
        # if the input matches the format return it
        if input.isalnum() == True:
            return input
        # if the input is blank
        elif input == "":
            return default
        # for anything else reprompt the user
        else:
            print("Please only use alphanumeric characters[abc123]")

def generic(answer, default):
    # Checks to make sure the entry isn't blank
    input = raw_input(answer)
    if input == "":
        return default
    else:
        return input

def required(answer):
    # Prompts until the user enters an answer
    while True:
        input = raw_input(answer)
        if not input:
            print("Please enter a response")
        else:
            return input

def is_num(answer, default):
    # Validates the input is a number
    while True:
        input = raw_input(answer)
        # if the input matches the format return it
        if input.isdigit() == True:
            return input
        # if the input is blank return the defualt
        elif input == "":
            return default
        else:
            print("Please enter a number")

minimal = yes_no('Deploy Minimal Configuration? ')
if minimal == True:
    # BOS
    ipaddr_network = ip_network("Please enter headnode IP network[192.168.0.]: ", "192.168.0.")
    ipaddr_client = ip_client("Please enter headnode IP client address[1]: ", "1")
    sms_name = generic("Please enter the headnode hostname[headnode]: ", "headnode")
    # Enable ohpc repo
    repo = generic("Please enter the OpenHPC repo to use[http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm]:", "http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm")
    # Add provision
    ntp = generic("Please enter the NTP to use[0.centos.pool.ntp.org]: ", "0.centos.pool.ntp.org")
    # Resource management
    compute_name = is_alphanumeric("Please enter the name for the compute nodes[compute]: ", "compute")
    compute_no = is_num("Please enter the number of compute nodes[4]: ", "4")
    socket_no = is_num("Please enter the number of sockets[2]: ", "2")
    core_no = is_num("Please enter the number of cores per socket[8]: ", "8")
    threads_no = is_num("Please enter the number of threads per core[2]: ", "2")
    # Basic warewulf
    interal_interface = required("Please enter the provisioning interface for the headnode: ")
    ip_netmask = netmask("Please enter the netmask for the headnode[255.255.255.0]: ", "255.255.255.0")
    # Customise sys config
    home_mount = generic("Please enter the home mount point[/home]: ", "/home")
    opt_mount = generic("Please enter the opt mount point[/opt/ohpc/pub]: ", "/opt/ohpc/pub")
    # Register nodes core
    c_provision = required("Please enter the compute node provisioning interface: ")
    c_ipaddr_network = ip_network("Please enter the compute IP network[192.168.0.]: ", "192.168.0.")
    c_ipaddr_client = ip_client("Please enter the compute IP client start address[2]: ", "2")
    c_mac = []
    for x in range(0, int(compute_no)):
        c_mac.append(required("Please enter MAC: "))
