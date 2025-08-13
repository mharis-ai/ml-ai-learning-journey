# Branches in Git

This section covers a way to work on different versions of a project at the same time. They allow you to create a separate line of development that can be worked on independently of the main branch. This can be useful when you want to make changes to a project without affecting the main branch or when you want to work on a new feature or bug fix.

## Git Commands and Their Purpose

```bash
# Creating a new branch
git branch                  # This command lists all the branches in the current repository.
git branch bug-fix          # This command switches to the bug-fix branch.
git switch bug-fix          # This command switches to the bug-fix branch.
git log                     # This command shows the commit history for the current branch.
git switch main             # This command switches to the main branch.
git switch -c dark-mode     # This command creates a new branch called dark-mode. the -c flag is used to create a new branch.
git checkout orange-mode    # This command switches to the orange-mode branch.

# Merging branches
git checkout main           # This command switches to the main branch.
git merge bug-fix           # This command merges the bug-fix branch into the main branch.

# Rename a branch
git branch -m <old-branch-name> <new-branch-name>

# Delete a branch
git branch -d <branch-name>
```

## Conclusion
In this section, we have learned about the different types of merges and how to resolve conflicts. We have also learned about the importance of `branching` and `merging` in Git and Github.