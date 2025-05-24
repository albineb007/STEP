"""
Script to generate a workflow diagram image showing the working of the REST API using Graphviz.

Usage:
1. Install Graphviz system package and Python package if not already installed:
   - Download and install Graphviz from https://graphviz.org/download/
   - Install Python package: pip install graphviz

2. Run this script:
   python scripts/generate_restapi_working_image.py

This will generate a file 'restapi_working_image.png' in the project root.
"""

import os
from graphviz import Digraph

def generate_restapi_working_image():
    dot = Digraph(comment='REST API Working')

    # Define workflow nodes for REST API request flow
    dot.node('A', 'Client Request')
    dot.node('B', 'API Gateway')
    dot.node('C', 'Authentication & Authorization')
    dot.node('D', 'Business Logic / Controllers')
    dot.node('E', 'Database Access')
    dot.node('F', 'Response to Client')

    # Define edges to show flow
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'restapi_working_image')
    dot.render(output_path, format='png', cleanup=True)
    print(f"REST API working image generated successfully: {output_path}.png")

if __name__ == "__main__":
    generate_restapi_working_image()
