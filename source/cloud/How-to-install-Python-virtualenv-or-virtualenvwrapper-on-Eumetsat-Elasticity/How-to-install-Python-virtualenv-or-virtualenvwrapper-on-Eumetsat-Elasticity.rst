How to install Python virtualenv or virtualenvwrapper on |brand-name|
======================================================================

Virtualenv is a tool with which you are able to create isolated Python environments. It is mainly used to get rid of problems with dependencies and versions.
It also does not include permission setup. Generally virtualenvwrapper is a kind of extension for virtualenv. It owns wrappers which are in charge of creating and deleting environments. It is useful supplement for our current subject.

For purposes of this guide we will use virtual machine **vm01** with operating system **Ubuntu 22.04 LTS**.

Log in to your virtual machine and check python version (it should be preinstalled). Next step would be the installation of pip:

::

  eouser@vm01:~$ python3 --version

  Python 3.10.12

  eouser@vm01:~$ sudo apt install python3-pip

Confirm the pip3 installation by invoking:

::

 eouser@vm01:~$ pip3 -V

.. If pip3 is not installed, you will get the following message:

.. ::

.. Command 'pip3' not found, but can be installed with:
.. sudo apt install python3-pip

.. In that case, execute **sudo apt install python3-pip** as instructed.

If pip3 is installed, the **pip3 -V** command should give the output similar to this:

::

 pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

Install virtualenvwrapper via pip:

::

  eouser@vm01:~$ pip3 install virtualenvwrapper

Create a new directory to store your virtual environments, for example:

::

  mkdir .virtualenvs

Now we are going to modify **.bashrc** file by adding a row that will adjust every new virtual environment to use Python 3.
We will point virtual environments to the directory we created above (.virtualenvs) and we will also point to the locations of the virtualenv and virtualenvwrapper.
Open .bashrc file using editor, for example:

::

  vim ~/.bashrc

Navigate to the bottom of the .bashrc file and add following rows:

::

   #virtualenvwrapper settings:
   export WORKON_HOME=$HOME/.virtualenvs
   export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
   export VIRTUALENVWRAPPER_VIRTUALENV=/home/eouser/.local/bin/virtualenv
   source ./.local/bin/virtualenvwrapper.sh

After that save the .bashrc file.

Now we have to reload the bashrc script, to do it execute the command:

::

  source ~/.bashrc

If everything is set up properly, you should see following lines:

::

  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/premkproject
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/postmkproject
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/initialize
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/premkvirtualenv
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/postmkvirtualenv
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/prermvirtualenv
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/postrmvirtualenv
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/predeactivate
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/postdeactivate
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/preactivate
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/postactivate
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/get_env_details

Now create your first virtual environment **'test'** with 'mkvirtualenv' command:

::

  mkvirtualenv test

The output should look like this:

::

  created virtual environment CPython3.10.12.final.0-64 in 207ms
    creator CPython3Posix(dest=/home/eouser/.virtualenvs/test, clear=False, no_vcs_ignore=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/eouser/.local/share/virtualenv)
      added seed packages: pip==23.2.1, setuptools==68.2.0, wheel==0.41.2
    activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/test/bin/predeactivate
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/test/bin/postdeactivate
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/test/bin/preactivate
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/test/bin/postactivate
  virtualenvwrapper.user_scripts creating /home/eouser/.virtualenvs/test/bin/get_env_details

Now you should see name of your environment in the parenthesis before username, which means that you're working on your virtual environment.

::

  (test) eouser@vm01:~$

If you would like to exit current environment, just type the 'deactivate' command:

::

  (test) eouser@vm01:~$ deactivate
  eouser@vm01:~$

To start working on virtual environment type 'workon' command:

::

  eouser@vm01:~$ workon test
  (test) eouser@vm01:~$

To remove virtual environment invoke 'rmvirtualenv':

::

  eouser@vm01:~$ rmvirtualenv test
  Removing test...

To list all virtual environments use 'workon' or 'lsvirtualenv':

::

  eouser@vm01:~$ workon
  test-1
  test-2
  test-3
  eouser@vm01:~$ lsvirtualenv
  test-1
  ======


  test-2
  ======


  test-3
  ======


