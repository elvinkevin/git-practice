# 🛠️ My Git & GitHub Reference Guide

A personal hands-on reference manual for version control workflows, repository management, and collaboration strategies.

---

##  1. Repository Initialization & Setup

To start tracking a project locally and link it to a remote GitHub repository:

```bash
# Initialize a new local Git repository
git init

# Stage all project files for the first commit
git add .

# Commit the staged files with a descriptive message
git commit -m "initial: setup project structure"

# Rename the default branch to 'main' (industry standard)
git checkout -b main

# Link the local repository to a remote GitHub repository
git remote add origin <PASTE_YOUR_GITHUB_REPO_URL>

# Push the local main branch to GitHub and set it as default upstream
git push -u origin main
