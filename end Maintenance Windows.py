"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'format_2' block
    format_2(container=container)

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_data_1:action_result.data.*.response_body.data.*.data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    update_maintenance_window_1(container=container)

    return

def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_2() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message__icontains=\"Maintenance Windows\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    get_data_1(container=container)

    return

def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_1() called')

    # collect data for 'get_data_1' call
    formatted_data_1 = phantom.get_format_data(name='format_2')

    parameters = []
    
    # build parameters list for 'get_data_1' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=format_1, name="get_data_1")

    return

def add_episode_comment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_episode_comment_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    source_data_identifier_value = container.get('source_data_identifier', None)

    # collect data for 'add_episode_comment_1' call

    parameters = []
    
    # build parameters list for 'add_episode_comment_1' call
    parameters.append({
        'comment': "Phantom: maintenance window will end in 60 seconds",
        'itsi_group_id': source_data_identifier_value,
    })

    phantom.act(action="add episode comment", parameters=parameters, assets=['splunk itsi'], name="add_episode_comment_1", parent_action=action)

    return

def update_maintenance_window_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_maintenance_window_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'update_maintenance_window_1' call
    formatted_data_1 = phantom.get_format_data(name='format_1')

    parameters = []
    
    # build parameters list for 'update_maintenance_window_1' call
    parameters.append({
        'maintenance_window_id': formatted_data_1,
        'title': "",
        'relative_start_time': "",
        'relative_end_time': 60,
        'start_time': "",
        'end_time': "",
        'object_type': "",
        'object_ids': "",
        'comment': "Phantom: end maintenance window in 60 seconds",
    })

    phantom.act(action="update maintenance window", parameters=parameters, assets=['splunk itsi'], callback=add_episode_comment_1, name="update_maintenance_window_1")

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