import telnetlib
import time

# Define the Telnet host and login credentials
host = '192.168.0.3'  # IP address of the remote device
username = 'huawei'    # Username for authentication
password = 'admin 123'       # Password for authentication

# Establish a Telnet connection to the host
tn = telnetlib.Telnet(host)

# Read until the device prompts for a username
tn.read_until(b"Username:")
# Send the username to the device, encoded in ASCII
tn.write(username.encode('ascii') + b"\n")

# Read until the device prompts for a password
tn.read_until(b"Password:")
# Send the password to the device, encoded in ASCII
tn.write(password.encode('ascii') + b"\n")

time.sleep(1) # Introduce a short delay to allow login completion

# Enter system configuration mode
tn.write(b'system-view \n')
time.sleep(1) # Short delay for command execution

# Select interface GigabitEthernet 0/0/1
tn.write(b'int g0/0/1 \n')

# Assign IP address 10.0.0.1/24 to the selected interface
tn.write(b'ip add 10.0.0.1 24 \n')

# Display the IP interface brief to verify configuration
tn.write(b'dis ip int br \n')

# Create VLANs 10 to 20 in batch mode
tn.write(b'vlan batch 10 to 20 \n')

# Optional: Print the output to the console to see the results
print(tn.read_very_eager().decode('ascii'))

# Close the connection
tn.close()