"""
Script to generate an ER diagram image for the REST API database using django-extensions.

Usage:
1. Install dependencies if not already installed:
   pip install django-extensions
   # Also install graphviz system package:
   # On Windows, download and install from https://graphviz.org/download/
   # Make sure 'dot' executable is in your PATH.

2. Add 'django_extensions' to INSTALLED_APPS in your config/settings.py if not already added.

3. Run this script:
   python scripts/generate_restapi_db_image.py [output_format]

   output_format (optional): The output image format (png, pdf, svg, etc.). Default is png.

This will generate a file 'restapi_db_image.<output_format>' in the project root.
"""

import os
import sys
import django
from django.core.management import call_command

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

def generate_restapi_db_image(output_format="png"):
    output_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        f"restapi_db_image.{output_format}"
    )
    try:
        # Generate ER diagram for all apps (including REST API models)
        call_command("graph_models", "-a", "-o", output_file)
        print(f"REST API database image generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating REST API database image: {e}")

if __name__ == "__main__":
    import sys
    fmt = sys.argv[1] if len(sys.argv) > 1 else "png"
    generate_restapi_db_image(fmt)
