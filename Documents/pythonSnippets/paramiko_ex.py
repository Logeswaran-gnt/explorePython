# 72.30.36.194
# ravi
# msys123
import paramiko,time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('172.30.36.194', username='ravi', password='msys123')
    print("connection success")
except paramiko.SSHException:
    print ("Connection Failed")
    quit()
time.sleep(5)
remote_conn = ssh.invoke_shell()
time.sleep(5)
stdin, stdout, stderr = ssh.exec_command("ls")
result=stdout.read()
#aaa=remote_conn.send("phydrv")
#print(aaa)
print(stdin.write)
# print stdout.read()
print result


'''result=""
result+=remote_conn.send("\n")
result+=remote_conn.send("ls")
result+=remote_conn.send("pwd")
print result'''

'''result=""
#pdb.set_trace()
stdin, stdout, stderr = ssh.exec_command("ls")
result+=stdout.read()
stdin1, stdout1, stderr1 = ssh.exec_command("pwd")
result+=stdout1.read()
print(result)'''
