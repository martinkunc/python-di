# Readme

Visual Studio Python plugin currently doesn't support virtualenvs outside of project tree.
Before installing poetry packages, it needs to be configured from command line by:
```
poetry config virtualenvs.in-project true
```

Then packages can be installed
```
poetry env use
```
