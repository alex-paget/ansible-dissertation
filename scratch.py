user_defined = ['ipaddr_network', 'ip_client', 'sms_name', 'repo', 'ntp', 'compute_name', 'compute_no', 'socket_no', 'core_no', 'threads_no', 'ib_network', 'ib_client', 'interal_interface', 'ip_netmask', 'chroot', 'home_mount', 'opt_mount', 'beegfs_repo', 'beegfs_ip', 'lustre_mount', 'lustre_ip', 'nagios_user', 'nagios_pass', 'bmc_network', 'c_bmc_client', 'c_bmc_user', 'c_bmc_password' 'c_provision', 'c_ipaddr_network', 'c_ipaddr_client', 'c_ipoib_network', 'c_ipoib_client']
for x in user_defined[:]:
    if user_defined[x] != "":
        print(user_defined[x])
for x in c_mac[:]:
    print(c_mac[x])
print(infiniband_support)
print(omnipath_base)
print(c_infiniband_support)
print(mem_limit)
print(ssh)
print(beegfs)
print(lustre)
print(logs)
print(nagios)
print(ganglia)
print(clustershell)
print(mrsh)
print(genders)
print(conman)
print(bootstrap_kernel)
print(bootstrap_singularity)
print(register_predictable)
if stateful_mode == "efi":
    print("efi")
elif stateful_mode == "legacy":
    print("legacy")
else:
    print("stateful empty")
print(dev)
user_dev = ['compiler', 'mpi', 'default_dev', 'performance_tools']
for x in user_dev[:]:
    if user_dev[x] != "":
        print(user_dev[x])
