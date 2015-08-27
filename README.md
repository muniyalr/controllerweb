# controllerweb
Pyton Django App to invoke ansible playbook for a particular private ip

Usage : Start the app as a django app
```
python manage.py runserver :8000
```
Executing ansible-playbook on a particular host

site.yml file hosts should be all
- name: apply configuration on the host
  hosts: all

```
ansible-playbook -i '10.10.11.11,' site.yml
````

AWS-Userdata to invoke the ansible-playbook on server startup
The ansible playbook is executed only when the server is started up for the
first time

Use userdata below to invoke the ansible-playbook from the controller server

```
"#!/bin/bash\n",
"mkdir /etc/ansible\n",
"echo '[defaults]' > /etc/ansible/ansible.cfg",
"echo 'host_key_checking = False' >> /etc/ansible/ansible.cfg\n"
"privateip=`curl http://169.254.169.254/latest/meta-data/local-ipv4`",
"\n",
"curl http://",{"Ref" : "ControllerDNSName"}, ":8000/runplaybook/myeeapp/${privateip}/ >> /var/log/app.log 2>>/var/log/app.log",
"\n",
```
