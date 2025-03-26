import sys
import time

from licensifylib import verify_and_activate_license
from licensifylib import create_license_file 

print(f"PROGRAM STARTS")


# 1st parameter: "TEST_COMMON" or "TEST_PERSONAL" or "PRO"

# CREATE LICENSE:
create_license_file("TEST_COMMON", "Andy Munjaro", "YourApplication", "licensify_test_lic.bin", expiry_days=1)
time.sleep(5) 

# LICENSE CHECK:
if not verify_and_activate_license("YourApplication", "licensify_test_lic.bin"): sys.exit(0)


print(f"PROGRAM ENDS")
