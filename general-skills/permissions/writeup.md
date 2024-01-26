## Permissions

difficulty: medium

---

sol:

ls -l shows that the root dir has blocked reading permissions for the dir

run sudo -l to see your sudo persmissions 

sudo -l shows that we are allowed to run vi as root
from within vi we can start a shell with !/bin/bash

in this shell we can see that we now are root with whoami

now we can read the contents of the /root.

when ls-ing the dir we dont see any files. by running ls -a we can see that this is because they are dotfiles
