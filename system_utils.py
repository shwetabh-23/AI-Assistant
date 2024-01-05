import sys
import os
import psutil
import subprocess

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def execute_terminal_command(command):

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def terminate_process_by_pid(pid_to_terminate):
    try:
        process = psutil.Process(pid_to_terminate)
        print(f"Process {pid_to_terminate} - {process.name()}")
    except psutil.NoSuchProcess:
        print(f"No such process with PID {pid_to_terminate}")
