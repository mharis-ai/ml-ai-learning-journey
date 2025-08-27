# Diff, Stash and Tags

This section covers useful Git commands for diff, tags, and stash—not mainstream, but valuable in specific situations.

## Git Commands and Their Purpose

```bash
# Git Diff
Diff is an informative command that shows the differences between two commits. It is used to compare the changes made in one commit with the changes made in another commit. Git consider the changed versions of same file as two different files. Then it gives names to these two files and shows the differences between them.

git diff                                         # This command shows the changes between commits, branches, or the working directory and staging area
git diff --staged                                # This command shows the changes between your last commit and the staging area
git diff <branch-name-one> <branch-name-two>     # This command compares the difference between two branches
git diff branch-name-one..branch-name-two        # Another way to compare the difference between two branches
git diff <commit-hash-one> <commit-hash-two>     # This command compares the difference between two commits

# Git Stash
Stash is a way to save your changes in a temporary location. It’s useful when switching branches without losing work. You can then come back to the file later and apply the changes.

git stash                                        # Saves changes temporarily in a stack for later use
git stash save "work in progress on X feature"   # Name a stash with this command
git stash list                                   # View the list of stashes with this command
git stash apply                                  # Apply latest stash (keeps it in stash list)
git stash apply stash@{0}                        # Apply specific stash by index
git stash pop                                    # Apply latest stash and remove it from stash list
git stash drop stash@{0}                         # Delete specific stash
git stash apply stash@{0} <branch-name>          # Apply specific stash to a branch
git stash clear                                  # Delete all stashes

# Git Tags
Tags are a way to mark a specific point in your repository. They are useful when you want to remember a specific version of your code or when you want to refer to a specific commit. Tags are like sticky notes that you can attach to your commits.

git tag <tag-name>                               # Create a lightweight tag
git tag -a <tag-name> -m "Release 1.0"           # Create an annotated tag with a message
git tag                                          # List all tags
git tag <tag-name> <commit-hash>                 # Tag a specific commit
git push origin <tag-name>                       # Push a specific tag to remote
git tag -d <tag-name>                            # Delete a local tag
git push origin :<tag-name>                      # Delete a remote tag
```

## Conclusion
In this section, we explored how to use Git’s `diff`, `stash`, and `tags` commands. Though not used as frequently as add, commit, or push, they are incredibly helpful in debugging, context switching, and release management.