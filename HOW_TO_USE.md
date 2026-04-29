Step 1 — Run cookiecutter once to generate the project:

cookiecutter https://github.com/TezRomacH/python-package-template 
# answer the questions: project name, your name, etc.

Step 2 — This creates a fresh local folder. Go into it:
cd my_project

Step 3 — Initialise it as your own Git repository:
git init
git add .
git commit -m "initial project structure from cookiecutter"

Step 4 — Create an empty repo on GitHub, then connect and push:
git remote add origin git@github.com:john/my_project.git
git push -u origin main

Step 5 — From this point forward, if you move to a new machine or share it with a colleague, that's when git clone comes in:
git clone git@github.com:john/my_project.git