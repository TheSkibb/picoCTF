## special

difficulty: hard

---

sol:

by testing different ways of writing commands i found that you can trick the shell by using parenthesis.
i was trying if you could launch commands in subshells using $(ls) and got the response "blargh not found", which signified that there was a file or dir called blargh in the current dir.

while testing some more i found that inputing / gives you the message "Absolutely not paths like that, please!" which was a good hint that i was on the right track

from some more testing i found that you could list the files in the current dir by invoking it directly in a subshell: (/bin/ls)
this showed that, in fact there is a file called blargh.

i also found that i could use grep and by running  $(grep pico blargh) i got the message that blargh was a directory

i ran (/bin/ls blargh), which listed a file called flag.txt
$(grep pico blargh/flag.txt) gave me the flag

from later testing, i also found that i could have used (/bin/cat blargh)

---

one of the main things i learned from this was the difference between $() and () in shells

$() runs a subshell and returns the result as an argument to the current shell.

() only runs the command in the subshell



