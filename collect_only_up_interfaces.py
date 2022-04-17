import re
import csv
import os

csv_path = "/Users/zhajili/Desktop/Python/General Networking Scripts/csv_outputs"  # path
regex_for_up_interfaces_vlan = r"(?P<interface>\S+) +(?P<description>\S+.\S+.\S+)(?P<status> +connected) +(?P<vlan>\d+)"
regex_for_hostname = r'(?P<hostname>\S+)#'
resource_list = [ ]


def collect_only_up_interfaces(initial_config):
    with open(initial_config) as f:
        for line in f:
            hostname = re.match(regex_for_hostname, line)
            interface_vlan_description = re.finditer(regex_for_up_interfaces_vlan, line)
            if hostname:
                filename = os.path.join(csv_path, hostname.group(1) + "_int_status.csv")  # save filename to directory
            elif interface_vlan_description:
                for i in interface_vlan_description:
                    resource_list.append(i.groups())
        resource_list.insert(0,["Interface", "Description", "Status", "VLAN"])
        with open(filename, "w") as m:
            writer = csv.writer(m)
            for row in resource_list:
                writer.writerow(row)
        with open(filename,"r") as k:
            reader = csv.reader(k)
            for row in reader:
                print(row)


if __name__ == "__main__":
    collect_only_up_interfaces("device_outputs/rn2dmzsw459.txt")
