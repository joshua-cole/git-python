# Git with Python

All of the following commands are executed from the root of your project directory.

To initialize git tracking on a project:

```
git init
```

To stage all of the changes for the project:

```
git add .
```

To commit all of your changes:

```
git commit -m "[message]"
```

To work on a feature without affecting your main branch, create a new branch as follows:

```
git checkout -b [branch]
```

To view all branches for your project:

```
git branch -a
```

To merge your feature changes into main:

```
git checkout main
git merge [branch]
```

To delete a branch:

```
git branch -d [branch]
```

To link your reposository with GitHub, create a repository through the GitHub UI.

Copy the GIT URL from the generated repository page:

![image](https://github.com/joshua-cole/git-python/assets/157483185/66556738-e096-47b1-bf11-288e19548055)

Setup the remote origin:

```
git remote add origin [url]
```

The first time you push to a branch that does not exist on the remote repo, you must specify the upstream branch:

```
git push -u origin main
```

After that, you can simply push with:

```
git push
```

To pull changes from the GitHub repository:

```
git pull origin [branch]
```