#!/usr/bin/env python3
import subprocess

def list_monitors():
    result = subprocess.run(['xrandr', '--listmonitors'], capture_output=True, text=True)
    monitors = result.stdout.splitlines()
    
    print("Available Monitors:")
    monitor_list = []
    
    for monitor in monitors[1:]:
        details = monitor.split()
        monitor_id = details[1]
        monitor_name = details[3] if len(details) > 3 else details[2]
        monitor_list.append((monitor_id, monitor_name))
    
    return monitor_list

def set_main_monitor(monitor_name):
    subprocess.run(['xrandr', '--output', monitor_name, '--primary'])

def main():
    monitors = list_monitors()

    for i, (monitor_id, monitor_name) in enumerate(monitors):
        print(f"{i + 1}: {monitor_name}")
    
    choice = int(input("Select the monitor number to set as primary: ")) - 1

    if 0 <= choice < len(monitors):
        selected_monitor = monitors[choice][1]
        set_main_monitor(selected_monitor)
        print(f"Set {selected_monitor} as the primary display.")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
