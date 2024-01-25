# Static ain't always noise

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/static)? This [BASH](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/ltdis.sh) script might help!

---

sol:

~~~bash
bash ltis.sh static
~~~

this gives you a file called "static.ltdis.strings.txt", the flag is in plaintext

the script basically just runs [objdump](https://man7.org/linux/man-pages/man1/objdump.1.html) on the static file.
