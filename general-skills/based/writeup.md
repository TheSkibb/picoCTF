## based

difficulty: medium

---

sol:

nc-ing the given url gives you different challenges of decryting different inputs

using [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8/disabled)From_Hex('Auto'/disabled)From_Base32('A-Z2-7%3D',true/disabled)From_Base64('A-Za-z0-9%2B/%3D',true,false/disabled)From_Decimal('Space',false/disabled)From_Octal('Space')&input=MTQ2IDE0MSAxNTQgMTQzIDE1NyAxNQ) i can rapidly decode them and explore what encodings to use
(remember to copy full input)

first input was binary:
01101101 01100001 01110000 -> map


second was [octal](https://en.wikipedia.org/wiki/Octal):
154 151 155 145 -> lime

discvery here was that if you have trailing spaces for octal encoding the encoding is not valid, and decoding does not work

third was [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal):
66616c636f6e -> falcon


