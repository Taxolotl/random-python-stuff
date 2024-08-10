import sys

hex = open(sys.argv[1], "r")
gpl = open(sys.argv[2], "w")
gpl.write("GIMP Palette\n#\n# Generated with Taxolotl's hex2gpl tool\n#\n")

for hex_code in hex:
    r, g, b = str(int(hex_code[:2], 16)).rjust(3), str(int(hex_code[2:4], 16)).rjust(3), str(int(hex_code[4:], 16)).rjust(3)
    gpl.write(f"{r} {g} {b} Untitled\n")

hex.close()
gpl.close()