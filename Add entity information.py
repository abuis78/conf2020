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

def pin_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('pin_1() called')

    results_data_1 = phantom.collect2(container=container, datapath=['get_entity_1:action_result.data.*.*.title', 'get_entity_1:action_result.data.*.*.ip.0'], action_results=results)

    for item in results_data_1:
        results_item_1_0 = item[0]
        results_item_1_1 = item[1]

        phantom.pin(container=container, data=results_item_1_1, message=results_item_1_0, pin_type="card", pin_style="grey", name=None)

    return

def Get_PIN(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Get_PIN() called')

    # collect data for 'Get_PIN' call
    formatted_data_1 = phantom.get_format_data(name='Create_URL_Parameters')

    parameters = []
    
    # build parameters list for 'Get_PIN' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_1, name="Get_PIN")

    return

def Create_URL_Parameters(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Create_URL_Parameters() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"{1}\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
        "DedupeListEntries:custom_function:entity_list",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Create_URL_Parameters")

    Get_PIN(container=container)
    add_comment_3(container=container)

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_1() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["Get_PIN:action_result.data.*.response_body.count", "==", 0],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        get_entity_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    return

def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_2() called')

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
        DedupeListEntries(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    return

def DedupeListEntries(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('DedupeListEntries() called')
    
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.entity_title', 'artifact:*.id'])
    container_item_0 = [item[0] for item in container_data]

    DedupeListEntries__entity_list = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug('DedupeListEntries() formatted_data_1: {}'.format(container_item_0))

    seen = {}
    DedupeListEntries__entity_list = [seen.setdefault(x, x) for x in container_item_0 if x not in seen]
    
    phantom.debug('DedupeListEntries() DedupeListEntries__entity_list: {}'.format(DedupeListEntries__entity_list))

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key='DedupeListEntries:entity_list', value=json.dumps(DedupeListEntries__entity_list))
    Create_URL_Parameters(container=container)
    add_comment_2(container=container)

    return

def get_entity_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_entity_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    DedupeListEntries__entity_list = json.loads(phantom.get_run_data(key='DedupeListEntries:entity_list'))
    # collect data for 'get_entity_1' call

    parameters = []
    
    # build parameters list for 'get_entity_1' call
    for entity_title in DedupeListEntries__entity_list:
        parameters.append({
            'entity_title': entity_title,
        })
    phantom.act(action="get entity", parameters=parameters, assets=['splunk itsi'], callback=pin_1, name="get_entity_1")

    return

def add_comment_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_2() called')

    DedupeListEntries__entity_list = json.loads(phantom.get_run_data(key='DedupeListEntries:entity_list'))

    phantom.comment(container=container, comment=DedupeListEntries__entity_list)

    return

def add_comment_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_3() called')

    formatted_data_1 = phantom.get_format_data(name='Create_URL_Parameters')

    phantom.comment(container=container, comment=formatted_data_1)

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