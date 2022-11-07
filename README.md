
# welcome to the python starter template

This is a template that we have created to give everyone a much needed foundation to start their journey in python development. Please not this is a windows specific project and will not work with linux or other operating systems.

Built and maintained by [@connorwilloughby](https://github.com/connorwilloughby). Please let me know if you have any questions and we can get you set up. 

# contents

 1. [New users](#new-users)
    1. [Collaboration software](#collaboration-software)
    2. [Handy extensions](#handy-extensions)
 2. [Documentation](#documentation)
    1. [Packages](#packages)
    2. [Critical Files](#critical-files)
        1. [req.txt](#reqtxt)
        2. [.vscode/launch.json](#vscodelaunchjson)
        1. [.vscode/extensions.json](#vscodeextensionsjson)
        1. [main.py](#mainpy)
 3. [Support](#support)
    1. [Admins](#admins)

# new users

Welcome! 👋👋

To get access to this repo, if you're looking to add a new user you will need the following:

 - [Python](https://www.python.org/downloads/release/python-3107/)
   - version may change dependant on the code base you're looking to work in
 - [VS Code](https://code.visualstudio.com/download)
 - [Github account](https://github.com/signup?user_email=&source=form-home-signup)
 - access to [Savills-Insight-Data](https://github.com/Savills-Insight-Data)
   - new users please reach out to an [admin](##admins)

## collaboration software

 - [Github Desktop](https://desktop.github.com/)
   - recommended for beginners
   - alternative would be the source control extension in vscode which requires an understanding of git / source control

## handy extensions

So these aren't required however they will save you a huge amount of time / hassle and more importantly keep you sane when working on complex projects.

These are all installed by searching in the vscode extensions marketplace

If anyone knows how to link these please update the docs!

 - Python Extension
   - most important on the list as it will add intelligent typing and hints to your repo
 - Python Virtual Environment manager
 - Solar Lint
   - a powerful extension which will give basically perfect the code you write
 - [Github Autopilot](https://github.com/features/copilot)
   - a useful tool which will write much of your code for you

# documentation

So there are a few things that we've built here for you. These code blocks will explain each step.

## packages

> literally the most important part of repo management

So setting up packages is an important part of sharing code with others. To get set up in a repo the owner SHOULD have a script explaining their dependencies set up however this is not always present. 

We've put an example here of what needs to be added to your VS Code terminal in order to collect some example packages for this repo.

```console
# this line creates a virtual environment
py -m venv venv
# in windows this line will allow the rest of the script to go ahead
# if in powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# this line starts the environment
.\/venv/scripts/activate
# this line will update your pip (package installer) version 
py -m pip install --upgrade pip
# this line will install all dependencies
py -m pip install -r req.txt
```

## critical files

Firstly this repo currently very few critical files so please do take the time to look into each of these. 

### req.txt

This is a file which lists all packages required to run your script. 

If you need add a package you can do this with direct terminal addition. Once you have finished you can use the following terminal command `pip freeze > req.txt`. This will replace the file with version specific dependencies for your code. 

To run and collect dependencies its `py -m pip install -r req.txt`

### .vscode/launch.json

Another more simple file thats used by vscode for setting up debugging. This is a pretty advanced subject so id say fire and forget on this one and if there are any issues consult the section below

> [File Documentation](https://code.visualstudio.com/docs/python/debugging#_set-configuration-options)
> [General Documentation](https://code.visualstudio.com/docs/python/debugging).

### .vscode/extensions.json

This ones more experimental and im not entirely sure if it works. Its purpose is to tell people when they have missing extensions such as the ones listed [here](##packages)

> [File Documentation](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions).
> [General Documentation](https://code.visualstudio.com/docs/editor/extension-marketplace).

### .gitignore

This file is used to IGNORE parts of your repo in git. Decent naming right?! This is critical to save you from storing potentially massive packages in repos, we don't like this. 

The one were using is maintained by github themselves (more info in docs below) and simply removes common python projects which would otherwise clog up your repo. 

> [File Documentation](https://github.com/github/gitignore/blob/main/Python.gitignore).
> [File Documentation](https://git-scm.com/docs/gitignore).

### main.py

This is a really simple bit of code mostly for training. Its not very important.

# support 

So we have created a few channels for python support the current best place for support is the Python Pros team chat. If you don't have access you can ask anyone in the [admin](##admins) section.

You can alternatively reach us on teams directly!

## admins

| name | github account | 
|---|---|
| Connor Willoughby| [@connorwilloughby](https://github.com/connorwilloughby) |
| Mohammed Eldosoky| [@mo1878](https://github.com/mo1878) |

Thats it, well done if you read this far! 🎉
