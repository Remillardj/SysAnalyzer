#!/usr/bin/env python3

import psutil
import logging
import os
import json
import time
import subprocess
import re

# format constant
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.WARNING)
logger = logging.getLogger(__name__)

def sysinfo():
	# get RAM memory
	ram = psutil.virtual_memory()

	# get disk partitions
	disks = psutil.disk_partitions()

	# get CPU information
	cpu_times = psutil.cpu_times()
	cpu_stats = psutil.cpu_stats()
	cpu_num = psutil.cpu_count()

	# get network information
	net_io_counters = psutil.net_io_counters(pernic=True)
	net_if_addrs = psutil.net_if_addrs()
	net_if_stats = psutil.net_if_stats()

	# get users
	users = psutil.users()

	# get boot time
	boot_time = psutil.boot_time()

	# get processes
	pids = psutil.pids()

	# get os & version
	uname = os.uname()

	sysinfo = {
		'ram' : ram,
		'disks' : disks,
		'cpu_times' : cpu_times,
		'cpu_stats' : cpu_stats,
		'cpu_num' : cpu_num,
		'net_io_counters' : net_io_counters,
		'net_if_addrs' : net_if_addrs,
		'net_if_stats' : net_if_stats,
		'users' : users,
		'boot_time' : boot_time,
		'pids' : pids,
		'uname' : uname,
	}

	return sysinfo

def get_cpu_temp(disks):
	sensors = subprocess.check_output("sensors")
	tempeartures = {match[0]: float(match[1]) for match in re.findall("^(.*?)\:\s+\+?(.*?)°C", sensors, re.MULTILINE)}
	for disk in disks:
		output = subprocess.check_output(["smartctl", "-A", disk])
		temperatures[disk] = int(re.search("Temperature.*\s(\d+)\s*(?:\([\d\s]*\)|)$", output, re.MULTILINE).group(1))
	return temperatures

while True:
	print (json.dumps(get_cpu_temp(("/dev/sda", "/dev/sdc"))))
	time.sleep(20)






