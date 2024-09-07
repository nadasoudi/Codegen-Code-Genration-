def extract_ip_address(filename):
    with open(filename) as f:
        for line in f:
            if line.startswith('X-DNS:'):
                return line.split(':')[1].strip()

print(extract_ip_address('/etc/hosts'))

"""

# Solution:

def extract_ip_address(filename):
    with open(filename) as f:
        for line in f:
            if line.startswith('X-