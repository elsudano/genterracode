# GenTerraCode
This application aims to create Terraform code from a detailed description of the features needed using LLM of an AI.

## How to install

1. Install Python3 (in OS Fedora 25 use `sudo dnf install python3`)
2. Install Tkinter (in OS Fedora 25 use `sudo dnf install python3-tkinter`)
    1. or with pip3...
3. For better performance it is recommended to install `virtualenv` in the
repository, to do this, run`virtualenv venv` inside the directory of the
repository
4. Before starting to encode you have to run the following statement so that
Virtual Env is activated: `source venv / bin / activate`
5. Finally, you have to run `pip3 -r install requirements.txt` to
install the dependencies

## How to run

Linux:

    python3 main.py

Windows:

    python3 main.py