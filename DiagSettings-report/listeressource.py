# Import the needed credential and management objects from the libraries.
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.monitor import MonitorManagementClient
import os, json
import progressbar
from tqdm import tqdm
import requests
# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = "1ddaf3cb-603f-4055-a51e-57d6d1d8fd09"


def get_r_d():
    try:
        url = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/azure-monitor/essentials/resource-logs-categories.md"
        r = requests.get(url)
        r.iter_lines()
        list_resource= []
        for c in r.iter_lines():
            value = c.decode()
            if "## microsoft." in value:
                print(value.split('## ')[1])
                list_resource.append(value.split('## ')[1])
            elif "## Microsoft." in value:
                print(value.split('## ')[1])
                list_resource.append(value.split('## ')[1])
        print(list_resource)
        # Serializing json
        json_object = json.dumps(list_resource, indent=4)
        
        # Writing to sample.json
        with open("microsoft.json", "w") as outfile:
            outfile.write(json_object)
        return list_resource
    except Exception as e:
        print(f"Invalid URL or some error occured while making the GET request to the specified URL{e}")

microsoft_list = get_r_d()

def check_category(r_id):
    rc=resource_client_m.diagnostic_settings_category.list(r_id)
    # print(f"le rc : {rc}")
    for t in list(rc):
        pass
        # print(t)
    
    
# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

# Retrieve the list of resource groups
group_list = resource_client.resource_groups.list()
r_list = resource_client.resources.list()

# Show the groups in formatted output
column_width = 40

print("Resource Group".ljust(column_width) + "Location")
print("-" * (column_width * 2))

for group in list(group_list):
    print(f"{group.name:<{column_width}}{group.location}")
    
print("Resource ".ljust(column_width) + "Location")
print("-" * (column_width * 2))
resource_client_m = MonitorManagementClient(credential, subscription_id)
# print(f"il y a {len(list(r_list))}")
l = []
er =[]
for r in progressbar.progressbar(r_list):
    try:
        print(29 * "*")
        print(r.type)
        d = {}
    
        if (True if r.type in x else False for x in microsoft_list ):
            print("supported")
            d = resource_client_m.diagnostic_settings.list(r.id)
            for i in d:
                # print(f"{i}\n")
                d={}
                d['workspace_id']=i.workspace_id
                d['rname']= r.name
                d['rloc']= r.location
                d['type']= r.type
                l.append(d)
                check_category(r.id)
        else:
            print("notttttttttttttttttttttttttttttttttt")
        
    except Exception as e:
        print(e)
print(l)
# microsoft.network/localnetworkgateways
    
# Serializing json
json_object = json.dumps(l, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)