import re
import csv

regex_for_up_interfaces = r"(?P<hostname>\S+)#show"  # regex to catch all up interfaces and hostname of device
regex_pattern = re.compile(regex_for_up_interfaces)


def collect_only_up_interfaces(initial_config):
    with open(initial_config) as f:
        match = regex_pattern.search(f.read())
        if match:
            with open(match.group(1)+"_int_status.csv","w") as k:
                return None


if __name__ == "__main__":
    collect_only_up_interfaces("device_outputs/rn2bacsw036.txt")
