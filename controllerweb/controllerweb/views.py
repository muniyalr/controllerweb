import subprocess


from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def runplaybook(request,rolename,ipaddress):

    # Create a command to run the playbook as below
    # ansible-playbook -i '10.20.11.11,' /home/ubuntu/ansible/site.yml
    # Also it requires 'hosts: all' in your playbook to execute on the private ip
    cmd="ansible-playbook -i '"+ipaddress+",' /home/ubuntu/ansible/"+rolename+".yml"

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    responseValue="Success"
    if p.returncode != 0 or stderr:
       responseValue=stdout

    return HttpResponse(responseValue+"\n")
