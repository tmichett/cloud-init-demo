import argparse
import xml.etree.ElementTree as ET

def modify_xml(xml_path, location, vm_name):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Define the new disk element
        disk_element = ET.Element("disk", type="file", device="cdrom")
        ET.SubElement(disk_element, "driver", name="qemu", type="raw")
        ET.SubElement(disk_element, "source", file=f"{location}/{vm_name}-cidata.iso")
        ET.SubElement(disk_element, "target", dev="sdb", bus="sata")
        ET.SubElement(disk_element, "readonly")
        ET.SubElement(disk_element, "address", type="drive", controller="0", bus="0", target="0", unit="1")
        
        # Find the devices section and insert the new disk element
        devices = root.find("devices")
        if devices is not None:
            devices.append(disk_element)
        else:
            print("No <devices> section found in XML.")
            return
        
        # Format and write back the modified XML
        ET.indent(tree, space="    ", level=0)  # Ensure proper formatting
        tree.write(xml_path, encoding="utf-8", xml_declaration=True)
        print(f"Updated XML file saved: {xml_path}")
    except Exception as e:
        print(f"Error modifying XML: {e}")

def main():
    parser = argparse.ArgumentParser(description="Modify a VM XML file to include a CD-ROM disk entry.")
    parser.add_argument("xml_file", help="Path to the XML file")
    parser.add_argument("location", help="Directory where the ISO file is located")
    parser.add_argument("vm_name", help="Name of the virtual machine")
    args = parser.parse_args()
    
    modify_xml(args.xml_file, args.location, args.vm_name)

if __name__ == "__main__":
    main()

