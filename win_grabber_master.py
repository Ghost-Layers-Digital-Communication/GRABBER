import os
import paramiko

# ---------- CONFIG ----------
WIN_HOST = "xxxxxxxxxxxxxxxxx" # Windows laptop IP
WIN_USER = "xxxxxxx" # Windows username
WIN_PASS = "YourWindowsPassword" # Windows password
FILE_NAME = "test.py" # file to pull

# Paths
REMOTE_FILE = f"/C/Users/{WIN_USER}/Desktop/{FILE_NAME}" # Bitvise SFTP path
LOCAL_FILE = os.path.join(os.path.expanduser("~"), "Desktop", FILE_NAME)
# ------------------------------------

# Ensure Pi Desktop folder exists
os.makedirs(os.path.dirname(LOCAL_FILE), exist_ok=True)

# SSH and SFTP
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(WIN_HOST, username=WIN_USER, password=WIN_PASS, look_for_keys=False)

sftp = ssh.open_sftp()
sftp.get(REMOTE_FILE, LOCAL_FILE)
sftp.close()
ssh.close()