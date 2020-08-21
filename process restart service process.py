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
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message__icontains=\"Entity\""""

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

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_1, name="get_entity_data")

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_1() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["get_entity_data:action_result.data.*.response_body.count", ">", 0],
            ["action_result.data.*.response_body.data.*.pin_style", "==", "grey"],
        ],
        logical_operator='and')

    # call connected blocks if condition 1 matched
    if matched:
        add_comment_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    add_comment_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def add_comment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_1() called')

    phantom.comment(container=container, comment="ja")

    return

def add_comment_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_2() called')

    phantom.comment(container=container, comment="nein")

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