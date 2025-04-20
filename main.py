import subprocess
import re

def get_instagram_clones():
    """Retrieve all installed Instagram clones"""
    result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
    packages = [line.split(":")[-1] for line in result.stdout.split("\n") if "instagram" in line.lower()]
    return packages

def get_app_display_name(package):
    """Fetch the app label (display name) using adb cmd package query-activities"""
    result = subprocess.run(["adb", "shell", "cmd", "package", "query-activities", package], capture_output=True, text=True)
    match = re.search(r"nonLocalizedLabel=([\w\s\d]+)", result.stdout)
    return match.group(1) if match else "Unknown Name"

def extract_number(display_name):
    """Extract number from display name like 'Instagram 42 icon'"""
    match = re.search(r'Instagram\s+(\d+)', display_name)
    return int(match.group(1)) if match else float('inf')  # use 'inf' if no number found, to push to bottom

def main():
    """Fetch and display Instagram clone names sorted by display number"""
    instagram_packages = get_instagram_clones()
    if not instagram_packages:
        print("No Instagram clones found.")
        return

    clones = []
    for package in instagram_packages:
        display_name = get_app_display_name(package)
        clones.append((extract_number(display_name), display_name, package))

    clones.sort(key=lambda x: x[0])  # sort by extracted number

    print("Found Instagram clones with Display Names and Package Names:")
    for _, display_name, package in clones:
        print(f"{display_name} - {package}")  # Combine name and package

if __name__ == "__main__":
    main()

