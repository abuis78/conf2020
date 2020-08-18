"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'decision_5' block
    decision_5(container=container)

    return

def decision_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_5() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        conditions=[
            ["artifact:*.cef.entity_key", "!=", ""],
            ["artifact:*.cef.entity_title", "!=", ""],
        ],
        logical_operator='and')

    # call connected blocks if condition 1 matched
    if matched:
        DedupeListEntries(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    return

"""
Removes duplicates from list and keeps list order
"""
def DedupeListEntries(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('DedupeListEntries() called')
    
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.entity_title', 'artifact:*.id'])
    container_item_0 = [item[0] for item in container_data]

    DedupeListEntries__new_list = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug('DedupeListEntries() formatted_data_1: {}'.format(container_item_0))

    seen = {}
    DedupeListEntries__new_list = [seen.setdefault(x, x) for x in container_item_0 if x not in seen]
    phantom.debug('DedupeListEntries() DedupeListEntries__new_list: {}'.format(DedupeListEntries__new_list))

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key='DedupeListEntries:new_list', value=json.dumps(DedupeListEntries__new_list))
    format_1(container=container)

    return

def get_entity_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_entity_2() called')

    DedupeListEntries__new_list = json.loads(phantom.get_run_data(key='DedupeListEntries:new_list'))
    # collect data for 'get_entity_2' call

    parameters = []
    
    # build parameters list for 'get_entity_2' call
    for entity_title in DedupeListEntries__new_list:
        parameters.append({
            'entity_title': entity_title,
        })

    phantom.act("get entity", parameters=parameters, assets=['splunk itsi'], callback=pin_6, name="get_entity_2")

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"Entity: {1}\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
        "DedupeListEntries:custom_function:new_list",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    get_data_1(container=container)

    return

def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_1() called')

    # collect data for 'get_data_1' call
    formatted_data_1 = phantom.get_format_data(name='format_1')

    parameters = []
    
    # build parameters list for 'get_data_1' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_6, name="get_data_1")

    return

def decision_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_6() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["get_data_1:action_result.data.*.response_body.count", "==", 0],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        get_entity_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    add_comment_3(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def add_comment_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_3() called')

    phantom.comment(container=container, comment="Eintrag vorhanden")

    return

def pin_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('pin_6() called')

    results_data_1 = phantom.collect2(container=container, datapath=['get_entity_2:action_result.parameter.entity_title', 'get_entity_2:action_result.data.*.*.ip.0'], action_results=results)

    for item in results_data_1:
        results_item_1_0 = "Entity: "+item[0]
        results_item_1_1 = item[1]

        phantom.pin(container=container, data=results_item_1_1, message=results_item_1_0, pin_type="card", pin_style="grey", name=None)

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