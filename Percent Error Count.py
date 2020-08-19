"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'decision_1' block
    decision_1(container=container)

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_1() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        conditions=[
            ["Percent Error Count", "in", "artifact:*.name"],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        format_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    return

def SPLUNK_query(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('SPLUNK_query() called')

    # collect data for 'SPLUNK_query' call
    formatted_data_1 = phantom.get_format_data(name='format_1')

    parameters = []
    
    # build parameters list for 'SPLUNK_query' call
    parameters.append({
        'command': "search",
        'query': formatted_data_1,
        'display': "",
        'parse_only': "",
    })

    phantom.act(action="run query", parameters=parameters, assets=['splunk'], name="SPLUNK_query")

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """index=nginx host=\"{0}\" (status>=400 status<500) 
| top src_ip 
| iplocation src_ip"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.entity_title",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    SPLUNK_query(container=container)

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