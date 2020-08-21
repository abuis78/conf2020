"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'Build_REST_call_for_entity_data' block
    Build_REST_call_for_entity_data(container=container)

    # call 'Build_rest_call_get_Service' block
    Build_rest_call_get_Service(container=container)

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

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=get_SNOW_ticket_ID, name="get_entity_pin")

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

def Request_approval_restart_service(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Request_approval_restart_service() called')
    
    # set user and message variables for phantom.prompt call
    user = "admin"
    message = """Hi,
we have determined that the service:  (on the host: )- is not available. Details on the process can be found in the ticket . Please confirm as follows:

Yes = the service is automatically restarted
No = we will assign the incident to you and the service will NOT be restarted

Do not respond within 5 minutes - the service will automatically restart"""

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

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=5, name="Request_approval_restart_service", response_types=response_types, callback=decision_2)

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
        update_artifact_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # check for 'elif' condition 2
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["Request_approval_restart_service:action_result.summary.responses.0", "==", "No"],
        ])

    # call connected blocks if condition 2 matched
    if matched:
        Request_was_denied(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 3
    add_comment_9(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def SNOW_worknote_service_started(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('SNOW_worknote_service_started() called')
    
    template = """Service was started automatically:

{0}

{1}

----------- Approved by --------------"""

    # parameter list for template variable replacement
    parameters = [
        "restart_Service:action_result.message",
        "Request_approval_restart_service:action_result.parameter.message",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="SNOW_worknote_service_started")

    join_service_path(container=container)

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

    phantom.act(action="no op", parameters=parameters, assets=['phantom'], callback=playbook_conf2020_conf2020_end_Maintenance_Windows_1, name="service_path")

    return

def join_service_path(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('join_service_path() called')
    
    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key='join_service_path_called'):
        return

    # no callbacks to check, call connected block "service_path"
    phantom.save_run_data(key='join_service_path_called', value='service_path', auto=True)

    service_path(container=container, handle=handle)
    
    return

def format_snow_worknote(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_snow_worknote() called')
    
    template = """The Service: {0} has been started / restarted on host"""

    # parameter list for template variable replacement
    parameters = [
        "get_entity_pin:action_result.data.*.location",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_snow_worknote")

    add_snow_work_note(container=container)

    return

def add_snow_work_note(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_snow_work_note() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'add_snow_work_note' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_data_5:action_result.data.*.response_body.data.*.data', 'get_data_5:action_result.parameter.context.artifact_id'], action_results=results)
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

    phantom.act(action="add work note", parameters=parameters, assets=['servicenow'], callback=add_tag_5, name="add_snow_work_note")

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
        Change_Pin_to_blue(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    join_service_path(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def add_tag_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_tag_5() called')

    phantom.add_tags(container=container, tags="itsi_service_restart_successful")
    remove_tag_6(container=container)

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
        "cf_community_list_deduplicate_2:custom_function_result.data.*.item",
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
                'id': results_item_1[0],
                'is_sys_id': "",
                'work_note': formatted_data_1,
                'table_name': "incident",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="add work note", parameters=parameters, assets=['servicenow'], callback=playbook_conf2020_add_Maintenance_Windows_3, name="add_work_note_2")

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
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=format_16, name="get_data_5")

    return

def playbook_conf2020_conf2020_end_Maintenance_Windows_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_end_Maintenance_Windows_1() called')
    
    # call playbook "conf2020/end Maintenance Windows", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/end Maintenance Windows", container=container, name="playbook_conf2020_conf2020_end_Maintenance_Windows_1", callback=format_snow_worknote)

    return

def cf_community_list_deduplicate_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('cf_community_list_deduplicate_2() called')
    
    action_results_data_0 = phantom.collect2(container=container, datapath=['get_entity_pin:action_result.data.*.parsed_response_body.data.*.data', 'get_entity_pin:action_result.parameter.context.artifact_id'], action_results=results )

    parameters = []

    action_results_data_0_0 = [item[0] for item in action_results_data_0]

    parameters.append({
        'input_list': action_results_data_0_0,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "community/list_deduplicate", returns the custom_function_run_id
    phantom.custom_function(custom_function='community/list_deduplicate', parameters=parameters, name='cf_community_list_deduplicate_2', callback=Request_approval_restart_service)

    return

def playbook_conf2020_add_Maintenance_Windows_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_add_Maintenance_Windows_3() called')
    
    # call playbook "conf2020/add Maintenance Windows", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/add Maintenance Windows", container=container, name="playbook_conf2020_add_Maintenance_Windows_3", callback=restart_Service)

    return

def Request_was_denied(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Request_was_denied() called')

    phantom.comment(container=container, comment="Approver: Request was denied")
    add_work_note_3(container=container)

    return

def add_work_note_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_work_note_3() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'add_work_note_3' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_data_6:action_result.data.*.response_body.data.*.data', 'get_data_6:action_result.parameter.context.artifact_id'], action_results=results)

    parameters = []
    
    # build parameters list for 'add_work_note_3' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'table_name': "incident",
                'id': results_item_1[0],
                'work_note': "",
                'is_sys_id': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="add work note", parameters=parameters, assets=['servicenow'], name="add_work_note_3", parent_action=action)

    return

def add_comment_9(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_9() called')

    phantom.comment(container=container, comment="Approver request timeout")
    add_work_note_4(container=container)

    return

def get_SNOW_ticket_ID(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_SNOW_ticket_ID() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"snow inc\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="get_SNOW_ticket_ID")

    SNOW_Ticket_ID(container=container)

    return

def SNOW_Ticket_ID(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('SNOW_Ticket_ID() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'SNOW_Ticket_ID' call
    formatted_data_1 = phantom.get_format_data(name='get_SNOW_ticket_ID')

    parameters = []
    
    # build parameters list for 'SNOW_Ticket_ID' call
    parameters.append({
        'location': formatted_data_1,
        'verify_certificate': False,
        'headers': "",
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=join_get_container_information, name="SNOW_Ticket_ID")

    return

def add_work_note_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_work_note_4() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'add_work_note_4' call

    parameters = []
    
    # build parameters list for 'add_work_note_4' call
    parameters.append({
        'table_name': "incident",
        'id': "SNOW_Ticket_ID:/rest/container_pin?_filter_container={0}&_filter_message=\"snow inc\"",
        'work_note': "",
        'is_sys_id': "",
    })

    phantom.act(action="add work note", parameters=parameters, assets=['servicenow'], name="add_work_note_4")

    return

def Build_rest_call_get_Service(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Build_rest_call_get_Service() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message__icontains=\"Service\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Build_rest_call_get_Service")

    get_service_pin(container=container)

    return

def get_service_pin(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_service_pin() called')

    # collect data for 'get_service_pin' call
    formatted_data_1 = phantom.get_format_data(name='Build_rest_call_get_Service')

    parameters = []
    
    # build parameters list for 'get_service_pin' call
    parameters.append({
        'location': formatted_data_1,
        'verify_certificate': False,
        'headers': "",
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=join_get_container_information, name="get_service_pin")

    return

def get_container_information(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_container_information() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_container_information' call

    parameters = []
    
    # build parameters list for 'get_container_information' call
    parameters.append({
        'sleep_seconds': 1,
    })

    phantom.act(action="no op", parameters=parameters, assets=['phantom'], callback=decision_11, name="get_container_information", parent_action=action)

    return

def join_get_container_information(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('join_get_container_information() called')

    # check if all connected incoming playbooks, actions, or custom functions are done i.e. have succeeded or failed
    if phantom.completed(action_names=['get_service_pin', 'SNOW_Ticket_ID']):
        
        # call connected block "get_container_information"
        get_container_information(container=container, handle=handle)
    
    return

def update_artifact_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_artifact_2() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'update_artifact_2' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.id', 'artifact:*.id'])

    parameters = []
    
    # build parameters list for 'update_artifact_2' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'data': "{ \"tags\": \"service_restart_in_progress \" }",
                'overwrite': True,
                'artifact_id': container_item[0],
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act(action="update artifact", parameters=parameters, assets=['phantom utilities'], callback=format_17, name="update_artifact_2")

    return

def decision_11(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_11() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["service_restart_in_progress", "not in", "artifact:*.tags"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        cf_community_list_deduplicate_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

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