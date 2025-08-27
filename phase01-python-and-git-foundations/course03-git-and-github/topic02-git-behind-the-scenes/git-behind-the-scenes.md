# Git Behind the Scenes

This section explores essential commands for inspecting Git's internal object database — including commits, trees, and blobs — to understand how Git stores and links data.

## Git Commands and Their Purpose

```bash
git show -s --pretty=raw <commit-hash>  # Show raw commit details (author, committer, message, and references)
git ls-tree <tree-id>                   # List the contents of a tree object (files and directories) in a specific commit/tree
git show <blob-id>                      # Display the contents of a blob object (file contents) by its ID
git cat-file -p <commit-id>             # Pretty-print the contents of any Git object (commit, tree, blob, or tag)
```

## Conclusion
These commands let you peek inside Git’s internal object database. By exploring commits (git show -s --pretty=raw), trees (git ls-tree), and blobs (git show), you can trace exactly how Git stores history. git cat-file -p is the universal viewer for any object type, making it the ultimate tool for understanding Git behind the scenes.