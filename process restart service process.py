"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'Check_entity_HUD' block
    Check_entity_HUD(container=container)

    return

def Check_entity_HUD(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Check_entity_HUD() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message__icontains=\"Entity\"&_filter_pin_style=\"grey\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Check_entity_HUD")

    get_entity_data(container=container)

    return

def get_entity_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_entity_data() called')

    # collect data for 'get_entity_data' call
    formatted_data_1 = phantom.get_format_data(name='Check_entity_HUD')

    parameters = []
    
    # build parameters list for 'get_entity_data' call
    parameters.append({
        'location': formatted_data_1,
        'verify_certificate': False,
        'headers': "",
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=check_service_HUD, name="get_entity_data")

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_1() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["get_entity_data:action_result.data.*.response_body.count", ">", 0],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        prompt_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    add_comment_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def add_comment_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_2() called')

    phantom.comment(container=container, comment="nein")

    return

def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('prompt_1() called')
    
    # set user and message variables for phantom.prompt call
    user = "admin"
    message = """Hi,
we have determined that the service: {0} (on the host: {1})- is not available. Details on the process can be found in the ticket . Please confirm as follows:

Yes = the service is automatically restarted
No = we will assign the incident to you and the service will NOT be restarted

Do not respond within 5 minutes - the service will automatically restart"""

    # parameter list for template variable replacement
    parameters = [
        "get_service_data:action_result.data.*.response_body.data.*.data",
        "get_entity_data:action_result.data.*.parsed_response_body.data.*.data",
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

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=2, name="prompt_1", parameters=parameters, response_types=response_types, callback=decision_3)

    return

def check_service_HUD(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('check_service_HUD() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message__icontains=\"Service\"&_filter_pin_style=\"red\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="check_service_HUD")

    get_service_data(container=container)

    return

def get_service_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_service_data() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_service_data' call
    formatted_data_1 = phantom.get_format_data(name='check_service_HUD')

    parameters = []
    
    # build parameters list for 'get_service_data' call
    parameters.append({
        'location': formatted_data_1,
        'verify_certificate': False,
        'headers': "",
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_1, name="get_service_data")

    return

def decision_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_3() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["prompt_1:action_result.summary.responses.0", "==", "Yes"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        playbook_conf2020_add_Maintenance_Windows_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # check for 'elif' condition 2
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["prompt_1:action_result.summary.responses.0", "==", "No"],
        ])

    # call connected blocks if condition 2 matched
    if matched:
        return

    return

def playbook_conf2020_add_Maintenance_Windows_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_add_Maintenance_Windows_1() called')
    
    # call playbook "conf2020/add Maintenance Windows", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/add Maintenance Windows", container=container, name="playbook_conf2020_add_Maintenance_Windows_1", callback=restart_service)

    return

def restart_service(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('restart_service() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'restart_service' call
    results_data_1 = phantom.collect2(container=container, datapath=['get_entity_data:action_result.data.*.parsed_response_body.data.*.data', 'get_entity_data:action_result.parameter.context.artifact_id'], action_results=results)

    parameters = []
    
    # build parameters list for 'restart_service' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'ip_hostname': results_item_1[0],
                'command': "sudo systemctl start nginx",
                'script_file': "",
                'timeout': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="execute program", parameters=parameters, assets=['ssh'], callback=decision_4, name="restart_service")

    return

def decision_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_4() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["restart_service:action_result.status", "==", "success"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        execute_program_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    return

def execute_program_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('execute_program_2() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'execute_program_2' call
    results_data_1 = phantom.collect2(container=container, datapath=['restart_service:action_result.parameter.ip_hostname', 'restart_service:action_result.parameter.context.artifact_id'], action_results=results)

    parameters = []
    
    # build parameters list for 'execute_program_2' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'ip_hostname': results_item_1[0],
                'command': "sudo systemctl is-active nginx",
                'script_file': "",
                'timeout': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })
    # calculate start time using delay of 1 minutes
    start_time = datetime.now() + timedelta(minutes=1)

    phantom.act(action="execute program", parameters=parameters, assets=['ssh'], callback=decision_5, start_time=start_time, name="execute_program_2")

    return

def decision_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_5() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["execute_program_2:action_result.status", "==", "success"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        playbook_conf2020_end_Maintenance_Windows_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    return

def playbook_conf2020_end_Maintenance_Windows_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_end_Maintenance_Windows_1() called')
    
    # call playbook "conf2020/end Maintenance Windows", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/end Maintenance Windows", container=container, name="playbook_conf2020_end_Maintenance_Windows_1")

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