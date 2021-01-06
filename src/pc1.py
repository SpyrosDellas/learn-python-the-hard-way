input = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

alphabet1 = "abcdefghijklmnopqrstuvwxyz"
alphabet2 = "cdefghijklmnopqrstuvwxyzab"
map = {}
for i in range(len(alphabet1)):
    map[alphabet1[i]] = alphabet2[i]

result = ""
for i in range(len(input)):
    if input[i] in map:
        result += map[input[i]]
    else:
        result += input[i]

print result
