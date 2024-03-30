#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil
import console
"""c"""
import os
cc = "file.json"
if not os.path.exists(cc):
    try:
        from models.engine.file_storage import FileStorage
        cc = FileStorage._FileStorage__file_path
    except:
        pass
if os.path.exists(cc):
    os.remove(cc)


"""sc"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("console.py", "tmp_console_main.py")

"""cdc"""
with open("tmp_console_main.py", "r") as fi:
    cl = fi.readlines()
    with open("console.py", "w") as fo:
        im = False
        for l in cl:
            if "__main__" in l:
                im = True
            elif im:
                if "cmdloop" not in l:
                    fo.write(l.lstrip("    "))
            else:
                fo.write(l)

"""c"""
c = "HBNBCommand"
for n, o in inspect.getmembers(console):
    if inspect.isclass(o) and issubclass(o, cmd.Cmd):
        c = o

mc = c(stdout=io.StringIO(), stdin=io.StringIO())
mc.use_rawinput = False

"""c"""
def exec_command(mc, tc, ll=1):
    mc.stdout = io.StringIO()
    rs = sys.stdout
    sys.stdout = mc.stdout
    mc.onecmd(tc)
    sys.stdout = rs
    l = mc.stdout.getvalue().split("\n")
    return "\n".join(l[(-1*(ll+1)):-1])

"""vb"""
r = exec_command(mc, "create Place")
if r is None or r == "":
    print("FAIL: No ID retrieved")

mi = r

r = exec_command(mc, "show Review {}".format(mi))
if r is None or r == "":
    print("FAIL: no output")
ss = "** no instance found **"
if r != ss:
    print("FAIL: wrong output \"{}\" instead of \"{}\"".format(result,
                                                               search_str))

print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
