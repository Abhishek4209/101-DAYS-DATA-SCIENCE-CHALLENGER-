import os

def create_notebook_folder():
    folder_name = "Notebooks"
    os.makedirs(folder_name, exist_ok=True)
    
    for day in range(1, 102):
        file_name = f"Day_{day}.ipynb"
        file_path = os.path.join(folder_name, file_name)
        
        # Create a new notebook file
        with open(file_path, "w") as file:
            file.write("# Day {} Notebook\n\n".format(day))
            file.write("## Introduction\n\n")
            file.write("This is the notebook for Day {}.\n\n".format(day))
            file.write("## Tasks\n\n")
            file.write("- Task 1\n")
            file.write("- Task 2\n")
            file.write("- Task 3\n")
            file.write("\n\n")
            file.write("## Conclusion\n\n")
            file.write("End of Day {} notebook.\n".format(day))
            
    print("Notebook folder created successfully!")

if __name__ == "__main__":
    create_notebook_folder()
