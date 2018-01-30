# Python Setup

Python is a valuable scripting language for data analysis and... well, just about anything really. We won't be getting into the weeds with Python this week. However, we're going to try to get ahead of the fact that managing a Python project environment can be nuanced and tricky. This workshop will get you set up to manage Python projects; we'll be installing Python and the Hydrogen plug-in for Atom, which will allow you to execute scripts and display output from the comfort of the Atom text editor. It then introduces virtual environments using the `virtualenv` package for Python (which we'll install using the `pip` package manager); we'll be using these virtual environments to manage our projects this semester.

## Python Setup

### Checking for Installed Versions

First, check whether you have Python installed. Open the Terminal or Windows Command Prompt and type the following command:

```sh
python -V
```
You should see something like `Python 3.6.3`. If a Python 2.x.x version shows up, type `python3 -V`. If the console prints a Python `3.6.x` version, you're set. Otherwise, you'll need to install Python 3.

### Installing Python 3.6.x

Navigate to the [3.6.3 release page](https://www.python.org/downloads/release/python-363/) and select the appropriate installer for your operating system. Install Python using the default settings. Close any open Terminal or Command Prompt windows and reopen the application. Now type `python -V`. This may still cause a Python 2.x.x version to appear; if this is the case, type `python3 -V`. We now have Python 3 and can execute it from the command line!

**Note**: If you ran Python 3 using the `python3` command, you'll use this in every instance below where you're instructed to type `python`.

### A Note on Python Versions

You may (reasonably) ask: why would I ever want to maintain two versions of the same language on my operating system? Good question! Ordinarily, this would be only a source of confusion. But something strange happened between Python 2.7 and Python 3.x---the development team made unusually significant changes to the way the language thinks and operates. These were so significant, in fact, that Python 3 sacrificed **backwards-compatibility**. In other words, scripts written in Python 2.x will often not run correctly in Python 3.x.

So: imagine you've been coding in Python for years and you've built up a substantial collection of scripts you'd still like to be able to execute. You'll need to have Python 2.7.x on hand if you want to run older scripts! This also means that scripts you find on Github and elsewhere will often not be updated for Python 3 compatibility.

### Run a Script

In this week's repo folder, you should see a file called `first-script.py`. This is a Python script! `.py` is the standard file extension. Now that we've installed Python, we can run this script easily from the command line.

```sh
$ cd /path/to/repo/big-data-spring2018/week-01/
$ python first-script.py
Python is printing me!
```

Open the script - we'll get into Python next week, but this script is very simple and it shouldn't strain your brain too much to figure out what is happening. For now, let's move on.

## Install Hydrogen for Atom

As Elliot Alderson as it may make us feel to run all of our scripts from the command line, it will sometimes frankly be much easier to run chunks of our Python scripts rather than the scripts in their entirety. To do this, we will be using an Atom package called Hydrogen that will let us execute and display the output of our Python and JavaScript code from within Atom.

To install Hydrogen, open Atom, and open your preferences. Select 'Install' search for Hydrogen. Click the 'Install' button. After a brief interlude, Hydrogen should be installed! Check that 'Hydrogen' appears under the Packages drop-down menu.

Open the `first-script.py` script. Select the first line and type shift-enter. You'll see a checkmark appear next to the line and your cursor will have progressed to the next line. The checkmark tells you that the line executed successfully. In this case, that means a variable called `msg` is now stored in memory. Type shift-enter again.  You should see "Python is printing me!" appear next to the print function. This is how Hydrogen displays console output. Cool, eh? We can now run not only full scripts, but 'chunks' of code. This will allow us significantly more flexibility as we're developing our own scripts.

## Virtual Environments for Python

All right... one last task! We're going to install a Python library that will allow us to create virtual environments where we can manage our libraries for different projects.

### Why Use a Virtual Environment?

In brief: projects have what are called dependencies. These are packages that given scripts require to run successfully. By using a virtual environment, we can carefully tailor Python and package versions for each project without worrying about scuttling other projects' dependencies.

If you hang around with data types, you may have heard of Anaconda (and if they're obnoxious, they'll call it 'Conda); 'Conda is essentially a large virtual environment designed for data scientists that comes loaded with many, many common packages. While this environment is common and powerful, it's also very large and cumbersome. There's also a pedagogical value to managing your own virtual environment instead of falling back on a large deployment like 'Conda. In short: we'll be accomplishing what Conda offers to do for us in a much more agile, hands-on way.

### Installing `virtualenv` using `pip`

We're going to install the Virtual Environment library using `pip`. `pip` is a package management system that allows you to easily install and maintain python libraries using a simple command line interface. If you're on a Mac with a Python distribution, you'll probably be able to run `pip` or `pip3` from your command line with no problems. On Windows, it's a bit trickier (as usual).

### Installing `pip` on Windows

Go to [the pip webpage](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py) and download `get-pip.py`. Change your directory to the location to which you downloaded the `get-pip` script, and execute the following command:

```sh
python get-pip.py
```

This will install `pip` on your system. Close your command line windows and reopen them. You should then be able to execute pip; type `pip -V` to see which version you have installed. Much like with Python, if you have installations of both Python 2 and Python 3 on the same machine, you'll have to use the `pip3` command to install Python 3 packages.

### Installing `virtualenv`

Now we're going to install `virtualenv` using `pip`.

```sh
# if you have only Python 3.x installed
pip install virtualenv
# If you have both Python 2.x and Python 3.x installed
pip3 install virtualenv
```

Wow! That was easy. And that, my friends, is why we use package managers.

### Creating a New Virtual Environment

Once we've installed `virtualenv`, we can create a new virtual environment using only a few commands.

```sh
mkdir ~/.venvs
virtualenv --system-site-packages ~/.venvs/bdvs
. ~/.venvs/bdvs/bin/activate
```

First we create a new folder to hold our virtual environments. Next, we create a new virtual environment in the `bdvs` subfolder of our new `.venvs` subdirectory. We're also telling `virtualenv` that we want this environment to inherit its packages from the Python system installation (this is the role of the `--system-site packages` option). Finally, we activate the virtual environment using the `.` operator, which tells the shell to source from a provided path.

Cool! You're now running Python in a virtual environment!

## Additional Reading and Resources

### Conda Command Line Cheatsheet -
http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf

### Mac Command Line Cheatsheet –
https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)

### Python Documentation -
https://docs.python.org/3/library/index.html

<!--

### Install Anaconda (aka Conda)

The Anaconda homepage contains the materials that you need to install Anaconda on your machine. You will primarily be using Anaconda through the command line, so you will have to get comfortable working on the command line.

## 1. Check Anaconda Version and Install

The first step is to open Terminal and check to see if you have Anaconda installed. If not, we will install it. To check the version, follow the following commands.

#### i. Open Terminal
#### ii. Check Version

The syntax to access Anaconda on the command line is simply ‘conda’. To check the version you have installed, use the following:

```sh
	conda info
```

If you have it installed, you will see platform information, version details, and environment paths after you hit enter, if not, the terminal will not recognize the command.


#### iii. Install Anaconda

To install ‘Conda’, navigate to the Anaconda downloads page at:

[Anaconda Homepage and Downloads](https://www.continuum.io/downloads)

Here, pick your system (Mac/Windows) and the Python version. In our case, we are going to pick Mac and select **version 3.6**. Use the graphical installer, it will provide us a wizard that will step us through the installation process.  Download the installer, double click the package file and follow the instructions. Just a heads up, the installation process takes 5-10 minutes, its a big program, but is straight forward.

If you run into problems installing, or you get an error that states that Anaconda cannot be install in the default location, visit this page for short instructions on how to troubleshoot installation.

[Anaconda Installation Docs](http://docs.continuum.io/anaconda/install#anaconda-install)

Anaconda is contained in one directory, so if you ever need to uninstall Anaconda, use Terminal to remove the entire Anaconda directory using **rm -rf ~/anaconda**.

We used Python 3, not Python 2. The guidelines on the site describe that we should use whichever version we intend to use most often, but ultimately it will not matter that much. Anaconda supports both, and if you ever want to use Python 2, you can create an environment that uses Python 2 and activate it. The main reason you would want to use Python 2 is that Linux distributions and Macs, Python 2.7 is still the default, and because the Python ecosystem has amassed a significant amount of quality software over the years in which some of it does not yet work on 3. Python 3, however, is designed to be more robust and fixes a lot of bugs in Python 2, so in the future, expect to see a continued migration to Python 3. We are set up with Python 3 as our default, but since we are using Anaconda, if we want to set up a Python 2 instance at some point, it will be easy to do!

## 2. Confirm the installation worked properly

Once we are finished with the installation, check to make sure it installed correctly by performing a version check.

```sh
conda info
```

If you see a 4.X.X version number popup, and with platform and environment information, the installation worked. Now we can begin working with Conda.

***

## 3. The Anaconda 30-minute Test Drive

Now let’s familiarize with what exactly Anaconda allows us to do. On a basic level, Anaconda is a Python distribution that adds many features and streamlines work with the language. It does this by creating specific environments on your machine in which you can specify the packages that are installed and used, and easily lets you toggle between environments. Within the individual environments, you can perform analysis, run scripts, and develop code.

Environments are the bread and butter of Anaconda, because not all Python scripts you run will use the same packages, so you can customize exactly what you need, and create a sandbox that lets you try new things. Your environments will save the packages you have installed, allowing you to easily load an environment and run your scripts.

The Anaconda team has put together a very nice Test Drive that is designed to take about a half hour that will introduce you to concepts around Anaconda, including setting up an environment, toggling between environments, managing the Python version you are using, managing the Python packages you are using in your environments, and finally, removing or uninstall packages and environments if you no longer need them.

Follow the Test Drive at the following link:

[Anaconda 30-minute Test Drive](http://conda.pydata.org/docs/test-drive.html)

Working with Anaconda can make working with Python a much more pleasant experience. For additional resources, including cheatsheets and useful links, see the following materials.

*** -->