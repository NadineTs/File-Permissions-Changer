# File-Permissions-Changer

The script sets the permissions of a given file to `rwxrwxr-x` (775), which allows the owner and group to read, write, and execute the file, while others can only read and execute it.

## Flowchart
![linux file permissions Flowchart](https://github.com/user-attachments/assets/9633178d-fd57-4731-b82c-94d023ad265a)
This flowchart illustrates the decision-making process for checking and applying file permissions based on the owner's and group's status.


## Code Explanation
os.chmod: This function is used to change the mode of the path to the specified mode (in this case, 0755).

Error Handling: The script includes basic error handling to manage cases where the specified file is not found or other exceptions occur.


## Usage
1. Clone this repository or download the script.
2. Open the script and specify the path to your file in the `file_path` variable.

   
