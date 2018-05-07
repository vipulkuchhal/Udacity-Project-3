LOG ANALYSIS PROJECT-3

AIM:
1. Find out the most popular 3 articles.
2. Find out which authors get the most page views on 
   their articles.
3. Find days when there were more than 1% requests that 
   led to errors.

 Run the program:

First of all, there are some files and softwares required for the project.
- Download vagrant from https://www.vagrantup.com/downloads.html    
  and install it.
- We need a VirtualBox to run linux using vagrant.Download it     
  from https://www.virtualbox.org/wiki/Downloads.
- Download the config and setup files of vagrant.
- Download the database(zip file) on which operations are  
  performed.Source: udacity github.
- Unzip it and extract the file in vagrant directory.
- Download the project.
- Unzip it and extract all files in vagrant directory.   

Now:
- Open GitBash and change the directory 
  to that of vagrant file.
- Run command "vagrant up" to setup Virtual Machine.
- Now, run "vagrant ssh" to login.
- cd into the directory cd /vagrant/Project
- Run psql -d news -f newsdata.sql for loading the data.

To Run, 
- Simply run the command "python newProject3.py".

You can check the sample output in text file named "Sample Output" that you can find in following folder.
