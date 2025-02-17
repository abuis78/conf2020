"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'format_1' block
    format_1(container=container)

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """ITSI Alert: {0}"""

    # parameter list for template variable replacement
    parameters = [
        "container:source_data_identifier",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    format_2(container=container)

    return

def update_incident_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_incident_1() called')

    # collect data for 'update_incident_1' call
    formatted_data_1 = phantom.get_format_data(name='format_1')
    formatted_data_2 = phantom.get_format_data(name='format_2')

    parameters = []
    
    # build parameters list for 'update_incident_1' call
    parameters.append({
        'routing_key': "",
        'message_type': "INFO",
        'entity_id': formatted_data_1,
        'entity_display_name': "",
        'state_message': formatted_data_2,
    })

    phantom.act(action="update incident", parameters=parameters, assets=['victorops'], name="update_incident_1")

    return

def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_2() called')
    
    template = """Die Container ID {0}"""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    update_incident_1(container=container)

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