#importing relevant packages
import subprocess as cmd

#running command line commands for staging and pushing commits
cp = cmd.run("git add .", check=True, shell=True)
cp = cmd.run(f"git commit -m \"update repo\"", check=True, shell=True)
cp = cmd.run("git push", check=True, shell=True)

#added pause for convenience
pawse = input("Done!")