# Download Git
- [Download Git](https://git-scm.com/)

- *Click on the download link for windows button, if you're using anything else then go for it. The installer (`.exe` file) will begin downloading.*

- *Locate the downloaded `.exe` file and double-click it to run.*

- **Select destination location:** *Choose the installation folder or leave it as default.*

- **Select components:** *Keep the defaults checked, or select additional options (e.g., "Git Bash Here" for context menu integration).*

- **Recomende:** *"Git from the command line and also from 3rd-party software."*

- **Choose SSH Executable:** *Leave it as the default.*

- **Configure Line Ending Conversion:**
    - Recomended: "Checkout windows-style, commit unix-style line ending."

**Configure Extras:** *Keep the defaults unless you need specific customizations.*

*Click `Install` and `Finish` when done.*

### Verify Git installation
```bash
git --version
```

## How to work with Git in Visual Studio Code

- *Open VS code and and then open terminal*
`ctrl + backtick` 

- *Clone repo*
```bash
git clone https://github.com/sumit-dev-01/python_study_meterials.git
```

- *Navigate to the repo and go to working directory*
```bash
cd python_study_meterials/python
```

- *Check files in folder*
`ls`

- *Check existing branches*
```bash
git branch -a
```

- *Create a local branch from remote branch*
```bash
git checkout -b introduction_brunch origin/introduction_brunch
```
*Make sure you work on your feature branch, don't work in main branch, after work is complete we'll push to feature branch then merge it to main branch.*

- *Now check where you're*
```bash
git branch -a
```
*`*` mark shows you where you're and color should be green.*
*After you confirm then proceed to `git add` and `git commit`*

- *When you edit existing file that show in `M` mode, means you're in Modifing*
```bash
git status
```
*looks like this in red color*
`modified:   github_work.md`

- *After made changes*
```bash
git add github_work.md
```
```bash
git commit -m "type your message (what you update. So that when you see next time...ooh..i update this, okay...)"
```

*Push to remote branch*
```bash
git push origin introduction_brunch
```

*You can fetch latest updated repo with this*
```bash
git pull origin introduction_brunch
```

### When you create a new branch on github's remote repository initially that don't appear on local system (VS Code)

*If you are run that command `git branch -a` and trying to show your position or available branches, still you don't show newly created branch  call `assignments` (my branch)*

**Run that**

```bash
git fetch --all
```
```bash
git branch -a
```
