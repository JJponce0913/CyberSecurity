import subprocess

# Define the Netcat command
command = 'ncat chals.swampctf.com 60001'

# Execute the command using subprocess
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()

# Print the output and error if any
print("Output:", output.decode())
print("Error:", error.decode())
