## About the connector
Cloudflare Web Application Firewall (WAF) integration allows customers to manage firewall rules, filters, and IP Lists. It also allows to retrieve zones list for each account.
<p>This document provides information about the Cloudflare WAF Connector, which facilitates automated interactions, with a Cloudflare WAF server using FortiSOAR&trade; playbooks. Add the Cloudflare WAF Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cloudflare WAF.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-cloudflare-waf</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Cloudflare WAF server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cloudflare WAF server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cloudflare WAF</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the cloudflare WAF server to connect and perform automated operations.</td>
</tr><tr><td>Account ID</td><td>Specify the Account ID to access the endpoint to which you will connect and perform the automated operations.</td>
</tr><tr><td>Zone ID</td><td>Specify the Zone ID to access the endpoint to which you will connect and perform the automated operations.</td>
</tr><tr><td>API Key</td><td>Specify the Global API Key to access the endpoint to which you will connect and perform the automated operations.</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Firewall Rule</td><td>Allows users to add or create a new firewall rule in a firewall configuration</td><td>create_firewall_rule <br/>Investigation</td></tr>
<tr><td>Update Firewall Rule</td><td>Allows users to modify or edit an existing firewall rule within the firewall configuration</td><td>update_firewall_rule <br/>Investigation</td></tr>
<tr><td>List Firewall Rules</td><td>Get a list of firewall rules that are currently configured for your Cloudflare account or for a specific domain or zone within your account</td><td>list_firewall_rules <br/>Investigation</td></tr>
<tr><td>Delete Firewall Rule</td><td>Remove or delete an existing firewall rule from the firewall configuration</td><td>delete_firewall_rule <br/>Investigation</td></tr>
<tr><td>Create Filter</td><td>Allows users to add a new filter to their WAF configuration</td><td>create_filter <br/>Investigation</td></tr>
<tr><td>List Filters</td><td>Retrieve a list of filters configured within the Cloudflare Web Application Firewall (WAF) settings</td><td>list_filters <br/>Investigation</td></tr>
<tr><td>Update Filter</td><td>Modify and update the configuration settings of existing filters within their WAF configuration</td><td>update_filter <br/>Investigation</td></tr>
<tr><td>Delete Filter</td><td>Allows users to remove a specific filter from their WAF configuration.</td><td>delete_filter <br/>Investigation</td></tr>
<tr><td>List Zones</td><td>Retrieves a list of all zones associated with the user's Cloudflare account</td><td>list_zones <br/>Investigation</td></tr>
<tr><td>Get IP Lists</td><td>Allows users to retrieve information about IP lists configured within their Cloudflare account</td><td>get_ip_lists <br/>Investigation</td></tr>
<tr><td>Create IP List</td><td>Create a new IP list with a specified name and associated IP addresses.</td><td>create_ip_list <br/>Investigation</td></tr>
<tr><td>Delete IP List</td><td>Remove an existing IP list from their Cloudflare account</td><td>delete_ip_list <br/>Investigation</td></tr>
<tr><td>Create IP Items List</td><td>Add or append new items, such as IP addresses, to a specific list</td><td>create_ip_items_list <br/>Investigation</td></tr>
<tr><td>Get IP List Items</td><td>Retrieves the list of IP addresses items from a specific list</td><td>get_ip_list_item <br/>Investigation</td></tr>
<tr><td>Update IP List Items</td><td>Removes all existing items from the list and adds the provided items to the list.</td><td>update_ip_list_item <br/>Investigation</td></tr>
<tr><td>Delete IP List Items</td><td>Allows users to remove specific items, such as IP addresses, from an IP list</td><td>delete_ip_list_item <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Firewall Rule
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Description</td><td>Specify a description or name for the new firewall rule being created
</td></tr><tr><td>Action</td><td>Specify the action or behavior to be taken when the rule's conditions are met
</td></tr><tr><td>Products</td><td>Select one or more products or services to which the firewall rule applies
</td></tr><tr><td>Paused</td><td>Specify whether the newly created firewall rule should be initially paused or inactive
</td></tr><tr><td>Priority</td><td>Specify the precedence or order of the newly created firewall rule relative to other rules
</td></tr><tr><td>Reference Tag</td><td>Specify an association of a reference or identifier with the newly created firewall rule
</td></tr><tr><td>Filter ID</td><td>Specify the identifier of an existing filter to be associated with the newly created firewall rule. Required if filter_expression is unspecified.
</td></tr><tr><td>Filter Expression</td><td>Specify the identifier of an existing filter to be associated with the newly created firewall rule. Required if filter_expression is unspecified. more info: https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/'
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "action": "",
            "description": "",
            "id": "",
            "paused": "",
            "priority": "",
            "products": [],
            "ref": "",
            "filter": {
                "description": "",
                "expression": "",
                "id": "",
                "paused": "",
                "ref": ""
            }
        }
    ],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    }
}</pre>
### operation: Update Firewall Rule
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Rule ID</td><td>Specify the unique identifier of the firewall rule that needs to be updated.
</td></tr><tr><td>Description</td><td>Specify the description or name of the existing firewall rule to modify or update
</td></tr><tr><td>Action</td><td>Specify the action or behavior to be taken when the updated rule's conditions are met
</td></tr><tr><td>Products</td><td>Select one or more products or services to which the updated firewall rule applies
</td></tr><tr><td>Paused</td><td>To update a firewall rule, it can be set to either active or inactive. To choose this option, the firewall rule must be paused or inactive
</td></tr><tr><td>Priority</td><td>Specify the precedence or order of the firewall rules to be updated
</td></tr><tr><td>Reference Tag</td><td>Specify a reference or identifier for the firewall rule to be updated
</td></tr><tr><td>Filter ID</td><td>Specifies the identifier of an existing filter to be associated with the updated firewall rule. Can not update or delete rule filter, only add a new filter
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "action": "",
            "description": "",
            "id": "",
            "paused": "",
            "priority": "",
            "products": [],
            "ref": "",
            "filter": {
                "description": "",
                "expression": "",
                "id": "",
                "paused": "",
                "ref": ""
            }
        }
    ],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    }
}</pre>
### operation: List Firewall Rules
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Action</td><td>Specifies the action or operation to be performed when retrieving firewall rules. Must be an exact match
</td></tr><tr><td>Description</td><td>Specify this parameter allows you to filter firewall rules based on their description or name
</td></tr><tr><td>Rule ID</td><td>Specify the unique identifier of the firewall rule
</td></tr><tr><td>Paused</td><td>Specify this parameter value true, indicates that the firewall rule is currently paused
</td></tr><tr><td>Page Number</td><td>Specify the page number of paginated results
</td></tr><tr><td>Record Per Page</td><td>Specify this parameter to indicate the number of firewall rules per page
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "action": "",
            "description": "",
            "id": "",
            "paused": "",
            "priority": "",
            "products": [],
            "ref": "",
            "filter": {
                "description": "",
                "expression": "",
                "id": "",
                "paused": "",
                "ref": ""
            }
        }
    ],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    }
}</pre>
### operation: Delete Firewall Rule
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Rule ID</td><td>Specify the unique identifier of the firewall rule to delete
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "action": "",
            "description": "",
            "id": "",
            "paused": "",
            "priority": "",
            "products": [],
            "ref": "",
            "filter": {
                "description": "",
                "expression": "",
                "id": "",
                "paused": "",
                "ref": ""
            }
        }
    ],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    }
}</pre>
### operation: Create Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Zone ID</td><td>Specifies the unique identifier of the Cloudflare zone where the filter will be applied
</td></tr><tr><td>Description</td><td>Allows users to provide a description or additional information about the newly created filter
</td></tr><tr><td>Expression</td><td>Specify this parameter allows users to define the filtering criteria or rules for the newly created filter
</td></tr><tr><td>Reference ID</td><td>Specifying this parameter allows users to associate a reference or identifier with the newly created filter
</td></tr><tr><td>Paused</td><td>Specifying this parameter allows users to specify whether the newly created filter should be initially paused or active
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "description": "",
            "expression": "",
            "id": "",
            "paused": "",
            "ref": ""
        }
    ],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    }
}</pre>
### operation: List Filters
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter ID</td><td>Specify the identifier of a specific filter for retrieval.
</td></tr><tr><td>Description</td><td>Allows users to filter the list of filters based on their descriptions
</td></tr><tr><td>Expression</td><td>Specify a search expression or pattern to filter the list of filters returned by the Cloudflare WAF
</td></tr><tr><td>Reference ID</td><td>Specifying this parameter allows users to filter the list of filters based on their reference or identifier.
</td></tr><tr><td>Page Number</td><td>Specify the page number of paginated results
</td></tr><tr><td>Per Page</td><td>Specify this parameter to indicate the number of filters per page
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "description": "",
            "expression": "",
            "id": "",
            "paused": "",
            "ref": ""
        }
    ],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    }
}</pre>
### operation: Update Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter ID</td><td>Specifies the unique identifier of the filter that the user intends to update
</td></tr><tr><td>Zone ID</td><td>Specifies this parameter facilitates the modification of the Cloudflare zone to which a specific filter is associated
</td></tr><tr><td>Description</td><td>Specifying this parameter allows users to update the description or additional information associated with a specific filter
</td></tr><tr><td>Expression</td><td>Specifying this parameter allows users to modify the filtering criteria or rules associated with a specific filter
</td></tr><tr><td>Reference ID</td><td>Specifying this parameter allows users to modify or update the reference or identifier associated with a specific filter
</td></tr><tr><td>Paused</td><td>Provides users with the ability to control the activation status of a specific filter
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "description": "",
            "expression": "",
            "id": "",
            "paused": "",
            "ref": ""
        }
    ],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    }
}</pre>
### operation: Delete Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter ID</td><td>Specifies the unique identifier of the filter that users want to remove from their WAF configuration
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "description": "",
            "expression": "",
            "id": "",
            "paused": "",
            "ref": ""
        }
    ],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    }
}</pre>
### operation: List Zones
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Match</td><td>Specifies this parameter is used to filter the list of zones based on specific criteria
</td></tr><tr><td>Name</td><td>Specifying this parameter allows users to filter the list of zones based on the zone name
</td></tr><tr><td>Account Name</td><td>Specifying this parameter allows users to filter the list of zones based on the name of the Cloudflare account associated with each zone
</td></tr><tr><td>Order</td><td>Specifying this parameter allows users to specify the order in which the list of zones should be sorted in the response. Possible values :
name
status
account.id
account.name
</td></tr><tr><td>Status</td><td>Specifying this parameter allows users to filter the list of zones based on their current operational status
</td></tr><tr><td>Direction</td><td>Specifying this parameter allows users to specify the sorting direction of the list of zones based on certain criteria
</td></tr><tr><td>Page Number</td><td>Specify the page number of paginated results
</td></tr><tr><td>Per Page</td><td>Specify this parameter to indicate the number of zones per page
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "success": "",
    "result_info": {
        "count": "",
        "page": "",
        "per_page": "",
        "total_count": ""
    },
    "result": [
        {
            "account": {
                "id": "",
                "name": ""
            },
            "activated_on": "",
            "created_on": "",
            "development_mode": "",
            "id": "",
            "meta": {
                "cdn_only": "",
                "custom_certificate_quota": "",
                "dns_only": "",
                "foundation_dns": "",
                "page_rule_quota": "",
                "phishing_detected": "",
                "step": ""
            },
            "modified_on": "",
            "name": "",
            "original_dnshost": "",
            "original_name_servers": [],
            "original_registrar": "",
            "owner": {
                "id": "",
                "name": "",
                "type": ""
            },
            "vanity_name_servers": []
        }
    ]
}</pre>
### operation: Get IP Lists
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page Number</td><td>Specify the page number of paginated results
</td></tr><tr><td>Per Page</td><td>Specify this parameter to indicate the number of IP list items per page
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "created_on": "",
            "description": "",
            "id": "",
            "kind": "",
            "modified_on": "",
            "name": "",
            "num_items": "",
            "num_referencing_filters": ""
        }
    ],
    "success": true
}</pre>
### operation: Create IP List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specifies the name of the new IP list to be created
</td></tr><tr><td>Description</td><td>Specify this parameter to allows users to provide additional information or details about the new IP list being created
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": {
        "0": "",
        "created_on": "",
        "description": "",
        "id": "",
        "kind": "",
        "modified_on": "",
        "name": "",
        "num_items": "",
        "num_referencing_filters": ""
    },
    "success": ""
}</pre>
### operation: Delete IP List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specifies the ID of the list that you want to delete
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": {
        "0": "",
        "id": ""
    },
    "success": ""
}</pre>
### operation: Create IP Items List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specifies the ID of the list from which you want to add or append as new items to the list.
</td></tr><tr><td>IP Address</td><td>Specifies a CSV list of IP addresses that you want to add or append as new items to the list.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": {
        "0": "",
        "operation_id": ""
    },
    "success": ""
}</pre>
### operation: Get IP List Items
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specifies the ID of the list from which you want to retrieve the list of IP addresses.
</td></tr><tr><td>Page Number</td><td>Specify the page number of paginated results
</td></tr><tr><td>Record Per Page</td><td>Specify this parameter to indicate the number of IP list item per page
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": [
        {
            "comment": "",
            "created_on": "",
            "id": "",
            "ip": "",
            "modified_on": ""
        }
    ],
    "success": "",
    "result_info": {
        "cursors": {
            "after": "",
            "before": ""
        }
    }
}</pre>
### operation: Update IP List Items
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specifies the ID of the list from which you want to update the list of IP addresses.
</td></tr><tr><td>IP Address</td><td>Specifies a CSV list of IP addresses that you want to update within the item list
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": {
        "0": "",
        "operation_id": ""
    },
    "success": ""
}</pre>
### operation: Delete IP List Items
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specifies the ID of the list from which you want to delete the IP list.
</td></tr><tr><td>Item ID</td><td>Specifies a CSV list of items ID that you want to delete from the list.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "errors": [],
    "messages": [],
    "result": {
        "0": "",
        "operation_id": ""
    },
    "success": ""
}</pre>
