🛠️ Git & GitHub
Reference Guide
A personal hands-on reference manual for version control workflows, repository management, and collaboration strategies.
1. Repository Initialization & Setup
To start tracking a project locally and link it to a remote GitHub repository, run the following commands in sequence:

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


2. Feature Branching Workflow
2.1 Branching Strategies
Choose a branching strategy that fits your team's size and release cadence:

Strategy	Best For	Key Characteristic
Git Flow	Complex products needing long-term support	Formal release branches with dedicated lifecycle
GitHub Flow	Fast-moving teams deploying one main version	Short-lived branches merged directly to main
Trunk-Based Development	Teams optimizing for CI/CD and developer velocity	All developers commit to a single shared trunk

2.2 Branch Management Best Practices
–Short-lived branches — merge frequently to avoid complex rebases
–Naming conventions — use consistent prefixes: feature/, bugfix/, release/, hotfix/
–Rebasing and syncing — regularly rebase or merge from your main branch to stay current
–Clean up stale branches — enable auto-delete after PR merge, or prune manually on a schedule

2.3 Step-by-Step Feature Branch Workflow

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

Opening a Pull Request
Once you have pushed your branch, navigate to your GitHub repository online and create a Pull Request (PR). Review the diff, add a description, then merge the branch into main. For solo projects or small teams this process can be lightweight.

2.4 Syncing and Cleaning Up After a Merge
After the PR is merged on GitHub, return to your terminal and update your local main branch:

# Pull the latest changes into your local main branch
git checkout main
git pull origin main
 
# Delete the feature branch locally
git branch -D feature/add-python-automation
 
# Delete the remote tracking reference
git push origin --delete feature/add-python-automation
 
# Prune stale remote-tracking references
git fetch --prune

What does git fetch --prune do?
This command downloads the latest changes from your remote repository while simultaneously removing local references to remote-tracking branches that have already been deleted from the server. Running it after cleanup keeps your local branch list accurate and uncluttered.
