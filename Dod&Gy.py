import subprocess

# runExe takes two parameters and runs CrackMe.exe.  It will return the result of CrackMe.exe as a string
# username: string
# pin: int
# return: string
def runExe(username, pin):
    out = subprocess.check_output([".\CrackMe.exe", username, str(pin)], shell=True)
    out = str(out, 'utf-8')
    out = out.strip()
    return out

# Example of how runExe is used (replace this with your solution)
output = runExe("bob@asdf.com", 1000)
print(output)