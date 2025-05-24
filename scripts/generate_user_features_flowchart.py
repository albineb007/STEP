"""
Script to generate a flowchart image of Admin, Student, and Teacher features using Graphviz.

Usage:
1. Install Graphviz system package and Python package if not already installed:
   - Download and install Graphviz from https://graphviz.org/download/
   - Install Python package: pip install graphviz

2. Run this script:
   python scripts/generate_user_features_flowchart.py

This will generate a file 'user_features_flowchart.png' in the project root.
"""

import os
from graphviz import Digraph

def generate_user_features_flowchart():
    dot = Digraph(comment='User Features Flowchart')

    # Define roles
    dot.node('Admin', 'Admin')
    dot.node('Student', 'Student')
    dot.node('Teacher', 'Teacher')

    # Admin features
    dot.node('A1', 'Manage Users')
    dot.node('A2', 'Manage Courses')
    dot.node('A3', 'View Reports')

    # Student features
    dot.node('S1', 'Enroll in Courses')
    dot.node('S2', 'Take Quizzes')
    dot.node('S3', 'View Results')

    # Teacher features
    dot.node('T1', 'Create Courses')
    dot.node('T2', 'Create Quizzes')
    dot.node('T3', 'Grade Quizzes')

    # Connect Admin to features
    dot.edge('Admin', 'A1')
    dot.edge('Admin', 'A2')
    dot.edge('Admin', 'A3')

    # Connect Student to features
    dot.edge('Student', 'S1')
    dot.edge('Student', 'S2')
    dot.edge('Student', 'S3')

    # Connect Teacher to features
    dot.edge('Teacher', 'T1')
    dot.edge('Teacher', 'T2')
    dot.edge('Teacher', 'T3')

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'user_features_flowchart')
    dot.render(output_path, format='png', cleanup=True)
    print(f"User features flowchart generated successfully: {output_path}.png")

if __name__ == "__main__":
    generate_user_features_flowchart()
