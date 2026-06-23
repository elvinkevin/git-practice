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

##  Scenario 4: Pushing to the Wrong Branch (After Push)

Mistakes become more critical when you’ve already **pushed commits to the wrong branch**, especially if others may have pulled that code.

---

###  Example Scenario

You intended to push changes to:

* `feature/payment-integration`

But accidentally pushed to:

* `main` 

---

##  Recovery Strategies

###  Option 1: Safe Fix (Recommended for Shared Branches)

If the branch (e.g., `main`) is shared with others, **do not rewrite history**.

Instead, use `git revert` to undo the changes safely.

```bash
# Identify the commit hash
git log --oneline

# Revert the incorrect commit
git revert <commit-hash>

# Push the fix
git push origin main
```

👉 This creates a **new commit that undoes the changes**, preserving history and avoiding conflicts for teammates.

---

###  Option 2: Rewrite History (Use With Caution)

If you're working **solo** or absolutely sure no one else has pulled the changes:

```bash
# Reset branch to previous state
git reset --hard HEAD~1

# Force push to overwrite remote history
git push --force origin main
```

---

###  Critical Warnings

* `git push --force` **rewrites history** — dangerous in team environments
* Teammates may experience broken histories or conflicts
* Only use force push when:

  * You are working alone
  * Or your team explicitly agrees

---

##  Moving the Commit to the Correct Branch

After fixing the wrong branch, apply the commit where it belongs:

```bash
# Switch to correct branch
git checkout feature/payment-integration

# Bring back the commit
git cherry-pick <commit-hash>

# Push correctly
git push origin feature/payment-integration
```

---

##  Summary

* If already pushed → prefer `git revert` (safe)
* Avoid `git push --force` on shared branches
* Use `git cherry-pick` to apply commits to the correct branch
* Always double-check your branch before pushing 🚀

---

💡 *Pro tip: Use `git status` and `git branch` before every push—it saves you from this entire scenario.*


##  Summary

This guide covers:

* Initial repository setup
* Branching strategies
* Feature development workflow
* Cleanup and maintenance practices

Use it as a quick reference to maintain clean, efficient, and scalable Git workflows.

---

 *Tip: Consistency in workflow matters more than complexity. Keep it simple and disciplined.*
