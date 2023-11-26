import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Create a new directory
new_dir = os.path.join(current_dir, 'new_directory')
os.mkdir(new_dir)
print(f"Created new directory: {new_dir}")

# List files and directories in the current directory
contents = os.listdir(current_dir)
print(f"Contents of the directory: {contents}")

# Remove the new directory
os.rmdir(new_dir)
print(f"Removed new directory: {new_dir}")
