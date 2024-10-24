#!/usr/bin/env python3
import subprocess

def list_monitors():
    result = subprocess.run(['xrandr', '--listmonitors'], capture_output=True, text=True)
    monitors = result.stdout.splitlines()[1:]

    monitor_list = []
    for monitor in monitors:
        details = monitor.split()
        monitor_id = details[1]
        monitor_name = details[3] if len(details) > 3 else details[2]
        is_primary = '*' in details[2]
        monitor_list.append((monitor_id, monitor_name, is_primary))

    return monitor_list

def display_monitors(monitors):
    print("\nAvailable Monitors:")
    for i, (_, monitor_name, is_primary) in enumerate(monitors):
        primary_indicator = " (Current Primary)" if is_primary else ""
        print(f"{i + 1}: {monitor_name}{primary_indicator}")
    print()

def set_main_monitor(monitor_name):
    subprocess.run(['xrandr', '--output', monitor_name, '--primary'])

def get_current_primary(monitors):
    for _, monitor_name, is_primary in monitors:
        if is_primary:
            return monitor_name
    return None

def main():
    while True:
        monitors = list_monitors()

        display_monitors(monitors)

        try:
            choice = int(input("Select the monitor number to set as primary (or 0 to exit): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == -1:
            print("Exiting...")
            break
        elif 0 <= choice < len(monitors):
            selected_monitor = monitors[choice][1]
            current_primary = get_current_primary(monitors)

            if selected_monitor == current_primary:
                print(f"'{selected_monitor}' is already the primary display.\n")
            else:
                set_main_monitor(selected_monitor)
                print(f"'{selected_monitor}' is now the primary display.\n")
        else:
            print("Invalid choice. Please select a valid monitor number.\n")

        another = input("Do you want to change the primary display again? (y/n): ").lower()
        if another != 'y':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
