#!/usr/bin/python

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
        if input.isalpha() == True:
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

minimal = yes_no('Deploy Minimal Configuration\n')
if minimal == True:
    ipaddr_network = ip_network("Please enter headnode IP network[192.168.0.]: ", "192.168.0.")
    ipaddr_client = ip_client("Please enter headnoe IP client address[1]: ", "1")
    repo = generic("Please enter the OpenHPC repo to use[http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm]:", "http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm")
    ntp = generic("Please enter the NTP to use[0.centos.pool.ntp.org]: ", "0.centos.pool.ntp.org")
    compute_name = generic("Please enter the name for the compute nodes[compute]: ", "compute")
    compute_no = is_num("Please enter the number of compute nodes[4]: ", "4")




ip_network("Please enter the headnode netowrk IP address\n")

#
