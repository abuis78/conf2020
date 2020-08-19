"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'cf_community_list_deduplicate_1' block
    cf_community_list_deduplicate_1(container=container)

    return

def playbook_conf2020_conf2020_Add_SNOW_Information_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Add_SNOW_Information_1() called')
    
    # call playbook "conf2020/Add SNOW Information", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Add SNOW Information", container=container, name="playbook_conf2020_conf2020_Add_SNOW_Information_1", callback=playbook_conf2020_conf2020_Add_entity_information_1)

    return

def playbook_conf2020_conf2020_Notable_clean_up_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Notable_clean_up_1() called')
    
    # call playbook "conf2020/Notable_clean_up", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Notable_clean_up", container=container, name="playbook_conf2020_conf2020_Notable_clean_up_1", callback=playbook_conf2020_conf2020_Add_SNOW_Information_1)

    return

def playbook_conf2020_conf2020_Add_entity_information_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Add_entity_information_1() called')
    
    # call playbook "conf2020/Add entity information", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Add entity information", container=container, name="playbook_conf2020_conf2020_Add_entity_information_1", callback=playbook_conf2020_conf2020_Get_Service_information_1)

    return

def playbook_conf2020_conf2020_Get_Service_information_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Get_Service_information_1() called')
    
    # call playbook "conf2020/Get Service information", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Get Service information", container=container, name="playbook_conf2020_conf2020_Get_Service_information_1", callback=playbook_conf2020_conf2020_Restart_Service_1)

    return

def playbook_conf2020_conf2020_Restart_Service_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Restart_Service_1() called')
    
    # call playbook "conf2020/Restart Service", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Restart Service", container=container, name="playbook_conf2020_conf2020_Restart_Service_1", callback=playbook_conf2020_conf2020_Close_SNOW_Ticket_1)

    return

def playbook_conf2020_conf2020_Close_SNOW_Ticket_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Close_SNOW_Ticket_1() called')
    
    # call playbook "conf2020/Close SNOW Ticket", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Close SNOW Ticket", container=container, name="playbook_conf2020_conf2020_Close_SNOW_Ticket_1")

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_1() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        conditions=[
            ["artifact:*.cef.entity_title", "!=", ""],
            ["artifact:*.cef.entity_key", "!=", ""],
        ],
        logical_operator='and')

    # call connected blocks if condition 1 matched
    if matched:
        rest_request_for_enity_check(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    return

def rest_request_for_enity_check(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('rest_request_for_enity_check() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"Entity: {1}\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
        "artifact:*.cef.entity_title",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="rest_request_for_enity_check")

    get_data_1(container=container)

    return

def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_1() called')

    # collect data for 'get_data_1' call
    formatted_data_1 = phantom.get_format_data(name='rest_request_for_enity_check')

    parameters = []
    
    # build parameters list for 'get_data_1' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_2, name="get_data_1")

    return

def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_2() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["get_data_1:action_result.data.*.response_body.count", "==", 0],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        return

    # call connected blocks for 'else' condition 2
    add_comment_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def add_comment_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_2() called')

    phantom.comment(container=container, comment="nothing")

    return

def cf_community_list_deduplicate_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('cf_community_list_deduplicate_1() called')
    
    container_data_0 = phantom.collect2(container=container, datapath=['artifact:*.cef.entity_title', 'artifact:*.id'])

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
    phantom.custom_function(custom_function='community/list_deduplicate', parameters=parameters, name='cf_community_list_deduplicate_1', callback=decision_3)

    return

def decision_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_3() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["cf_community_list_deduplicate_1:custom_function_result.data.*.item", "!=", ""],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        playbook_conf2020_conf2020_Notable_clean_up_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
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