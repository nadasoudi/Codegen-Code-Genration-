python solution.py

"""

import json
import sys

def main():
    if len(sys.argv)!= 3:
        print("Usage: python solution.py <input.json> <output.json>")
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        data = json.load(f)
    
    with open(sys.argv[2], 'w') as f: