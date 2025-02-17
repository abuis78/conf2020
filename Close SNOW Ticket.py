"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'decision_2' block
    decision_2(container=container)

    return

def Approval_Close_Incident(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Approval_Close_Incident() called')
    
    # set user and message variables for phantom.prompt call
    user = "Administrator"
    message = """The Episode {0} is resolved.
All steps are documented in the ticket: {1}

Please decide if the status of this Episode should be changed to: CLOSED"""

    # parameter list for template variable replacement
    parameters = [
        "container:name",
        "artifact:*.cef.snow_inc",
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

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=3, name="Approval_Close_Incident", parameters=parameters, response_types=response_types, callback=decision_1)

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_1() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["Approval_Close_Incident:action_result.summary.responses.0", "==", "Yes"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        SNOW_Close_ticket(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    SNOW_Do_Not_Close_Ticket(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def update_episode_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_episode_1() called')

    source_data_identifier_value = container.get('source_data_identifier', None)

    # collect data for 'update_episode_1' call

    parameters = []
    
    # build parameters list for 'update_episode_1' call
    parameters.append({
        'owner': "",
        'status': "Resolved",
        'severity': "Low",
        'itsi_group_id': source_data_identifier_value,
    })

    phantom.act(action="update episode", parameters=parameters, assets=['splunk itsi'], callback=break_episode_1, name="update_episode_1")

    return

def SNOW_Update_Resolved(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('SNOW_Update_Resolved() called')
    
    template = """{{\"close_code\":\"Solved Remotely (Work Around)\",\"state\":\"6\",\"caller_id\":\"phantom\",\"close_notes\":\"Phantom: resolved via API\", \"work_notes\": \"Service was started and ITSI episode status is been set to resolved\"}}"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.act",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="SNOW_Update_Resolved")

    format_4(container=container)

    return

def Update_SNOW_work_note_ITSI_resolved(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Update_SNOW_work_note_ITSI_resolved() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'Update_SNOW_work_note_ITSI_resolved' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_data_1:action_result.data.*.response_body.data.*.data', 'get_data_1:action_result.parameter.context.artifact_id'], action_results=results)
    formatted_data_1 = phantom.get_format_data(name='SNOW_Update_Resolved')

    parameters = []
    
    # build parameters list for 'Update_SNOW_work_note_ITSI_resolved' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'id': results_item_1[0],
                'table': "incident",
                'fields': formatted_data_1,
                'vault_id': "",
                'is_sys_id': True,
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="update ticket", parameters=parameters, assets=['servicenow'], callback=Approval_Close_Incident, name="Update_SNOW_work_note_ITSI_resolved", parent_action=action)

    return

def SNOW_Close_ticket(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('SNOW_Close_ticket() called')
    
    template = """{{\"work_notes\": \"Approval response: {0}. Ticket will be closed.\"}}"""

    # parameter list for template variable replacement
    parameters = [
        "Approval_Close_Incident:action_result.summary.responses.0",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="SNOW_Close_ticket")

    Update_SNOW_work_notes_ITSI_episode(container=container)

    return

def Update_SNOW_work_notes_ITSI_episode(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Update_SNOW_work_notes_ITSI_episode() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'Update_SNOW_work_notes_ITSI_episode' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_data_1:action_result.data.*.response_body.data.*.data', 'get_data_1:action_result.parameter.context.artifact_id'], action_results=results)
    formatted_data_1 = phantom.get_format_data(name='SNOW_Close_ticket')

    parameters = []
    
    # build parameters list for 'Update_SNOW_work_notes_ITSI_episode' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'id': results_item_1[0],
                'table': "incident",
                'fields': formatted_data_1,
                'vault_id': "",
                'is_sys_id': True,
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="update ticket", parameters=parameters, assets=['servicenow'], callback=format_5, name="Update_SNOW_work_notes_ITSI_episode")

    return

def SNOW_Do_Not_Close_Ticket(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('SNOW_Do_Not_Close_Ticket() called')
    
    template = """{{\"work_notes\": \"Approval response: {0}. Ticket will not be closed.\"}}"""

    # parameter list for template variable replacement
    parameters = [
        "Approval_Close_Incident:action_result.summary.responses.0",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="SNOW_Do_Not_Close_Ticket")

    update_ticket_3(container=container)

    return

def update_ticket_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_ticket_3() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'update_ticket_3' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_data_1:action_result.data.*.response_body.data.*.data', 'get_data_1:action_result.parameter.context.artifact_id'], action_results=results)
    formatted_data_1 = phantom.get_format_data(name='SNOW_Do_Not_Close_Ticket')

    parameters = []
    
    # build parameters list for 'update_ticket_3' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'id': results_item_1[0],
                'table': "incident",
                'fields': formatted_data_1,
                'vault_id': "",
                'is_sys_id': True,
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="update ticket", parameters=parameters, assets=['servicenow'], callback=join_set_status_set_severity_set_sensitivity_1, name="update_ticket_3")

    return

def format_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_4() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"snow_id\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_4")

    get_data_1(container=container)

    return

def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_data_1' call
    formatted_data_1 = phantom.get_format_data(name='format_4')

    parameters = []
    
    # build parameters list for 'get_data_1' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=Update_SNOW_work_note_ITSI_resolved, name="get_data_1")

    return

def Change_snow_ticket_status_closed(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Change_snow_ticket_status_closed() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'Change_snow_ticket_status_closed' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_data_1:action_result.data.*.response_body.data.*.data', 'get_data_1:action_result.parameter.context.artifact_id'], action_results=results)
    formatted_data_1 = phantom.get_format_data(name='format_5')

    parameters = []
    
    # build parameters list for 'Change_snow_ticket_status_closed' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'id': results_item_1[0],
                'table': "incident",
                'fields': formatted_data_1,
                'vault_id': "",
                'is_sys_id': True,
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="update ticket", parameters=parameters, assets=['servicenow'], callback=join_set_status_set_severity_set_sensitivity_1, name="Change_snow_ticket_status_closed")

    return

def format_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_5() called')
    
    template = """{{\"close_code\":\"Closed/Resolved By Caller\",\"state\":\"7\",\"caller_id\":\"phantom\",\"close_notes\":\"Phantom: closed by API\"}}"""

    # parameter list for template variable replacement
    parameters = [
        "Update_SNOW_work_notes_ITSI_episode:action_result.data.*.caller_id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_5")

    Change_snow_ticket_status_closed(container=container)

    return

def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_2() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        conditions=[
            ["service_restart_in_progress", "in", "artifact:*.tags"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        filter_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2

    return

def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('filter_1() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["service_restart_in_progress", "in", "artifact:*.tags"],
        ],
        name="filter_1:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        update_episode_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def set_status_set_severity_set_sensitivity_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('set_status_set_severity_set_sensitivity_1() called')

    phantom.set_status(container=container, status="Closed")

    phantom.set_severity(container=container, severity="Low")

    phantom.set_sensitivity(container=container, sensitivity="green")

    return

def join_set_status_set_severity_set_sensitivity_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('join_set_status_set_severity_set_sensitivity_1() called')
    
    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key='join_set_status_set_severity_set_sensitivity_1_called'):
        return

    # check if all connected incoming playbooks, actions, or custom functions are done i.e. have succeeded or failed
    if phantom.completed(action_names=['update_ticket_3']):
        
        # save the state that the joined function has now been called
        phantom.save_run_data(key='join_set_status_set_severity_set_sensitivity_1_called', value='set_status_set_severity_set_sensitivity_1')
        
        # call connected block "set_status_set_severity_set_sensitivity_1"
        set_status_set_severity_set_sensitivity_1(container=container, handle=handle)
    
    return

def break_episode_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('break_episode_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    source_data_identifier_value = container.get('source_data_identifier', None)

    # collect data for 'break_episode_1' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.itsi_policy_id', 'artifact:*.id'])

    parameters = []
    
    # build parameters list for 'break_episode_1' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'itsi_group_id': source_data_identifier_value,
                'itsi_policy_id': container_item[0],
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act(action="break episode", parameters=parameters, assets=['splunk itsi'], callback=SNOW_Update_Resolved, name="break_episode_1", parent_action=action)

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