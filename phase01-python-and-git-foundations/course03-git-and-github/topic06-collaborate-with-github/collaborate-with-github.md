# Collaborate with GitHub

Github is a web-based Git repository hosting service. It is a popular platform for developers to collaborate on projects and to share code. Github provides a user-friendly interface for managing and tracking changes to your code, as well as a platform for hosting and sharing your projects with others.

## Git Commands and Their Purpose

```bash
# Configuring Git
git config --global user.email "your-email@example.com"   # Set your global Git email
git config --global user.name "Your Name"                 # Set your global Git username
git config --list                                         # List all Git configurations

# Setup SSH Key
ssh-keygen -t ed25519 -C "your-email@chaicode.com"        # Generate a new SSH key with a comment (your email)

# Publish code to remote repository
git init                                                  # Initialize a new Git repository (creates .git folder)
git add <files>                                           # Stage files to be committed
git commit -m "commit message"                            # Commit staged files with a message

# Remote URL settings
git remote -v                                             # View all remote repositories linked to the project
git remote add origin <remote-url>                        # Add a remote repository named 'origin'
git remote add upstream <remote-url>                      # Add a remote repository named 'upstream'

# Pushing code
git push <remote-name> <branch-name>                      # Push a local branch to a remote repository
git push -u origin main                                   # Push local main branch and set upstream tracking

# Fetch code
git fetch <remote-name>                                   # Download objects and refs from a remote (no merge)

# Pull code
git pull origin main                                      # Fetch and merge changes from remote main branch
```

## Conclusion
In this section, we have learned about Github and how to use it. We have also learned about how to setup ssh key and add it to your github account. We have also learned about how to publish code to the remote repository.