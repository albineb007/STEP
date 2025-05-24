"""
Script to generate a features flowchart image for the REST API using Graphviz.

Usage:
1. Install Graphviz system package and Python package if not already installed:
   - Download and install Graphviz from https://graphviz.org/download/
   - Install Python package: pip install graphviz

2. Run this script:
   python scripts/generate_restapi_features_image.py

This will generate a file 'restapi_features_image.png' in the project root.
"""

import os
from graphviz import Digraph

def generate_restapi_features_image():
    dot = Digraph(comment='REST API Features')

    # Define REST API features
    dot.node('F1', 'CRUD Operations')
    dot.node('F2', 'Authentication & Authorization')
    dot.node('F3', 'Input Validation')
    dot.node('F4', 'Rate Limiting')
    dot.node('F5', 'Error Handling')
    dot.node('F6', 'Logging & Monitoring')
    dot.node('F7', 'API Versioning')
    dot.node('F8', 'Pagination & Filtering')

    # Connect features to a central REST API node
    dot.node('API', 'REST API')
    dot.edge('API', 'F1')
    dot.edge('API', 'F2')
    dot.edge('API', 'F3')
    dot.edge('API', 'F4')
    dot.edge('API', 'F5')
    dot.edge('API', 'F6')
    dot.edge('API', 'F7')
    dot.edge('API', 'F8')

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'restapi_features_image')
    dot.render(output_path, format='png', cleanup=True)
    print(f"REST API features image generated successfully: {output_path}.png")

if __name__ == "__main__":
    generate_restapi_features_image()
