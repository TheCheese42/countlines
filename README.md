# Countlines

Quick CLI utility to count the lines of a project.

## Install

Using [pipx](https://pipx.pypa.io/):

```
pipx install git+https://github.com/TheCheese42/countlines
```

## Usage

`Usage: countlines <path> [--detailed] [--exts:.py,] [--excludes:.venv,venv, (supports regex)]`

### Path

Any directory path containing the files to analyze.

### --detailed

Give a more detailed output, i.e. show the lines count per file

### --exts

Specify a list of file extensions to analyze. Separate using commas ",".

Example: `--exts:.py,.js,.c`

### --excludes

Specify a list of files and folders (without leading or trailing slashs, no absolute paths) to ignore.

Example: `--excludes:.venv,venv,.*_ui.py,tests`

Regexps are also supported.

## Example Outputs

### Without --detailed

```text
Files: 6
Lines: 2964
Lines per file: 494.0
```

### With --detailed

```text
Files: 6
Lines: 2964
Lines per file: 494.0
/home/User/code/projects/Buttonbox/client/buttonbox_client/__init__.py: 0
/home/User/code/projects/Buttonbox/client/buttonbox_client/gui.py: 1606
/home/User/code/projects/Buttonbox/client/buttonbox_client/version.py: 2
/home/User/code/projects/Buttonbox/client/buttonbox_client/model.py: 861
/home/User/code/projects/Buttonbox/client/buttonbox_client/config.py: 184
/home/User/code/projects/Buttonbox/client/buttonbox_client/__main__.py: 311
```
