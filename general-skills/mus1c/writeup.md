## music

difficulty: hard

---

sol:

would not have solved this without finding a writeup [online](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/mus1c.md)

since the hint is "Do you think you can master rockstar?", you are meant to use the lyrics for a programming language called rockstar

pasting the lyrics into an [online interpreter](https://codewithrockstar.com/online) we get an output of a series of numbers

~~~
114
114
114
111
99
107
110
114
110
48
49
49
51
114
~~~

this can be converted into ascii characters using cyberchef "from charcode" with delimiter: linefeed, and base 10 (base was found by playing around)
