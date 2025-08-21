0x00-shell_basics

In this assignment we learned basic shell commands. These are commands that can be used in order to navigate the shell, look around the shell, manipulating files in the shell. For more information on the task please see: https://docs.google.com/document/d/1ytDZTI9MpY70xBZ53PM_yUeWhni9rNMVx7_UcO77hdQ/edit?usp=sharing


What is "the Shell"?

The shell is a program that takes commands from the keyboard and gives them to the operating system to perform. On most Linux systems a program called bash (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, sh, written by Steve Bourne) acts as the shell program.

What's a "Terminal?"
It's a program called a terminal emulator. This is a program that opens a window and lets you interact with the shell. There are a bunch of different terminal emulators we can use.

Navigation
The files on a Linux system are arranged in what is called a hierarchical directory structure. This means that they are organized in a tree-like pattern of directories  which may contain files and subdirectories. The first directory in the file system is called the root directory. The root directory contains files and subdirectories, which contain more files and subdirectories and so on and so on.

pwd
Since the command line interface cannot provide graphic pictures of the file system structure, we must have a different way of representing it. The directory we are standing in is called the working directory. To see the name of the working directory, we use the pwd command.

cd
To change the working directory (where we are standing in the maze) we use the cd command. To do this, we type cd followed by the pathname of the desired working directory. An absolute pathname begins with the root directory and follows the tree branch by branch until the path to the desired directory or file is completed. 

For example, there is a directory on your system in which most programs are installed. The pathname of the directory is /usr/bin. This means from the root directory (represented by the leading slash in the pathname) there is a directory called "usr" which contains a directory called "bin".

ls
The ls command is used to list the contents of a directory. It is probably the most commonly used Linux command

less
less is a program that lets us view text files. This is very handy since many of the files used to control and configure Linux are human readable.

file
As we wander around our Linux system, it is helpful to determine what kind of data a file contains before we try to view it. This is where the file command comes in.

Manipulating Files

cp 
The cp program copies files and directories. In its simplest form, it copies a single file. It can also be used to copy multiple files (and/or directories) to a different directory. 

mv
The mv command moves or renames files and directories depending on how it is used. It will either move one or more files to a different directory, or it will rename a file or directory.

rm
The rm command removes (deletes) files and directories. Using the recursive option (-r), rm can also be used to delete directories

mkdir
The mkdir command is used to create directories.
