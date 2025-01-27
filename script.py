import os
import subprocess

def automate_git_operations(run_times):
    """
    Automate creating a file, performing git add/commit/push, deleting the file,
    and repeating the git commands for the specified number of run times.

    :param run_times: Number of times to repeat the process
    """
    for i in range(1, run_times + 1):
        filename = f"temp_file_{i}.txt"
        
        # Step 1: Create a blank text file
        with open(filename, "w") as file:
            pass

        # Step 2: Add, commit, and push the file to the repository
        try:
            subprocess.run(["git", "add", filename], check=True)
            subprocess.run(["git", "commit", "-m", f"Add {filename}"], check=True)
            subprocess.run(["git", "push"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during git operation: {e}")
            return

        # Step 3: Delete the file
        os.remove(filename)

        # Step 4: Run git add, commit, and push again
        try:
            subprocess.run(["git", "add", "-A"], check=True)
            subprocess.run(["git", "commit", "-m", f"Remove {filename}"], check=True)
            subprocess.run(["git", "push"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during git operation: {e}")
            return

# Example usage
automate_git_operations(5)
