

mystring="ORIGIN      1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed 61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn //"

mynewstring = mystring.replace("ORIGIN", "").replace("1","").replace("61","").replace(" ","").replace("//","")

print(mynewstring)