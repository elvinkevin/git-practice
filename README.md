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
##  Handling Merge Conflicts

Not all merges complete smoothly — conflicts are a normal part of development. This section covers practical recovery techniques when they occur.

---

##  Scenario 1: Merge Conflicts

Merge conflicts happen when two branches modify the same line in a file, and Git cannot determine which version to keep.

###  Step-by-Step Resolution Workflow

**1. Identify the conflict**

When running `git merge` or `git pull`, Git will stop and flag the conflicting files.

---

**2. Open the file**

Look for conflict markers inserted by Git:

```text
<<<<<<< HEAD
Your current local changes
=======
Incoming changes from another branch
>>>>>>> branch-name
```

---

**3. Clean up the code**

* Remove the markers: `<<<<<<<`, `=======`, `>>>>>>>`
* Manually edit and keep the correct code (or combine both changes)

---

**4. Finalize the merge**

```bash
# Stage the resolved file
git add <filename>

# Commit the resolution
git commit -m "fix: resolve merge conflict in automation script"

# Push the updated branch
git push origin <branch-name>
```

---

##  Scenario 2: Committing to the Wrong Branch

Imagine you have:

* `main` branch
* `feature/login-page` branch

You accidentally commit changes to `main` instead of your feature branch.

---

###  Recovery Steps (Before Push)

If you **haven’t pushed yet**, you can safely fix this:

```bash
# Reset main branch to match remote (discarding the accidental commit)
git reset --hard origin/main

# Switch to your feature branch
git switch feature/login-page
```

 Your commit will still be available in your Git history and can be recovered on the correct branch.

---

###  Important Notes

* `git reset --hard` will discard uncommitted changes — use with caution
* This workflow only works safely if changes have **not been pushed**
* If already pushed, recovery requires a different approach (e.g., revert or force push)

---
##  Scenario 3: Pushing to the Wrong Branch (Using `git cherry-pick`)

When working across multiple branches, it’s easy to accidentally commit and push code to the wrong branch. In such cases, `git cherry-pick` is a precise way to move commits where they actually belong.

---

###  Example Scenario

You have two branches:

* `feature/login-form`
* `hotfix/authentication`

You accidentally commit changes intended for `hotfix/authentication` onto `feature/login-form`.

---

###  Recovery Steps

**1. Identify the commit**

Run:

```bash
git log --oneline
```

* Copy the commit hash (usually a short 7-character string)

---

**2. Apply the commit to the correct branch**

```bash
# Switch to the correct branch
git checkout hotfix/authentication

# Apply the commit from the other branch
git cherry-pick <commit-hash>
```

👉 This **copies** the commit into the current branch (it does not move it).

---

**3. Push the corrected branch**

```bash
git push origin hotfix/authentication
```

---

**4. Clean up the wrong branch**

Go back to the branch that received the commit by mistake:

```bash
git checkout feature/login-form
```

If the commit has **not been pushed**, you can safely remove it:

```bash
git reset --hard HEAD~1
```

---

###  Important Corrections & Notes

* `git cherry-pick` **duplicates** a commit — it does not transfer it
* Your original commit will still exist on the wrong branch until you remove it
* `git reset --hard HEAD~1` removes the latest commit locally
* If the commit was already pushed:

  * Prefer using `git revert` instead of `reset`
  * Or use `git push --force` (only if you understand the risks)

---

##  Summary

* Conflicts are normal — resolve them manually and commit
* Always review conflict markers carefully
* Fix wrong-branch commits early (before pushing if possible)
* Use `git cherry-pick` to move commits across branches safely
* Keep branches clean and intentional

---

💡 *Pro tip: Small, frequent commits make mistakes easier to fix and reduce recovery complexity.*








##  Summary

This guide covers:

* Initial repository setup
* Branching strategies
* Feature development workflow
* Cleanup and maintenance practices

Use it as a quick reference to maintain clean, efficient, and scalable Git workflows.

---

 *Tip: Consistency in workflow matters more than complexity. Keep it simple and disciplined.*
