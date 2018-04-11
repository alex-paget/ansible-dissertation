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

def ip_full(answer, defualt):
    # Validates the input of any full IP addresses
    while True:
        input = raw_input(answer)
        print(input)
        # if the input matches the format expected return it
        if re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", input):
            return input
        # if the input is blank use the default value
        elif input == "":
            return default
        # for anything else reprompt the user
        else:
            print("Please give the full IP address in this format: 192.168.0.1")


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

def efi_legacy(answer):
    # Validates that the user entered an expected answer
    while True:
        input = raw_input(answer).lower()
        if input == "efi":
            return "efi"
        elif input == "legacy":
            return "legacy"
        else:
            print("Please enter efi or legacy")

def compiler(answer):
    # Validates that the user entered an expected answer
    while True:
        input = raw_input(answer).lower()
        if input == "gnu":
            return "gnu"
        elif input == "llvm":
            return "llvm"
        else:
            print("Please enter gnu or llvm")

def mpi(answer):
    # Validates that the user entered an expected answer
    while True:
        input = raw_input(answer).lower()
        if input == "ethernet":
            return "ethernet"
        elif input == "infiniband":
            return "infiniband"
        elif input == "opa":
            return "opa"
        elif input == "pmix":
            return "pmix"
        else:
            print("Please enter openmpi, mpich, or mvapich")

def default_dev(answer):
    # Validates that the user entered an expected answer
    while True:
        input = raw_input(answer).lower()
        if input == "openmpi":
            return "openmpi"
        elif input == "mpich":
            return "mpich"
        elif input == "mvapich":
            return "mvapich"
        else:
            print("Please enter openmpi, mpich, or mvapich")

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
    # Install BOS
    chroot = generic("Please enter the chroot location[/opt/ohpc/admin/images/centos7.4]: ", "/opt/ohpc/admin/images/centos7.4")
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
    # Boot nodes
    bmc_network = ip_network("Please enter the BMC network address[192.168.1.]: ", "192.168.0.")
    bmc_client = ip_client("Please enter the BMC client start address[2]: ", "2")
    bmc_user = required("Please enter the BMC username: ")
    bmc_password = required("Please enter the BMC password: ")
else:
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
    # Infiniband support
    infiniband_support = yes_no("Add Infiniband Support? ")
    if infiniband_support == True:
        ib_network = ip_network("Please enter the IB network for the headnode[192.168.5.]: ", "192.168.5.")
        ib_client = ip_client("Please enter the IB client address for the headnode[1]: ", "1")
    # Omnipath base
    omnipath_base = yes_no("Add omnipath base? ")
    # Basic warewulf
    interal_interface = required("Please enter the provisioning interface for the headnode: ")
    ip_netmask = netmask("Please enter the netmask for the headnode[255.255.255.0]: ", "255.255.255.0")
    # Install BOS
    chroot = generic("Please enter the chroot location[/opt/ohpc/admin/images/centos7.4]: ", "/opt/ohpc/admin/images/centos7.4")
    # Customise sys config
    home_mount = generic("Please enter the home mount point[/home]: ", "/home")
    opt_mount = generic("Please enter the opt mount point[/opt/ohpc/pub]: ", "/opt/ohpc/pub")
    # Infiniband drivers compute
    c_infiniband_support = yes_no("Add Infiniband Support to compute nodes? ")
    # mem limit
    mem_limit = yes_no("Increase locked memory limit? ")
    # SSH control
    ssh = yes_no("Enable SSH control via resource manager?" )
    # Beegfs
    beegfs = yes_no("Add Beegfs to cluster? ")
    if beegfs == True:
        beegfs_repo = generic("Please enter Beegfs repo[https://www.beegfs.io/release/latest-stable/dists/beegfs-rhel7.repo]: ", "https://www.beegfs.io/release/latest-stable/dists/beegfs-rhel7.repo")
        beegfs_ip = ip_full("Please enter the Beegfs IP address[192.168.0.254]: ", "192.168.0.1")
    # Lustre
    lustre = yes_no("Add Lustre to cluster? ")
    if lustre == True:
        lustre_mount = generic("Please enter the Lustre mount point[/mnt/lustre]: ", "/mnt/lustre")
        lustre_ip = ip_full("Please enter the Lustre IP[192.168.0.254]: ", "192.168.0.254")
    # Forward logs
    logs = yes_no("Forward logs from compute nodes to headnode? ")
    # Nagios
    nagios = yes_no("Add Nagios Monitoring to cluster? ")
    if nagios == True:
        nagios_user = is_alphanumeric("Please enter the Nagios Admin username[admin]: ", "admin")
        nagios_pass = is_alphanumeric("Please enter the Nagios Admin password[password]: ", "password")
    # Ganglia
    ganglia = yes_no("Add Ganglia to cluster? ")
    # Clustershell
    clustershell = yes_no("Add Clustershell to cluster? ")
    # Mrsh
    mrsh = yes_no("Add Mrsh to cluster? ")
    # Genders
    genders = yes_no("Add genders to cluster? ")
    if genders == True:
        bmc_network = ip_network("Please enter the BMC IP network[192.168.1.]: ", "192.168.1.")
        c_bmc_client = ip_client("Please enter the BMC IP client compute start address[2]: ", "2")
    # Conman
    conman = yes_no("Add Conman to cluster? ")
    if conman == True:
        if bmc_network != "":
            bmc_network = ip_network("Please enter the BMC IP network[192.168.1.]: ", "192.168.1.")
            c_bmc_client = ip_client("Please enter the BMC IP client compute start address[2]: ", "2")
            c_bmc_user = is_alphanumeric("Please enter the BMC username[admin]: ", "admin")
            c_bmc_password = is_alphanumeric("Please enter the BMC password[password]: ", "password")
    # Import files core
    # Import files ib
    # Bootstrap kernel
    bootstrap_kernel = yes_no("Add additional kernel arguments to bootstrap? ")
    # Bootstrap Singularity
    bootstrap_singularity = yes_no("Add Singularity arguments to kernel? ")
    # Bootstrap
    # VNFS
    # Register nodes core
    c_provision = required("Please enter the compute node provisioning interface: ")
    c_ipaddr_network = ip_network("Please enter the compute IP network[192.168.0.]: ", "192.168.0.")
    c_ipaddr_client = ip_client("Please enter the compute IP client start address[2]: ", "2")
    c_mac = []
    for x in range(0, int(compute_no)):
        c_mac.append(required("Please enter MAC: "))
    # Register nodes IB
    if infiniband_support == True:
        c_ipoib_network = ip_network("Please enter the compute IPoIB network[192.168.5.]: ", "192.168.5.")
        c_ipoib_client = ip_client("Please enter the compute IPoIB client start address[2]: ", "2")
    # Register nodes predictable
    register_predictable = yes_no("Set compute interface names? ")
    # Stateful
    stateful = yes_no("Deploy nodes in stateful configuration? ")
    if stateful == True:
        stateful_mode = efi_legacy("Deploy nodes as efi or legacy?")
    # Boot nodes
    # Development
    dev = yes_no("Install Development Tools? ")
    if dev == True:
        compiler = compiler("Which compiler should be installed: gnu or llvm? ")
        mpi = mpi("Which MPI stack should be installed: ethernet, infiniband, opa, or pmix? ")
        default_dev = default_dev("Which toolchain should be installed: openmpi, mpich, or mvapich?")
        performance_tools = yes_no("Install performance tools? ")
    # Resource startup

# Write to file
user_defined = [ipaddr_network, ip_client, sms_name, repo, ntp, compute_name, compute_no, socket_no, core_no, threads_no, interal_interface, ip_netmask, chroot, home_mount, opt_mount, bmc_network, c_bmc_client, c_bmc_user, c_bmc_password, c_provision, c_ipaddr_network, c_ipaddr_client]
for x in range(len(user_defined)):
    if user_defined[x] != "":
        print(user_defined[x])
for x in range(len(c_mac)):
    print(c_mac[x])
if infiniband_support != "":
    print(infiniband_support)
    print(ib_network, ib_client)
if omnipath_base != "":
    print(omnipath_base)
if c_infiniband_support != "":
    print(c_infiniband_support)
    print(c_ipoib_network, c_ipoib_client)
if mem_limit != "":
    print(mem_limit)
if ssh != "":
    print(ssh)
if beegfs != "":
    print(beegfs)
    print(beegfs_repo, beegfs_ip)
if lustre != "":
    print(lustre)
    print(lustre_mount, lustre_ip)
if logs != "":
    print(logs)
if nagios != "":
    print(nagios)
    print(nagios_user, nagios_pass)
if ganglia != "":
    print(ganglia)
if clustershell != "":
    print(clustershell)
if mrsh != "":
    print(mrsh)
if genders != "":
    print(genders)
if conman != "":
    print(conman)
if bootstrap_kernel != "":
    print(bootstrap_kernel)
if bootstrap_singularity != "":
    print(bootstrap_singularity)
if register_predictable != "":
    print(register_predictable)
if stateful_mode == "efi":
    print("efi")
elif stateful_mode == "legacy":
    print("legacy")
else:
    print("stateful empty")
if dev != "":
    print(dev)
    user_dev = [compiler, mpi, default_dev, performance_tools]
    for x in range(len(user_dev)):
        if user_dev[x] != "":
            print(user_dev[x])
