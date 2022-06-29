# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

     # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = 'f3f96dd9-f9f8-4652-b65b-b9c14602d567'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '29eaf41d-9356-44cf-9a7e-fdcb0ade3ee7'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '0ae51e19-07c8-4e4b-bb6d-648ee58410f4'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '6dcd8115-d760-4f94-90e6-14d7ae707624'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = '18s8Q~81PJRYhQRVmoNKvXepB17xoxmmStpAEb0j'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''
