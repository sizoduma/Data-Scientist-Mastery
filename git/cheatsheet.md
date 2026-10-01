# Git cheat sheet

## Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Basic workflow
```bash
git init
git clone <repo-url>
git status
git add .
git commit -m "Add notebook and preprocessing"
git push origin main
```

## Branching
```bash
git checkout -b feature/model-tuning
git checkout main
git branch
git branch -d feature/model-tuning
```

## Updating from main
```bash
git fetch origin
git merge origin/main
# or
# git rebase origin/main
```

## Undoing changes
```bash
git restore <file>
git reset --soft HEAD~1
git revert <commit-hash>
```

## Best practices
- Keep commits small and meaningful
- Use descriptive commit messages
- Avoid committing generated artifacts unless needed
- Use PRs for review and discussion
- Pull before starting work on shared branches
