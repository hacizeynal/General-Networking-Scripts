import re
from pathlib import Path

folder_for_device_outputs = Path("device_outputs")
file_to_open = folder_for_device_outputs / "rn2oumsw001_show_interface_status.txt"
regex_to_catch = ""


def collect_only_up_interfaces(device_input, result_output):
    with open(device_input) as f, open(result_output, "w") as k:
        return None


collect_only_up_interfaces(file_to_open, "final_output.csv")
