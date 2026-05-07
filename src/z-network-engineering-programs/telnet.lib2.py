import paramiko
import time

# Connection Details
hostname = "192.168.10.2"
username = "admin"
password = "admin123"

# Create SSH client
client = paramiko.SSHClient()
# Automatically add the device to known_hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Connecting to {hostname}...")
    client.connect(
        hostname=hostname,
        username=username,
        password=password,
        port=22,
        timeout=10,
        allow_agent=False,
        look_for_keys=False,
        disabled_algorithms=dict(pubkeys=["rsa-sha2-256", "rsa-sha2-512"])
    )

    print("Connected successfully!")

    # Open interactive shell (better for Huawei/CLI devices)
    shell = client.invoke_shell()
    time.sleep(1) # Give the shell a second to initialize

    # Send command
    print("Sending command: display version")
    shell.send("display version\n")

    # Wait for output - Huawei 'display' commands can be long
    time.sleep(2)

    # Receive and decode output
    output = shell.recv(65535).decode('ascii')
    print("-" * 20)
    print("OUTPUT:\n", output)
    print("-" * 20)

except Exception as e:
    print("Error:", e)

finally:
    # Ensure the connection is closed
    client.close()
    print("Connection closed.")