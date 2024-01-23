text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(':')
# print(ipos) # 18
piece = text[ipos + 2:]
# print(piece)
value = float(piece)

print(value)