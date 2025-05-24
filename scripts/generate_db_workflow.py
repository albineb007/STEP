"""
Script to generate a simple workflow/process diagram related to the database using Graphviz.

Usage:
1. Install Graphviz system package and Python package if not already installed:
   - Download and install Graphviz from https://graphviz.org/download/
   - Install Python package: pip install graphviz

2. Run this script:
   python scripts/generate_db_workflow.py

This will generate a file 'db_workflow.png' in the project root.
"""

import os
from graphviz import Digraph

def generate_db_workflow():
    dot = Digraph(comment='Database Workflow')

    # Example workflow nodes
    dot.node('A', 'User Request')
    dot.node('B', 'Application Logic')
    dot.node('C', 'Database Query')
    dot.node('D', 'Database')
    dot.node('E', 'Response to User')

    # Example workflow edges
    dot.edges(['AB', 'BC', 'CD', 'DE'])

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db_workflow')
    dot.render(output_path, format='png', cleanup=True)
    print(f"Database workflow diagram generated successfully: {output_path}.png")

if __name__ == "__main__":
    generate_db_workflow()
