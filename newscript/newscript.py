import os

def create_new_script():
    print("This script was made by Abigor111. The objective is to create a new folder that has the necessary files to create a new script for this project.")
    script_name = input("Please write the name of the new script: ")
    os.makedirs(script_name, exist_ok=True)
    answer = input("Do you want to generate the additional files, like the python file and md file? yes(y) no(n)")
    if (answer.lower() == 'y'):
        with open(f"{script_name}/{script_name}.py", "w") as python_file:
            python_file.write(f"# {script_name}\n")
            python_file.write("import os\n")
        with open(f"{script_name}/README.md", "w") as md_file:
            md_file.write(f"# {script_name}\n")
            md_file.write(f"Description of {script_name}")
    else:
        exit()
if __name__ == "__main__":
    create_new_script()
