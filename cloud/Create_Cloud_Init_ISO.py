import argparse
import subprocess
import os

def create_iso(output_path, vm_name):
    iso_path = os.path.join(output_path, f"{vm_name}-cidata.iso")
    user_data = os.path.join(output_path, "user-data")
    meta_data = os.path.join(output_path, "meta-data")
    vendor_data = os.path.join(output_path, "vendor-data")
    
    cmd = [
        "genisoimage", "-output", iso_path, "-V", "cidata", "-r", "-J", 
        user_data, meta_data, vendor_data
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"ISO image created successfully: {iso_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating ISO: {e}")

def main():
    parser = argparse.ArgumentParser(description="Generate a cloud-init ISO image.")
    parser.add_argument("path", help="Path to the directory containing user-data, meta-data, and vendor-data")
    parser.add_argument("vm_name", help="Name of the virtual machine")
    args = parser.parse_args()
    
    create_iso(args.path, args.vm_name)

if __name__ == "__main__":
    main()

