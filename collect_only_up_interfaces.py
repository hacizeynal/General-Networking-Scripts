import re
from pathlib import Path

folder_for_device_outputs = Path("device_outputs")
file_to_open = folder_for_device_outputs / "rn2oumsw001_show_interface_status.txt"
with file_to_open.open() as f:
    print(f.read())

