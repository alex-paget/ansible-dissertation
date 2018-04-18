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
    # External IP
    ipaddr_network_ex = ip_network("Please enter external IP network[192.168.0.]: ", "192.168.0.")
    ipaddr_client_ex = ip_client("Please enter external IP client address[1]: ", "1")
    with open('hosts', 'w') as the_file:
        the_file.write('{0}\n{1}\n{2}\n{3}\n{4}{5}{6}\n'.format("all:", " hosts:", "  headnode:", "   ansible_port: 22", "   ansible_host: ", ipaddr_network_ex, ipaddr_client_ex))
    # BOS
    ipaddr_network = ip_network("Please enter headnode IP network[192.168.0.]: ", "192.168.0.")
    ipaddr_client = ip_client("Please enter headnode IP client address[1]: ", "1")
    buffer = "sms_ip: " + ipaddr_network + ipaddr_client + "\n"
    with open('./group_vars/all', 'w') as the_file:
        the_file.write(buffer)
    sms_name = generic("Please enter the headnode hostname[headnode]: ", "headnode")
    buffer = "sms_name: " + sms_name + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'w') as the_file:
        the_file.write('{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n'.format("# This playbook deploys the whole OpenHPC software stack", "", "- name: Deploy OpenHPC", "  hosts: all", "  remote_user: afpaget", "  become: yes", "  become_method: sudo", "", "  roles:", "     - install_bos"))
    # Enable ohpc repo
    repo = generic("Please enter the OpenHPC repo to use[http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm]:", "http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm")
    buffer = "ohpc_repo: " + repo + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write('     - enable_ohpc_repo\n')
    # Add provision
    ntp = generic("Please enter the NTP to use[0.centos.pool.ntp.org]: ", "0.centos.pool.ntp.org")
    buffer = "ntp_server: " + ntp + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a')as the_file:
        the_file.write("     - add_provision\n")
    # Resource management
    compute_name = is_alphanumeric("Please enter the name for the compute nodes[compute]: ", "compute")
    buffer = "c_name: " + compute_name + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    compute_no = is_num("Please enter the number of compute nodes[4]: ", "4")
    buffer = "num_computes: " + compute_no + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    socket_no = is_num("Please enter the number of sockets[2]: ", "2")
    buffer = "num_sockets: " + socket_no + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    core_no = is_num("Please enter the number of cores per socket[8]: ", "8")
    buffer = "num_cores: " + core_no + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    threads_no = is_num("Please enter the number of threads per core[2]: ", "2")
    buffer = "num_threads: " + threads_no + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - resource_management\n")
    # Basic warewulf
    interal_interface = required("Please enter the provisioning interface for the headnode: ")
    buffer = "sms_eth_internal: " + interal_interface + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    ip_netmask = netmask("Please enter the netmask for the headnode[255.255.255.0]: ", "255.255.255.0")
    buffer = "sms_netmask: " + ip_netmask + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - basic_warewulf\n")
    # Install BOS
    chroot = generic("Please enter the chroot location[/opt/ohpc/admin/images/centos7.4]: ", "/opt/ohpc/admin/images/centos7.4")
    buffer = "chroot: " + chroot + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a')as the_file:
        the_file.write("     - initial_bos_image\n")
    # OHPC components
    with open('site.yml', 'a')as the_file:
        the_file.write("     - ohpc_components\n")
    # Customise sys config
    home_mount = generic("Please enter the home mount point[/home]: ", "/home")
    buffer = "home_mount: " + home_mount + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    opt_mount = generic("Please enter the opt mount point[/opt/ohpc/pub]: ", "/opt/ohpc/pub")
    buffer = "opt_mount: " + opt_mount + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - customise_sys_config\n")
    # import files cores
    with open('site.yml', 'a')as the_file:
        the_file.write("     - import_files_core\n")
    # bootstrap_core
    with open('site.yml', 'a')as the_file:
        the_file.write("     - bootstrap_core\n")
    # VNFS
    with open('site.yml', 'a')as the_file:
        the_file.write("     - vnfs\n")
    # Register nodes core
    c_provision = required("Please enter the compute node provisioning interface: ")
    buffer = "eth_provision: " + c_provision + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    c_ipaddr_network = ip_network("Please enter the compute IP network[192.168.0.]: ", "192.168.0.")
    buffer = "c_ip: " + c_ipaddr_network + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    c_ipaddr_client = ip_client("Please enter the compute IP client start address[2]: ", "2")
    buffer = "c_ip_last: " + c_ipaddr_client + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    c_mac = []
    for x in range(0, int(compute_no)):
        c_mac.append(required("Please enter MAC: "))
    with open('./group_vars/all', 'a') as the_file:
        the_file.write("c_mac: \n")
    for i in range(len(c_mac)):
        buffer = "  - " + c_mac[i] + "\n"
        with open('./group_vars/all', 'a') as the_file:
            the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - register_nodes_core\n")
    # Boot nodes
    bmc_network = ip_network("Please enter the BMC network address[192.168.1.]: ", "192.168.0.")
    buffer = "bmc_host: " + bmc_network + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    bmc_client = ip_client("Please enter the BMC client start address[2]: ", "2")
    buffer = "bmc_ip: " + bmc_client + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    bmc_user = required("Please enter the BMC username: ")
    buffer = "bmc_username: " + bmc_user + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    bmc_password = required("Please enter the BMC password: ")
    buffer = "bmc_password: " + bmc_password + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - boot_nodes")
else:
    # External IP
    ipaddr_network_ex = ip_network("Please enter external IP network[192.168.0.]: ", "192.168.0.")
    ipaddr_client_ex = ip_client("Please enter external IP client address[1]: ", "1")
    with open('hosts', 'w') as the_file:
        the_file.write('{0}\n{1}\n{2}\n{3}\n{4}{5}{6}\n'.format("all:", " hosts:", "  headnode:", "   ansible_port: 22", "   ansible_host: ", ipaddr_network_ex, ipaddr_client_ex))
    # BOS
    ipaddr_network = ip_network("Please enter headnode IP network[192.168.0.]: ", "192.168.0.")
    ipaddr_client = ip_client("Please enter headnode IP client address[1]: ", "1")
    buffer = "sms_ip: " + ipaddr_network + ipaddr_client + "\n"
    with open('./group_vars/all', 'w') as the_file:
        the_file.write(buffer)
    sms_name = generic("Please enter the headnode hostname[headnode]: ", "headnode")
    buffer = "sms_name: " + sms_name + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'w') as the_file:
        the_file.write('{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n'.format("# This playbook deploys the whole OpenHPC software stack", "", "- name: Deploy OpenHPC", "  hosts: all", "  remote_user: afpaget", "  become: yes", "  become_method: sudo", "", "  roles:", "     - install_bos"))
    # Enable ohpc repo
    repo = generic("Please enter the OpenHPC repo to use[http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm]:", "http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm")
    buffer = "ohpc_repo: " + repo + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write('     - enable_ohpc_repo\n')
    # Add provision
    ntp = generic("Please enter the NTP to use[0.centos.pool.ntp.org]: ", "0.centos.pool.ntp.org")
    buffer = "ntp_server: " + ntp + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a')as the_file:
        the_file.write("     - add_provision\n")
    # Resource management
    compute_name = is_alphanumeric("Please enter the name for the compute nodes[compute]: ", "compute")
    buffer = "c_name: " + compute_name + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    compute_no = is_num("Please enter the number of compute nodes[4]: ", "4")
    buffer = "num_computes: " + compute_no + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    socket_no = is_num("Please enter the number of sockets[2]: ", "2")
    buffer = "num_sockets: " + socket_no + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    core_no = is_num("Please enter the number of cores per socket[8]: ", "8")
    buffer = "num_cores: " + core_no + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    threads_no = is_num("Please enter the number of threads per core[2]: ", "2")
    buffer = "num_threads: " + threads_no + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - resource_management\n")
    # Infiniband support
    infiniband_support = yes_no("Add Infiniband Support? ")
    if infiniband_support == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - infiniband_support\n")
        ib_network = ip_network("Please enter the IB network for the headnode[192.168.5.]: ", "192.168.5.")
        ib_client = ip_client("Please enter the IB client address for the headnode[1]: ", "1")
        buffer = "master_ipoib: " + ib_network + ib_client + "\n"
        with open('./group_vars/all', 'w') as the_file:
            the_file.write(buffer)
        ib_netmask = ip_netmask("Please enter the IB netmask[255.255.255.0]: ", "255.255.255.0")
        buffer = "ipoib_netmask: " + ib_netmask + "\n"
        with open('./group_vars/all', 'w') as the_file:
            the_file.write(buffer)
    # Omnipath base
    omnipath_base = yes_no("Add omnipath base? ")
    if omnipath_base == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - opa_support_base\n")
    # Basic warewulf
    interal_interface = required("Please enter the provisioning interface for the headnode: ")
    buffer = "sms_eth_internal: " + interal_interface + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    ip_netmask = netmask("Please enter the netmask for the headnode[255.255.255.0]: ", "255.255.255.0")
    buffer = "sms_netmask: " + ip_netmask + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - basic_warewulf\n")
    # Install BOS
    chroot = generic("Please enter the chroot location[/opt/ohpc/admin/images/centos7.4]: ", "/opt/ohpc/admin/images/centos7.4")
    buffer = "chroot: " + chroot + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a')as the_file:
        the_file.write("     - initial_bos_image\n")
    # OHPC components
    with open('site.yml', 'a')as the_file:
        the_file.write("     - ohpc_components\n")
    # Customise sys config
    home_mount = generic("Please enter the home mount point[/home]: ", "/home")
    buffer = "home_mount: " + home_mount + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    opt_mount = generic("Please enter the opt mount point[/opt/ohpc/pub]: ", "/opt/ohpc/pub")
    buffer = "opt_mount: " + opt_mount + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - customise_sys_config\n")
    # Infiniband drivers compute
    c_infiniband_support = yes_no("Add Infiniband Support to compute nodes? ")
    if c_infiniband_support == True:
    with open('site.yml', 'a') as the_file:
        the_file.write("     - infiniband_drivers_comp\n")
    # mem limit
    mem_limit = yes_no("Increase locked memory limit? ")
    if mem_limit == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - mem_limit\n")
    # SSH control
    ssh = yes_no("Enable SSH control via resource manager?" )
    if ssh == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - ssh_control\n")
    # Beegfs
    beegfs = yes_no("Add Beegfs to cluster? ")
    if beegfs == True:
        beegfs_repo = generic("Please enter Beegfs repo[https://www.beegfs.io/release/latest-stable/dists/beegfs-rhel7.repo]: ", "https://www.beegfs.io/release/latest-stable/dists/beegfs-rhel7.repo")
        buffer = "beegfs_repo: " + beegfs_repo + "\n"
        with open('group_vars/all', 'a') as the_file:
            the_file.write(buffer)
        beegfs_ip = ip_full("Please enter the Beegfs IP address[192.168.0.254]: ", "192.168.0.1")
        buffer = "systemtd_host: " + sysmgmtd_host + "\n"
        with open('group_vars/all', 'a') as the_file:
            the_file.write(buffer)
        with open('site.yml', 'a') as the_file:
            the_file.write("     - beegfs\n")
    # Lustre
    lustre = yes_no("Add Lustre to cluster? ")
    if lustre == True:
        lustre_mount = generic("Please enter the Lustre mount point[/mnt/lustre]: ", "/mnt/lustre")
        lustre_ip = ip_full("Please enter the Lustre IP[192.168.0.254]: ", "192.168.0.254")
        buffer = "mgs_fs_name: " + lustre_ip + lustre_mnt + "\n"
        with open('group_vars/all', 'a') as the_file:
            the_file.write(buffer)
        with open('site.yml', 'a') as the_file:
            the_file.write("     - lustre\n")
    # Forward logs
    logs = yes_no("Forward logs from compute nodes to headnode? ")
    with open('site.yml', 'a') as the_file:
        the_file.write("     - forward_logs\n")
    # Nagios
    nagios = yes_no("Add Nagios Monitoring to cluster? ")
    if nagios == True:
        nagios_user = is_alphanumeric("Please enter the Nagios Admin username[admin]: ", "admin")
        buffer = "nagios_web_user: " + nagios_user + "\n"
        with open('group_vars/all', 'a') as the_file:
            the_file.write(buffer)
        nagios_pass = is_alphanumeric("Please enter the Nagios Admin password[password]: ", "password")
        buffer = "nagios_web_password: " + nagios_pass + "\n"
        with open('group_vars/all', 'a') as the_file:
            the_file.write(buffer)
        with open('site.yml', 'a') as the_file:
            the_file.write("     - nagios\n")
    # Ganglia
    ganglia = yes_no("Add Ganglia to cluster? ")
    if ganglia == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - ganglia\n")
    # Clustershell
    clustershell = yes_no("Add Clustershell to cluster? ")
    if clustershell == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - clustershell\n")
    # Mrsh
    mrsh = yes_no("Add Mrsh to cluster? ")
    if mrsh == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - mrsh\n")
    # Genders
    genders = yes_no("Add genders to cluster? ")
    if genders == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - genders\n")
    # Conman
    conman = yes_no("Add Conman to cluster? ")
    if conman == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - conman\n")
    # Import files core
    with open('site.yml', 'a')as the_file:
        the_file.write("     - import_files_core\n")
    # Import files ib
    if infiniband_support == True:
        with open('site.yml', 'a')as the_file:
            the_file.write("     - import_files_ib\n")
    # Bootstrap kernel
    bootstrap_kernel = yes_no("Add additional kernel arguments to bootstrap? ")
    if bootstrap_kernel == True:
        with open('site.yml', 'a')as the_file:
            the_file.write("     - bootstrap_updates\n")
    # Bootstrap Singularity
    bootstrap_singularity = yes_no("Add Singularity arguments to kernel? ")
    if bootstrap_singularity == True:
        with open('site.yml', 'a')as the_file:
            the_file.write("     - bootstrap_singularity\n")
    # Bootstrap
    with open('site.yml', 'a')as the_file:
        the_file.write("     - bootstrap_core\n")
    # VNFS
    with open('site.yml', 'a')as the_file:
        the_file.write("     - vnfs\n")
    # Register nodes core
    c_provision = required("Please enter the compute node provisioning interface: ")
    buffer = "eth_provision: " + c_provision + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    c_ipaddr_network = ip_network("Please enter the compute IP network[192.168.0.]: ", "192.168.0.")
    buffer = "c_ip: " + c_ipaddr_network + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    c_ipaddr_client = ip_client("Please enter the compute IP client start address[2]: ", "2")
    buffer = "c_ip_last: " + c_ipaddr_client + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    c_mac = []
    for x in range(0, int(compute_no)):
        c_mac.append(required("Please enter MAC: "))
    with open('./group_vars/all', 'a') as the_file:
        the_file.write("c_mac: \n")
    for i in range(len(c_mac)):
        buffer = "  - " + c_mac[i] + "\n"
        with open('./group_vars/all', 'a') as the_file:
            the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - register_nodes_core\n")
    # Register nodes IB
    if infiniband_support == True:
        c_ipoib_network = ip_network("Please enter the compute IPoIB network[192.168.5.]: ", "192.168.5.")
        buffer = "c_ipoib: " + c_ipoib_network + "\n"
        with open('group_vars/all', 'a') as the_file:
            the_file.write(buffer)
        c_ipoib_client = ip_client("Please enter the compute IPoIB client start address[2]: ", "2")
        buffer = "c_ipoib_last: " + c_ipoib_client + "\n"
        with open('group_vars/all', 'a') as the_file:
            the_file.write(buffer)
    # Register nodes predictable
    register_predictable = yes_no("Set compute interface names? ")
    if register_predictable == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - register_nodes_predictable\n")
    # Stateful
    stateful = yes_no("Deploy nodes in stateful configuration? ")
    if stateful == True:
        stateful_mode = efi_legacy("Deploy nodes as efi or legacy?")
        if stateful_mode == "efi":
            with open('site.yml', 'a')as the_file:
                the_file.write("     - stateful_efi\n")
        elif stateful_mode == "legacy":
            with open('site.yml', 'a')as the_file:
                the_file.write("     - stateful_legacy\n")
        else:
            print("error reading stateful_mode")
    # Boot nodes
    bmc_network = ip_network("Please enter the BMC network address[192.168.1.]: ", "192.168.0.")
    buffer = "bmc_host: " + bmc_network + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    bmc_client = ip_client("Please enter the BMC client start address[2]: ", "2")
    buffer = "bmc_ip: " + bmc_client + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    bmc_user = required("Please enter the BMC username: ")
    buffer = "bmc_username: " + bmc_user + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    bmc_password = required("Please enter the BMC password: ")
    buffer = "bmc_password: " + bmc_password + "\n"
    with open('./group_vars/all', 'a') as the_file:
        the_file.write(buffer)
    with open('site.yml', 'a') as the_file:
        the_file.write("     - boot_nodes\n")
    # Development
    dev = yes_no("Install Development Tools? ")
    if dev == True:
        with open('site.yml', 'a') as the_file:
            the_file.write("     - development_tools\n")
        compiler = compiler("Which compiler should be installed: gnu or llvm? ")
        if compiler == "gnu":
            with open('group_vars/all', 'a') as the_file:
                the_file.write("gnu_compiler: true\n")
        elif compiler == "llvm":
            with open('group_vars/all', 'a') as the_file:
                the_file.write("llvm_compiler: true\n")
        else:
            print("error reading compiler")
        with open('site.yml', 'a') as the_file:
            the_file.write("     - compilers\n")
        mpi = mpi("Which MPI stack should be installed: ethernet, infiniband, opa, or pmix? ")
        if mpi == "ethernet":
            with open('group_vars/all', 'a') as the_file:
                the_file.write("ethernet_mpi: true\n")
        elif mpi == "infiniband":
            with open('group_vars/all', 'a') as the_file:
                the_file.write("infini_mpi: true\n")
        elif mpi == "opa":
            with open('group_vars/all', 'a') as the_file:
                the_file.write("psm2_mpi: true\n")
        elif mpi == "pmix":
            with open('group_vars/all', 'a') as the_file:
                the_file.write("pmix_mpi: true\n")
        with open('site.yml', 'a') as the_file:
            the_file.write("     - mpi\n")
        default_dev = default_dev("Which toolchain should be installed: openmpi, mpich, or mvapich?")
        if default_dev == "openmpi":
            with open('group_vars/all', 'a') as the_file:
                the_file.write("openmpi3_dev_env: true\n")
        elif default_dev == "mpich":
            with open('site.yml', 'a') as the_file:
                the_file.write("mpich_dev_env: true\n")
        elif default_dev == "mvapich":
            with open('site.yml', 'a') as the_file:
                the_file.write("mvapich_dev_env: true\n")
        else:
            print("error reading default_dev")
        with open('site.yml', 'a') as the_file:
            the_file.write("     - default_dev_env\n")
        performance_tools = yes_no("Install performance tools? ")
        if performance_tools == True:
            with open('site.yml', 'a') as the_file:
                the_file.write("     - performance_tools\n")
    # Resource startup
    with open('site.yml', 'a') as the_file:
        the_file.write("     - resource_startup\n")
