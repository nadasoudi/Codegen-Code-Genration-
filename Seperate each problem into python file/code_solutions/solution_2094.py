python -m networkx.examples.pydot_agraph -G G -o G.gexf

"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Set the path to the directory where the source code is
source_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(source_dir)

from