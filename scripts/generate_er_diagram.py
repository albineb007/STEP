"""
Script to generate ER diagram from Django models using django-extensions.

Usage:
1. Install dependencies if not already installed:
   pip install django-extensions
   # Also install graphviz system package:
   # On Windows, download and install from https://graphviz.org/download/
   # Make sure 'dot' executable is in your PATH.

2. Add 'django_extensions' to INSTALLED_APPS in your config/settings.py

3. Run this script:
   python scripts/generate_er_diagram.py [output_format]

   output_format (optional): The output image format (png, pdf, svg, etc.). Default is png.

This will generate a file 'er_diagram.<output_format>' in the project root.
"""

import os
import sys
import django
from django.core.management import call_command

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

def generate_er_diagram(output_format="png"):
    output_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        f"er_diagram.{output_format}"
    )
    try:
        call_command("graph_models", "-a", "-o", output_file)
        print(f"ER diagram generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating ER diagram: {e}")

if __name__ == "__main__":
    import sys
    fmt = sys.argv[1] if len(sys.argv) > 1 else "png"
    generate_er_diagram(fmt)
