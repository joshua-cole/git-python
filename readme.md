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

