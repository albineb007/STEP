"""
Script to generate a simple dependency/relationship diagram beyond the ER diagram using Graphviz.

Usage:
1. Install Graphviz system package and Python package if not already installed:
   - Download and install Graphviz from https://graphviz.org/download/
   - Install Python package: pip install graphviz

2. Run this script:
   python scripts/generate_db_dependency.py

This will generate a file 'db_dependency.png' in the project root.
"""

import os
from graphviz import Digraph

def generate_db_dependency():
    dot = Digraph(comment='Database Dependency Diagram')

    # Example dependency nodes (tables/modules)
    dot.node('User', 'User Table')
    dot.node('Order', 'Order Table')
    dot.node('Product', 'Product Table')
    dot.node('Payment', 'Payment Table')

    # Example dependencies (edges)
    dot.edge('Order', 'User', label='belongs to')
    dot.edge('Order', 'Product', label='contains')
    dot.edge('Payment', 'Order', label='pays for')

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db_dependency')
    dot.render(output_path, format='png', cleanup=True)
    print(f"Database dependency diagram generated successfully: {output_path}.png")

if __name__ == "__main__":
    generate_db_dependency()
