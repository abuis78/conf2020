"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'Build_REST_call_for_entity_data' block
    Build_REST_call_for_entity_data(container=container)

    # call 'format_9' block
    format_9(container=container)

    return

def Build_REST_call_for_entity_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Build_REST_call_for_entity_data() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message__icontains=\"Entity\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Build_REST_call_for_entity_data")

    get_entity_pin(container=container)

    return

def get_entity_pin(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_entity_pin() called')

    # collect data for 'get_entity_pin' call
    formatted_data_1 = phantom.get_format_data(name='Build_REST_call_for_entity_data')

    parameters = []
    
    # build parameters list for 'get_entity_pin' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_3, name="get_entity_pin")

    return

def Format_Server_Address(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Format_Server_Address() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_entity_pin:action_result.data.*.parsed_response_body.data.*.data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Format_Server_Address")

    join_get_info_host_path(container=container)

    return

def restart_Service(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('restart_Service() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'restart_Service' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_entity_pin:action_result.data.*.parsed_response_body.data.*.data', 'get_entity_pin:action_result.parameter.context.artifact_id'], action_results=results)

    parameters = []
    
    # build parameters list for 'restart_Service' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'command': "sudo systemctl start nginx",
                'timeout': "",
                'ip_hostname': results_item_1[0],
                'script_file': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="execute program", parameters=parameters, assets=['ssh'], callback=add_tag_3, name="restart_Service", parent_action=action)

    return

def Cotent_for_Approval(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Cotent_for_Approval() called')
    
    template = """The Service on the Server needs to be started / restarted.
Server IP / Host:  {0}
Service Name: {1}"""

    # parameter list for template variable replacement
    parameters = [
        "Format_Server_Address:formatted_data",
        "Format_Service_Name:formatted_data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Cotent_for_Approval")

    decision_7(container=container)

    return

def Request_approval_restart_service(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Request_approval_restart_service() called')
    
    # set user and message variables for phantom.prompt call
    user = "admin"
    message = """Hi,
we have determined that the service: {1} (on the host: {2})- is not available. Details on the process can be found in the ticket . Please confirm as follows:

Yes = the service is automatically restarted
No = we will assign the incident to you and the service will NOT be restarted

Do not respond within 5 minutes - the service will automatically restart"""

    # parameter list for template variable replacement
    parameters = [
        "Cotent_for_Approval:formatted_data",
        "Format_Service_Name:formatted_data",
        "Format_Server_Address:formatted_data",
    ]

    #responses:
    response_types = [
        {
            "prompt": "",
            "options": {
                "type": "list",
                "choices": [
                    "Yes",
                    "No",
                ]
            },
        },
    ]

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=5, name="Request_approval_restart_service", parameters=parameters, response_types=response_types, callback=decision_2)

    return

def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_2() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["Request_approval_restart_service:action_result.summary.responses.0", "==", "Yes"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        cf_community_list_deduplicate_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    playbook_conf2020_add_Maintenance_Windows_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def SNOW_worknote_service_started(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('SNOW_worknote_service_started() called')
    
    template = """Service was started automatically:

{0}

{1}

----------- Approved by --------------
{2}"""

    # parameter list for template variable replacement
    parameters = [
        "Format_Server_Address:formatted_data",
        "restart_Service:action_result.message",
        "Request_approval_restart_service:action_result.parameter.message",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="SNOW_worknote_service_started")

    join_service_path(container=container)

    return

def SNOW_worknote_manual_task(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('SNOW_worknote_manual_task() called')
    
    template = """{0}

Server was started automaticaly"""

    # parameter list for template variable replacement
    parameters = [
        "Format_Server_Address:formatted_data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="SNOW_worknote_manual_task")

    format_13(container=container)

    return

def service_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('service_path() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'service_path' call

    parameters = []
    
    # build parameters list for 'service_path' call
    parameters.append({
        'sleep_seconds': 1,
    })

    phantom.act(action="no op", parameters=parameters, assets=['phantom'], callback=playbook_conf2020_end_Maintenance_Windows_1, name="service_path")

    return

def join_service_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('join_service_path() called')
    
    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key='join_service_path_called'):
        return

    # check if all connected incoming playbooks, actions, or custom functions are done i.e. have succeeded or failed
    if phantom.completed(action_names=['post_data_1', 'restart_Service']):
        
        # save the state that the joined function has now been called
        phantom.save_run_data(key='join_service_path_called', value='service_path')
        
        # call connected block "service_path"
        service_path(container=container, handle=handle)
    
    return

def format_snow_ticket_id_request(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_snow_ticket_id_request() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"snow inc\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_snow_ticket_id_request")

    get_snow_ticket(container=container)

    return

def get_snow_ticket(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_snow_ticket() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_snow_ticket' call
    formatted_data_1 = phantom.get_format_data(name='format_snow_ticket_id_request')

    parameters = []
    
    # build parameters list for 'get_snow_ticket' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=format_snow_worknote, name="get_snow_ticket")

    return

def format_snow_worknote(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_snow_worknote() called')
    
    template = """The Service: {0} has been started / restarted on host {1}"""

    # parameter list for template variable replacement
    parameters = [
        "Format_Service_Name:formatted_data",
        "Format_Server_Address:formatted_data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_snow_worknote")

    add_snow_work_note(container=container)

    return

def add_snow_work_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_snow_work_note() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'add_snow_work_note' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_snow_ticket:action_result.data.*.response_body.data.*.data', 'get_snow_ticket:action_result.parameter.context.artifact_id'], action_results=results)
    formatted_data_1 = phantom.get_format_data(name='format_snow_worknote')

    parameters = []
    
    # build parameters list for 'add_snow_work_note' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'id': results_item_1[0],
                'is_sys_id': False,
                'work_note': formatted_data_1,
                'table_name': "incident",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="add work note", parameters=parameters, assets=['servicenow'], callback=join_add_tag_5, name="add_snow_work_note")

    return

def format_9(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_9() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message__icontains=\"Service\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_9")

    get_service_pin(container=container)

    return

def get_service_pin(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_service_pin() called')

    # collect data for 'get_service_pin' call
    formatted_data_1 = phantom.get_format_data(name='format_9')

    parameters = []
    
    # build parameters list for 'get_service_pin' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_4, name="get_service_pin")

    return

def get_pin_info_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_pin_info_path() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_pin_info_path' call

    parameters = []
    
    # build parameters list for 'get_pin_info_path' call
    parameters.append({
        'sleep_seconds': 1,
    })

    phantom.act(action="no op", parameters=parameters, assets=['phantom'], callback=Cotent_for_Approval, name="get_pin_info_path")

    return

def join_get_pin_info_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('join_get_pin_info_path() called')

    # check if all connected incoming playbooks, actions, or custom functions are done i.e. have succeeded or failed
    if phantom.completed(action_names=['get_info_host_path', 'get_info_service_path']):
        
        # call connected block "get_pin_info_path"
        get_pin_info_path(container=container, handle=handle)
    
    return

def Format_Service_Name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Format_Service_Name() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_service_pin:action_result.data.*.response_body.data.*.data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Format_Service_Name")

    join_get_info_service_path(container=container)

    return

def decision_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_3() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["get_entity_pin:action_result.status", "==", "success"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        Format_Server_Address(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    join_get_info_host_path(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def decision_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_4() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["get_service_pin:action_result.status", "==", "success"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        Format_Service_Name(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    join_get_info_service_path(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def get_info_host_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_info_host_path() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_info_host_path' call

    parameters = []
    
    # build parameters list for 'get_info_host_path' call
    parameters.append({
        'sleep_seconds': 1,
    })

    phantom.act(action="no op", parameters=parameters, assets=['phantom'], callback=join_get_pin_info_path, name="get_info_host_path")

    return

def join_get_info_host_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('join_get_info_host_path() called')
    
    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key='join_get_info_host_path_called'):
        return

    # check if all connected incoming playbooks, actions, or custom functions are done i.e. have succeeded or failed
    if phantom.completed(action_names=['get_entity_pin']):
        
        # save the state that the joined function has now been called
        phantom.save_run_data(key='join_get_info_host_path_called', value='get_info_host_path')
        
        # call connected block "get_info_host_path"
        get_info_host_path(container=container, handle=handle)
    
    return

def get_info_service_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_info_service_path() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_info_service_path' call

    parameters = []
    
    # build parameters list for 'get_info_service_path' call
    parameters.append({
        'sleep_seconds': 1,
    })

    phantom.act(action="no op", parameters=parameters, assets=['phantom'], callback=join_get_pin_info_path, name="get_info_service_path")

    return

def join_get_info_service_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('join_get_info_service_path() called')

    # check if all connected incoming playbooks, actions, or custom functions are done i.e. have succeeded or failed
    if phantom.completed(action_names=['get_service_pin']):
        
        # call connected block "get_info_service_path"
        get_info_service_path(container=container, handle=handle)
    
    return

def decision_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_5() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["restart_Service:action_result.status", "==", "success"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        systemctl_is_service_active(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    join_service_path(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def systemctl_is_service_active(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('systemctl_is_service_active() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'systemctl_is_service_active' call
    results_data_1 = phantom.collect2(container=container, datapath=['restart_Service:action_result.parameter.ip_hostname', 'restart_Service:action_result.parameter.context.artifact_id'], action_results=results)

    parameters = []
    
    # build parameters list for 'systemctl_is_service_active' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'command': "sudo systemctl is-active nginx",
                'timeout': "",
                'ip_hostname': results_item_1[0],
                'script_file': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })
    # calculate start time using delay of 1 minutes
    start_time = datetime.now() + timedelta(minutes=1)

    phantom.act(action="execute program", parameters=parameters, assets=['ssh'], callback=decision_8, start_time=start_time, name="systemctl_is_service_active")

    return

def decision_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_6() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["systemctl_is_service_active:action_result.data.*.output", "==", "active"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        Change_Pin_to_blue(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    join_service_path(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def post_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('post_data_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'post_data_1' call
    formatted_data_1 = phantom.get_format_data(name='Change_Pin_to_blue')
    formatted_data_2 = phantom.get_format_data(name='build_rest_call_url_1')

    parameters = []
    
    # build parameters list for 'post_data_1' call
    parameters.append({
        'body': formatted_data_1,
        'headers': "",
        'location': formatted_data_2,
        'verify_certificate': False,
    })

    phantom.act(action="post data", parameters=parameters, assets=['http'], callback=SNOW_worknote_service_started, name="post_data_1")

    return

def Change_Pin_to_blue(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Change_Pin_to_blue() called')
    
    template = """{{
\"pin_style\": \"blue\"
}}"""

    # parameter list for template variable replacement
    parameters = [
        "get_entity_pin:action_result.data.*.response_body.data.*.id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Change_Pin_to_blue")

    build_rest_call_url_1(container=container)

    return

def add_tag_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_tag_3() called')

    phantom.add_tags(container=container, tags="service_restart_in_progress")
    decision_5(container=container)

    return

def decision_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_7() called')
    
    tags_value = container.get('tags', None)
    tags_value = container.get('tags', None)

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["service_restart_in_progress", "in", tags_value],
            ["itsi_service_restart_successful", "in", tags_value],
        ],
        logical_operator='or')

    # call connected blocks if condition 1 matched
    if matched:
        join_add_tag_5(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    format_15(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def execute_program_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('execute_program_3() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'execute_program_3' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_entity_pin:action_result.data.*.parsed_response_body.data.*.data', 'get_entity_pin:action_result.parameter.context.artifact_id'], action_results=results)

    parameters = []
    
    # build parameters list for 'execute_program_3' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'command': "sudo systemctl start nginx",
                'timeout': 10,
                'ip_hostname': results_item_1[0],
                'script_file': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="execute program", parameters=parameters, assets=['ssh'], callback=add_tag_4, name="execute_program_3")

    return

def build_rest_call_url_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('build_rest_call_url_1() called')
    
    template = """/rest/container_pin/{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_service_pin:action_result.data.*.parsed_response_body.data.*.id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="build_rest_call_url_1")

    post_data_1(container=container)

    return

def format_13(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_13() called')
    
    template = """{{
\"pin_style\": \"blue\"
}}"""

    # parameter list for template variable replacement
    parameters = [
        "SNOW_worknote_manual_task:formatted_data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_13")

    format_14(container=container)

    return

def format_14(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_14() called')
    
    template = """/rest/container_pin/{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_service_pin:action_result.data.*.parsed_response_body.data.*.id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_14")

    post_data_2(container=container)

    return

def post_data_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('post_data_2() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'post_data_2' call
    formatted_data_1 = phantom.get_format_data(name='format_13')
    formatted_data_2 = phantom.get_format_data(name='format_14')

    parameters = []
    
    # build parameters list for 'post_data_2' call
    parameters.append({
        'body': formatted_data_1,
        'headers': "",
        'location': formatted_data_2,
        'verify_certificate': False,
    })

    phantom.act(action="post data", parameters=parameters, assets=['http'], callback=join_service_path, name="post_data_2")

    return

def add_tag_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_tag_4() called')

    phantom.add_tags(container=container, tags="service_restart_in_progress")
    SNOW_worknote_manual_task(container=container)

    return

def decision_8(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_8() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["systemctl_is_service_active:action_result.status", "!=", "failed"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        decision_6(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    join_service_path(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def format_15(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_15() called')
    
    template = """/rest/artifact?_filter_container={0}&_filter_type=\"notable\"&_filter_tags__icontains=\"service_restart_in_progress\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_15")

    add_tag_service_restart_in_progress(container=container)

    return

def add_tag_service_restart_in_progress(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_tag_service_restart_in_progress() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'add_tag_service_restart_in_progress' call
    formatted_data_1 = phantom.get_format_data(name='format_15')

    parameters = []
    
    # build parameters list for 'add_tag_service_restart_in_progress' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_10, name="add_tag_service_restart_in_progress")

    return

def decision_10(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_10() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["add_tag_service_restart_in_progress:action_result.data.*.response_body.count", ">=", 1],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        join_add_tag_5(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    update_artifact_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def update_artifact_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_artifact_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'update_artifact_1' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.id', 'artifact:*.id'])

    parameters = []
    
    # build parameters list for 'update_artifact_1' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'data': "{ \"tags\": \"service_restart_in_progress \" }",
                'overwrite': True,
                'artifact_id': container_item[0],
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act(action="update artifact", parameters=parameters, assets=['phantom utilities'], callback=Request_approval_restart_service, name="update_artifact_1")

    return

def add_tag_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_tag_5() called')

    phantom.add_tags(container=container, tags="itsi_service_restart_successful")
    remove_tag_6(container=container)

    return

def join_add_tag_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('join_add_tag_5() called')
    
    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key='join_add_tag_5_called'):
        return

    # check if all connected incoming playbooks, actions, or custom functions are done i.e. have succeeded or failed
    if phantom.completed(action_names=['add_tag_service_restart_in_progress', 'get_pin_info_path']):
        
        # save the state that the joined function has now been called
        phantom.save_run_data(key='join_add_tag_5_called', value='add_tag_5')
        
        # call connected block "add_tag_5"
        add_tag_5(container=container, handle=handle)
    
    return

def remove_tag_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('remove_tag_6() called')

    phantom.remove_tags(container=container, tags="itsi_in_progress")

    return

def format_16(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_16() called')
    
    template = """I got approval from: {0} and restart the service / entity:  {1}."""

    # parameter list for template variable replacement
    parameters = [
        "Request_approval_restart_service:action_result.parameter.message",
        "Format_Server_Address:formatted_data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_16")

    add_work_note_2(container=container)

    return

def add_work_note_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_work_note_2() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'add_work_note_2' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_data_5:action_result.data.*.response_body.data.*.data', 'get_data_5:action_result.parameter.context.artifact_id'], action_results=results)
    formatted_data_1 = phantom.get_format_data(name='format_16')

    parameters = []
    
    # build parameters list for 'add_work_note_2' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'table_name': "incident",
                'id': results_item_1[0],
                'work_note': formatted_data_1,
                'is_sys_id': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="add work note", parameters=parameters, assets=['servicenow'], callback=restart_Service, name="add_work_note_2")

    return

def format_17(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_17() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"snow inc\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_17")

    get_data_5(container=container)

    return

def get_data_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_5() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_data_5' call
    formatted_data_1 = phantom.get_format_data(name='format_17')

    parameters = []
    
    # build parameters list for 'get_data_5' call
    parameters.append({
        'location': formatted_data_1,
        'verify_certificate': False,
        'headers': "",
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=format_16, name="get_data_5")

    return

def playbook_conf2020_add_Maintenance_Windows_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_add_Maintenance_Windows_2() called')
    
    # call playbook "conf2020/add Maintenance Windows", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/add Maintenance Windows", container=container, name="playbook_conf2020_add_Maintenance_Windows_2", callback=execute_program_3)

    return

def playbook_conf2020_end_Maintenance_Windows_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_end_Maintenance_Windows_1() called')
    
    # call playbook "conf2020/end Maintenance Windows", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/end Maintenance Windows", container=container, name="playbook_conf2020_end_Maintenance_Windows_1", callback=format_snow_ticket_id_request)

    return

def cf_community_list_deduplicate_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('cf_community_list_deduplicate_1() called')
    
    container_data_0 = phantom.collect2(container=container, datapath=['artifact:*.cef.entity_key', 'artifact:*.id'])

    parameters = []

    container_data_0_0 = [item[0] for item in container_data_0]

    parameters.append({
        'input_list': container_data_0_0,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "community/list_deduplicate", returns the custom_function_run_id
    phantom.custom_function(custom_function='community/list_deduplicate', parameters=parameters, name='cf_community_list_deduplicate_1', callback=format_18)

    return

def format_18(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_18() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "cf_community_list_deduplicate_1:custom_function_result.data.*.item",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_18")

    format_19(container=container)

    return

def format_19(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_19() called')
    
    template = """Maintenance Windows - Affected entity ID {0}"""

    # parameter list for template variable replacement
    parameters = [
        "cf_community_list_deduplicate_1:custom_function_result.data.*.item",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_19")

    add_maintenance_window_1(container=container)

    return

def add_maintenance_window_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_maintenance_window_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'add_maintenance_window_1' call
    formatted_data_1 = phantom.get_format_data(name='format_19')
    formatted_data_2 = phantom.get_format_data(name='format_18')

    parameters = []
    
    # build parameters list for 'add_maintenance_window_1' call
    parameters.append({
        'title': formatted_data_1,
        'relative_start_time': "",
        'relative_end_time': 300,
        'start_time': "",
        'end_time': "",
        'object_type': "entity",
        'object_ids': formatted_data_2,
        'comment': "Phantom hast started Maintenance Windows",
    })

    phantom.act(action="add maintenance window", parameters=parameters, assets=['splunk itsi'], callback=format_20, name="add_maintenance_window_1")

    return

def format_20(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_20() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "add_maintenance_window_1:action_result.data.*._key",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_20")

    format_21(container=container)

    return

def format_21(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_21() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "add_maintenance_window_1:action_result.parameter.title",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_21")

    pin_7(container=container)

    return

def pin_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('pin_7() called')

    formatted_data_1 = phantom.get_format_data(name='format_21')
    formatted_data_2 = phantom.get_format_data(name='format_20')

    phantom.pin(container=container, data=formatted_data_2, message=formatted_data_1, name=None)
    format_22(container=container)

    return

def add_episode_comment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_episode_comment_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    source_data_identifier_value = container.get('source_data_identifier', None)

    # collect data for 'add_episode_comment_1' call

    parameters = []
    
    # build parameters list for 'add_episode_comment_1' call
    parameters.append({
        'itsi_group_id': source_data_identifier_value,
        'comment': "",
    })

    phantom.act(action="add episode comment", parameters=parameters, assets=['splunk itsi'], callback=format_17, name="add_episode_comment_1")

    return

def format_22(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_22() called')
    
    template = """Maintenance Windows has been started: {0}"""

    # parameter list for template variable replacement
    parameters = [
        "add_maintenance_window_1:action_result.parameter.title",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_22")

    add_episode_comment_1(container=container)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return