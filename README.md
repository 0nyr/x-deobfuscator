# Deobfuscate java X code

Need to deobfuscate the code given by some malicious teacher ? Here is a tool to help you so.

## run command

1. Copy/paste the code inside`input/Main.java`
2. Run`python3 x-deobfuscator.py`
3. You cleaned code is inside`input/Main.java`.

## Notes

### Potential characters

* invisible separator U+2063
* invisible plus U+2064
* invisible times U+2062

### Used characters

* U+200D : ZERO WIDTH JOINER [ZWJ]
* U+2002 : EN SPACE {nut}
* U+2003 : EM SPACE {mutton}
