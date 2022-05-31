a = True
b = False

# and statements return true if both values are true
#╔═══════╦═══════╦════════╗
#║   a   ║   b   ║ Result ║
#╠═══════╬═══════╬════════╣
#║ False ║ False ║ False  ║
#║ False ║ True  ║ False  ║
#║ True  ║ False ║ False  ║
#║ True  ║ True  ║ True   ║
#╚═══════╩═══════╩════════╝
if(a and b):
    print("A and B!")


# or statements return true if any value is true
#╔═══════╦═══════╦════════╗
#║   a   ║   b   ║ Result ║
#╠═══════╬═══════╬════════╣
#║ False ║ False ║ False  ║
#║ False ║ True  ║ True   ║
#║ True  ║ False ║ True   ║
#║ True  ║ True  ║ True   ║
#╚═══════╩═══════╩════════╝
if(a or b):
    print("A or B!")

# not inverses the value
#╔═══════╦════════╗
#║   a   ║ Result ║
#╠═══════╬════════╣
#║ False ║ True   ║
#║ True  ║ False  ║
#╚═══════╩════════╝
if(not a):
    print("Not A!")