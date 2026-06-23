# 🛠️ Git & GitHub Reference Guide

A personal hands-on reference manual for version control workflows, repository management, and collaboration strategies.

---

##  1. Repository Initialization & Setup

To start tracking a project locally and link it to a remote GitHub repository, run the following commands in sequence:

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
```

---

##  2. Feature Branching Workflow

###  2.1 Branching Strategies

Choose a branching strategy that fits your team's size and release cadence:

| Strategy                | Best For                                | Key Characteristic                                |
| ----------------------- | --------------------------------------- | ------------------------------------------------- |
| Git Flow                | Complex products with long-term support | Formal release branches with structured lifecycle |
| GitHub Flow             | Fast-moving teams                       | Short-lived branches merged directly to `main`    |
| Trunk-Based Development | CI/CD-focused teams                     | Developers commit to a shared trunk frequently    |

---

### 📏 2.2 Branch Management Best Practices

* Use **short-lived branches** — merge frequently to avoid complex rebases
* Follow **naming conventions** — `feature/`, `bugfix/`, `release/`, `hotfix/`
* Keep branches updated — regularly **rebase or merge from `main`**
* **Clean up stale branches** — enable auto-delete or prune manually

---

### ⚙️ 2.3 Step-by-Step Feature Branch Workflow

```bash
# 1. Ensure you are on main and have the latest updates
git checkout main
git pull origin main

# 2. Create and switch to a new feature branch
git checkout -b feature/add-python-automation

# 3. Work on your code, then stage and commit changes
git add .
git commit -m "feat: add initial python backup script"

# 4. Push the feature branch to GitHub
git push origin feature/add-python-automation
```

---

###  Opening a Pull Request

Once you have pushed your branch:

1. Go to your GitHub repository
2. Open a **Pull Request (PR)**
3. Review the changes (diff)
4. Add a clear description
5. Merge into `main`

> For solo projects or small teams, this process can remain lightweight.

---

###  2.4 Syncing and Cleaning Up After a Merge

```bash
# Pull the latest changes into your local main branch
git checkout main
git pull origin main

# Delete the feature branch locally
git branch -D feature/add-python-automation

# Delete the remote branch
git push origin --delete feature/add-python-automation

# Prune stale remote-tracking references
git fetch --prune
```

---

###  What does `git fetch --prune` do?

This command:

* Fetches the latest updates from the remote repository
* Removes local references to remote branches that no longer exist

👉 Keeps your local environment clean and up to date.

---
# Handling Merge Conflicts
not all merges will be completed with a green flag, some will raise errors which is to be expected as a developer.
in this section we will cover the recovery techniques when a conflict arises.
. scenario one
Merge conflicts happen when two branches change the same line of the same file, and Git doesn't know which version to keep.

Step-by-Step Resolution Workflow:
Identify the conflict: When you try to merge or pull, Git will stop and flag the conflicting files.

Open the file: Look for the conflict markers inserted by Git:

<<<<<<< HEAD: Your current local changes.

=======: The dividing line between changes.

>>>>>>> branch-name: The incoming changes from the other branch.

Clean up the code: Delete the markers (<<<<<<<, =======, >>>>>>>) and manually edit the code to keep what you actually need.

Finalize the merge:
# Stage the resolved file
git add <filename>

# Commit the resolution to complete the merge
git commit -m "fix: resolve merge conflict in automation script"

# Push the clean updates
git push origin <branch-name>

scenario 2
## commiting to a wrong branch
lets say you are working with two branches : your main brach and a feature/login-page branch
you accidentally *commit* code to your main branch instead of the your feature branch how do you recover:
step 1
if you have not yet pushed your changes and they are still in the commit stage, from your main  


##  Summary

This guide covers:

* Initial repository setup
* Branching strategies
* Feature development workflow
* Cleanup and maintenance practices

Use it as a quick reference to maintain clean, efficient, and scalable Git workflows.

---

 *Tip: Consistency in workflow matters more than complexity. Keep it simple and disciplined.*
