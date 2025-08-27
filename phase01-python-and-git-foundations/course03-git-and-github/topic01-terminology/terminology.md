# Terminology

This section covers fundamental Git commands and their purposes, providing a foundation for effective version control.

## Git Commands and Their Purpose

```bash
# Check your git version
git --version                                            # This command will display the version of git installed on your system

# Repository
git status                                               # Show the status of your working directory and staging area

# Your config settings
git config --global user.email "your-email@example.com"  # Set your global Git email
git config --global user.name "Your Name"                # Set your global Git username
git config --list                                        # List all Git configurations

# Creating a repository 
git status                                               # This command will show you the current state of your repository
git init                                                 # Initialize a new Git repository, creating a hidden .git folder for version control

# Stage
git add <file> <file2>                                   # Stage files to be committed
git status                                               # Check the status after adding files

# Commit
git commit -m "commit message"                           # Commit staged files with a message
git status                                               # Check the status after committing

# Logs
git log                                                  # This command will show you the commit history of your repository. 
git log --oneline                                        # This command will make the output more compact and easier to read.

# Change default code editor
git config --global core.editor "code --wait"            # Set VS Code as the default Git editor

# .gitignore
node_modules                                             # Folder containing project dependencies (usually large, not tracked)
.env                                                     # Environment variables file (sensitive data, not tracked)
.vscode                                                  # VS Code workspace settings folder (personal config, not tracked)
# When you run the git status command, it will not show the node_modules and .vscode folders as being tracked by git.
```

## Conclusion
In this section, we have learned about the basics of git and how to use it to track changes to your files and folders. We have also learned about the different commands that you can use to interact with your repository, such as `init`, `add`, `commit`, `log`, etc By the end of this section, you should have a good understanding of how to use git and how to use it effectively to manage your code.