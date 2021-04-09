MMIV-DLN-AI-2021 Setup for the Biomedical imaging course module

# Setting up your system for this biomedical imaging course module

(Assuming Anaconda is already in place, go directly to "Installing the `mmiv-dln-img` conda environment")


#### Are you using Mac?
Then you must install [xcode](https://developer.apple.com/xcode/resources) (for free) before you start. See also [here](https://www.youtube.com/watch?v=m9m6HozVjo8) and [here](https://medium.com/@LondonAppBrewery/how-to-download-and-setup-xcode-10-for-ios-development-b63bed1865c). <br>Thereafter (see also [here](https://stackoverflow.com/questions/9329243/how-to-install-xcode-command-line-tools)):


- Launch the `terminal.app`, found in /Applications/Utilities/
- Type the following command string: `xcode-select --install`


#### On Mac, Windows and Linux we will use the [command line](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_interpreter) (shell)
See e.g. [Basic Unix Commands](https://people.duke.edu/~ccc14/pcfb/unix.html) and [Computing Skills for Biologists](https://computingskillsforbiologists.com) [[here](https://github.com/CSB-book/CSB)] if this is unfamiliar to you. See also the
[Unix Shell](http://swcarpentry.github.io/shell-novice) lessons (thanks to [Anne Fouilloux](https://www.mn.uio.no/geo/english/people/adm/annefou), UiO)

#### ... and luckily also the [Jupyter notebook](https://www.nature.com/articles/d41586-018-07196-1)
- for openness [!](https://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261) and reproduciblity [!](https://arxiv.org/pdf/1810.08055.pdf)

## GitHub:
The course code is hosted on the code-sharing platform GitHub (where you now are reading this). If you do not have a GitHub account already you should make one now (https://github.com/join). We recommend that you are using the platform for your own projects during the course. Hence:


- Create an account on GitHub (https://github.com) using the `Sign up for GitHub` form on the right side of the page.
- Send your GitHub username to your instructor.
- Once your instructor adds you to the course GitHub organization you will receive an email asking you to accept the invitation. Click on the link to accept.
- Check if this worked
  - Go to https://github.com.
  - Sign in if necessary.
  - In the upper left corner click on the drop down with your name.
  - Confirm that the name of the course GitHub organization is present

## Anaconda:
We recommend installing Python via the [Anaconda Distribution](https://www.anaconda.com/download). Be sure to use the "Python 3.8" version. We will use the Conda Package Management System within the Anaconda Distribution. From the [documentation](https://conda.io/docs):
> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.

After the installation run `python --version` in a terminal window (in "**Anaconda Powershell Prompt**" if you are using Windows). If the output show "Python 3.8" (and "Anaconda") you are good to go.


# Installing the `mmiv-dln-img` conda environment

### Configure the conda environment `mmiv-dln-img` from this directory
```bash
conda env create -f environment-img.yml
```

### Activate the environment:
```bash
conda activate mmiv-dln-img
```

### Install the specific `MMIV-DLN-IMG` Jupyter kernel:
```bash
python -m ipykernel install --user --name mmiv-dln-img --display-name "MMIV-DLN-IMG"
```



## Update:
The code and environment can be updated during the course. Run the following commands regularly from within this directory:

* Update this particular `mmiv-dln-img` environment:
```bash
conda activate mmiv-dln-img
conda env update --file environment-img.yml
```
