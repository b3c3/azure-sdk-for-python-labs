# Import the needed credential and management objects from the libraries.
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
#import os
#from bu import dosomething

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = 'e33f5ab3-ea71-474d-9d49-5b250ff2b8c4' #os.environ["AZURE_SUBSCRIPTION_ID"]

# Retrieve the resource group to use, defaulting to "myResourceGroup".
resource_group = 'bu-c6m3-kick-off' #os.getenv("RESOURCE_GROUP_NAME", "myResourceGroup")

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

# Retrieve the list of resources in "myResourceGroup" (change to any name desired).
# The expand argument includes additional properties in the output.
resource_list = resource_client.resources.list_by_resource_group(
    resource_group, expand = "createdTime,changedTime")

# Show the groups in formatted output
column_width = 36

print("Resource".ljust(column_width) + "Type".ljust(column_width)
    + "Create date".ljust(column_width) + "Change date".ljust(column_width))
print("-" * (column_width * 4))

for resource in list(resource_list):
    print(f"{resource.name:<{column_width}}{resource.type:<{column_width}}"
       f"{str(resource.created_time):<{column_width}}{str(resource.changed_time):<{column_width}}")

