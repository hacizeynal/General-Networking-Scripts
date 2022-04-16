import re
import csv
import os

csv_path = "/Users/zhajili/Desktop/Python/General Networking Scripts/csv_outputs"  # path
regex_for_up_interfaces_vlan = r"(?P<interface>\S+) +(?P<description>\S+.\S+.\S+)(?P<status> connected) +(?P<vlan>\d+)"
regex_for_hostname = r'(?P<hostname>\S+)#'


def collect_only_up_interfaces(initial_config):
    with open(initial_config) as f:
        for line in f:
            hostname = re.match(regex_for_hostname, line)
            interface_vlan_status = re.search(regex_for_up_interfaces_vlan, line)
            if hostname:
                filename = os.path.join(csv_path, hostname.group(1) + "_int_status.csv")  # save filename to directory
            elif interface_vlan_status:
                print(interface_vlan_status.group(1),interface_vlan_status.group(2),interface_vlan_status.group(4))


if __name__ == "__main__":
    collect_only_up_interfaces("device_outputs/rn2bacsw036.txt")
