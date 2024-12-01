from Office365.SharePoint.ClientContext import ClientContext
from Office365.Runtime.Authentication.ClientCredential import ClientCredential
from Office365.SharePoint.Files.file import FileCreationInformation
import os

def get_sharepoint_context(site_url: str, client_id: str, client_secret: str) -> ClientContext:
    client_credentials = ClientCredential(client_id, client_secret)
    ctx = ClientContext(site_url).with_credentials(client_credentials)
    return ctx

def get_sharepoint_lists(site_url: str, client_id: str, client_secret: str):
    ctx = get_sharepoint_context(site_url, client_id, client_secret)
    lists = ctx.web.lists
    ctx.load(lists)
    ctx.execute_query()
    lists_data = [{"title": list_obj.properties["Title"], "id": list_obj.properties["Id"]} for list_obj in lists]
    return lists_data

def upload_file_to_sharepoint(site_url: str, client_id: str, client_secret: str, library_name: str, file_name: str, file_content: bytes):
    ctx = get_sharepoint_context(site_url, client_id, client_secret)
    target_library = ctx.web.lists.get_by_title(library_name)
    ctx.load(target_library)
    ctx.execute_query()
    
    file_info = FileCreationInformation()
    file_info.content = file_content
    file_info.url = os.path.join(target_library.properties["RootFolder"]["ServerRelativeUrl"], file_name)
    file_info.overwrite = True
    
    target_file = target_library.rootFolder.files.add(file_info)
    ctx.execute_query()
    return {"file_url": target_file.properties["ServerRelativeUrl"]}
