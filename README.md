# skill-communicate

Communication with voice command between picroft or Desktop and another picroft with skill-gpio8s installed.
The communication is made using an ssh connection sending say_to_mycroft command to a remote picroft.

Local (desktop or picroft) skill-communicate --> remote (picroft with skill-gpio8s)

From local Picroft you are able to run remote picroft commands


# Requirement

local Picroft - skill-communicate

remote Picroft - skill-gpio8s or skill-gpio8s-lcd


# Installation


Step 1. Create a public/private keys with “ssh-keygen” (ENTER through everything):

 user@host:~/.ssh$ ssh-keygen -t rsa
 
      Generating public/private rsa key pair.
 
      Enter file in which to save the key (/home/toly/.ssh/id_rsa): 		[ENTER]
      Enter passphrase (empty for no passphrase): 				[ENTER]
      Enter same passphrase again: 							[ENTER]
 
      Your identification has been saved in /home/user/.ssh/id_rsa.
      Your public key has been saved in /home/user/.ssh/id_rsa.pub.
      The key fingerprint is:
      66:fd:11:ca:2d:21:b9:73:c1:b6:fa:1d:b2:2c:71:cd user@host
 
      The key's randomart image is:
      +--[ RSA 2048]----+
      |                         |
      |           .             |
      |          . o           |
      |         o + o         |
      |        E S.o o       |
      |       o. .+.o .       |
      |       . +o o.         |
      |        +. o...        |
      |       ... ..=.         |
      +-----------------+
      
      At this point the public and private keys should be created and saved into “~/.ssh” directory:

      user@host:~/.ssh$ ls -l
      total 20
      -rw------- 1 user group 1675 2009-03-10 14:18 id_rsa
      -rw-r--r-- 1 user group 392 2009-03-10 14:18 id_rsa.pub
      -rw-r--r-- 1 user group 8642 2009-03-10 12:10 known_hosts
      
      Step 2. Add identity to the local ssh authorizer with “ssh-add”.

If you “entered” through the “Enter file in which to save the key (/home/toly/.ssh/id_rsa)” in the previous step, then your identity file should be “id_rsa”:

      user@host:~/.ssh$ ssh-add id_rsa
Otherwise replace “id_rsa” with the file you chose to save your identity in.

In case of a friendly “Could not open a connection to your authentication agent.” error message, start “ssh-agent” as:

eval `ssh-agent`
and re-run “ssh-add”.

Step 3. Copy the public key to the remote host ( server ) under “~/.ssh”:

From the step above “id_rsa.pub” would be the public key that needs to be copied to the remote system you would like to run commands on.

      user@host:~/.ssh$ scp id_rsa.pub remoteuser@remotehost.com:~/.ssh/
from the remote host

Step 4. On remote host add this public key to “authorized_keys”:

      remoteuser@remotehost:~$ cd ~/.ssh
      remoteuser@remotehost:~/.ssh~$ cat id_rsa.pub >> authorized_keys
Step 5. Change “authorized_keys” permissions to allow only you to read/write it:

      remoteuser@remotehost:~/.ssh$ chmod 600 authorized_keys
      
    Step 6. Now you can run any command on the remote box from the local box with no password:

Let’s see what that remote box is running at:

       user@host:~$ ssh remoteuser@remotehost.com  uname -a
 
       Linux remotehost 2.6.27-01-generic #1 SMP Thu Mar 21 10:34:21 UTC 2009 i686 GNU/Linux  
       
# skill install - to local Picroft

msm install https://github.com/smolino/skill-communicate.git

edit "__init__.py" and change the ip address ssh pi@your_ip_remote_address

# Command

Hey Mycroft, send turn light on

Hey Mycroft, send turn light off

Hey Mycroft, send Turn Switch On

Hey Mycroft, send Turn Switch Off

Hey Mycroft, send Turn Fan On

Hey Mycroft, send Turn Fan Off

Hey Mycroft, send Turn Living On

Hey Mycroft, send Turn Living Off

Hey Mycroft, send Turn Bathroom On

Hey Mycroft, send Turn Bathroom Off

Hey Mycroft, send Turn Kitchen On

Hey Mycroft, send Turn Kitchen Off

Hey Mycroft, send Turn Lamp On

Hey Mycroft, send Turn Lamp Off

Hey Mycroft, send Turn Bedroom On

Hey Mycroft, send Turn Bedroom Off

and mycroft respond:

sending turn light on

sending turn light off


