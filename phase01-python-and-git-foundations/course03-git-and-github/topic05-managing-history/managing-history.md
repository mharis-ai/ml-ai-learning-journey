# Managing History

This section explores essential commands for inspecting Git's internal object database — including commits, trees, and blobs — to understand how Git stores and links data.

## Git Commands and Their Purpose

```bash
# Rebase in git
Git rebase is a powerful Git feature used to change the base of a branch. It effectively allows you to move a branch to a new starting point, usually a different commit, by “replaying” the commits from the original base onto the new base. This can be useful for keeping a cleaner, linear project history.

git checkout feature-branch              # Switch to the branch named 'feature-branch'
git rebase main                          # Reapply commits from the current branch on top of the main branch
git add <resolved-files>                 # Stage resolved files after fixing merge conflicts during a rebase
git rebase --continue                    # Continue the rebase process after resolving conflicts

# Git reflog
Git reflog is a command that shows you the history of your commits. It allows you to see the changes that you have made to your repository over time. This can be useful for debugging and understanding the history of your project.

git reflog                               # Show history of branch movements
git reflog <commit-hash>                 # View reflog from a specific commit
git reset --hard <commit-hash>           # Reset branch to a specific commit (discard changes)
git reset --hard HEAD@{1}                # Reset branch to a previous state from reflog
```

## Conclusion
In this guide, we’ve covered important aspects of managing Git history through `rebase` and `reflog`. We’ve learned how rebase can help maintain a cleaner, more linear project history, and how reflog can help recover lost commits or changes.