import subprocess as subproc
import re

command_output = subproc.run(["netsh", "wlan", "show", "profiles"],capture_output=True).stdout.decode()

profile_name = re.findall("All User Profile     :(.*)\r", command_output)

wifi_list = list()

if len(profile_name)!= 0:
       for name in profile_name:
           wifi_profile = dict()
           nametext =format(name).strip()
       #    print(test)
           profile_info = subproc.run(["netsh", "wlan", "show", "profile", (nametext)], capture_output  =True).stdout.decode()
         #  print("stdout result:", profile_info)

           if re.search("Security key           : Absent",profile_info):
              continue
           else:
               wifi_profile["ssid"] = nametext
               profile_info_pass = subproc.run(["netsh", "wlan", "show", "profile", nametext, "key=clear"], capture_output = True).stdout.decode()

               password = re.search("Key Content            :(.*)\r", profile_info_pass)
               if password == None:
                   wifi_profile["password"] =  None
               else:
                  wifi_profile["password"] = password
               wifi_list.append(wifi_profile)
for x in range (len(wifi_list)):
    print(wifi_list[x])