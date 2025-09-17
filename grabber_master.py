#!/usr/bin/env python3
import os
import paramiko

# ---------- CONFIG ----------
PI_HOST = "xxx.xxx.xxx.xxx" # pi ip
PI_USER = "xxxxxxxx" # pi user name
PI_PASS = "xxxxxxxxx" # hardcoded password
PORT = 5150
REMOTE_FILE = "/home/xxxxx/Desktop/secret.txt" # replace xxx with user name
LOCAL_DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
LOCAL_FILE = os.path.join(LOCAL_DESKTOP, "secret.txt")
# ----------------------------

os.makedirs(LOCAL_DESKTOP, exist_ok=True)

# Connect via SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(PI_HOST, username=PI_USER, password=PI_PASS)

# Pull the file
sftp = ssh.open_sftp()
sftp.get(REMOTE_FILE, LOCAL_FILE)
sftp.close()
ssh.close()

print(f"Done — {REMOTE_FILE} has been saved to {LOCAL_FILE}")