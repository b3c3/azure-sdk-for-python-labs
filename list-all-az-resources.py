# Import the needed credential and management objects from the libraries.
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
#import os

def get_resources_in_resource_group(resource_group_name : str, obj_resource_client : ResourceManagementClient):
    # Obtain the management object for resources.
    #resource_client = ResourceManagementClient(credential, subscription_id)

    # Retrieve the list of resources in "myResourceGroup" (change to any name desired).
    # The expand argument includes additional properties in the output.
    resource_list = obj_resource_client.resources.list_by_resource_group(resource_group_name, expand = "createdTime,changedTime")

    return resource_list

def list_resources_in_resource_group(lst_resources : list):
    # Show the groups in formatted output
    res_column_width = 36

    print("Resource".ljust(res_column_width) + "Type".ljust(res_column_width)
        + "Create date".ljust(res_column_width) + "Change date".ljust(res_column_width))
    print("-" * (res_column_width * 4))

    for resource in list(lst_resources):
        print(f"{resource.name:<{res_column_width}}{resource.type:<{res_column_width}}"
        f"{str(resource.created_time):<{res_column_width}}{str(resource.changed_time):<{res_column_width}}")

    return 0

#Main Program
if __name__ == "__main__":
    # Acquire a credential object using CLI-based authentication.
    credential = AzureCliCredential()

    # Retrieve subscription ID from environment variable.
    subscription_id = 'e33f5ab3-ea71-474d-9d49-5b250ff2b8c4' #os.environ["AZURE_SUBSCRIPTION_ID"]

    # Obtain the management object for resources.
    resource_client = ResourceManagementClient(credential, subscription_id)

    # Retrieve the list of resource groups
    az_resource_groups_list_paged = resource_client.resource_groups.list()
    lst_az_res_groups = list(az_resource_groups_list_paged)

    # Show the groups in formatted output
    COLUMN_WIDTH = 40

    print("Resource Group".ljust(COLUMN_WIDTH) + "Location")
    print("-" * (COLUMN_WIDTH * 2))

    for group in lst_az_res_groups: #list(group_list):
        print(f"{group.name:<{COLUMN_WIDTH}}{group.location}")

    #Try list all the resources within each resource group
    for group in lst_az_res_groups:
        print(f"\nList of Resources within the Resource Group [{group.name}]:")
        list_resources_in_resource_group(get_resources_in_resource_group(group.name, resource_client))

#End of Main Program