#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    print("Starting Webinar Registration Dashboard")
    
    # Check if input data exists
    input_file = "/data/in/tables/webinar_registration.csv"
    if not os.path.exists(input_file):
        print(f"Warning: Input file {input_file} not found. App will use sample data if available.")
    else:
        print(f"Found input data at {input_file}")
    
    # Run the Streamlit app
    try:
        print("Starting Streamlit server...")
        # For Keboola, we need to specify host=0.0.0.0 to allow external access
        subprocess.run([
            "streamlit", "run", "app.py", 
            "--server.port=8501", 
            "--server.address=0.0.0.0",
            "--server.enableCORS=false",
            "--server.enableXsrfProtection=false"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()