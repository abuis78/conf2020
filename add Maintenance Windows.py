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

def add_maintenance_window_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_maintenance_window_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'add_maintenance_window_1' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.entity_key', 'artifact:*.id'])
    formatted_data_1 = phantom.get_format_data(name='format_1')

    parameters = []
    
    # build parameters list for 'add_maintenance_window_1' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'title': formatted_data_1,
                'comment': "Phantom hast started Maintenance Windows",
                'end_time': "",
                'object_ids': container_item[0],
                'start_time': "",
                'object_type': "entity",
                'relative_end_time': 300,
                'relative_start_time': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act(action="add maintenance window", parameters=parameters, assets=['splunk itsi'], callback=pin_1, name="add_maintenance_window_1")

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """Maintenance Windows for entity {0}"""

    # parameter list for template variable replacement
    parameters = [
        "cf_community_list_deduplicate_1:custom_function_result.data.*.item",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    add_maintenance_window_1(container=container)

    return

def pin_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('pin_1() called')

    results_data_1 = phantom.collect2(container=container, datapath=['add_maintenance_window_1:action_result.parameter.title', 'add_maintenance_window_1:action_result.data'], action_results=results)

    results_item_1_0 = [item[0] for item in results_data_1]
    results_item_1_1 = [item[1] for item in results_data_1]

    phantom.pin(container=container, data=results_item_1_1, message=results_item_1_0, name=None)

    return

def cf_community_list_deduplicate_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('cf_community_list_deduplicate_1() called')
    
    container_data_0 = phantom.collect2(container=container, datapath=['artifact:*.cef.entity_key', 'artifact:*.id'])

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
    phantom.custom_function(custom_function='community/list_deduplicate', parameters=parameters, name='cf_community_list_deduplicate_1', callback=cf_community_list_deduplicate_1_callback)

    return

def cf_community_list_deduplicate_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('cf_community_list_deduplicate_1_callback() called')
    
    format_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
    add_comment_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def add_comment_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_2() called')

    custom_function_results_data_1 = phantom.collect2(container=container, datapath=['cf_community_list_deduplicate_1:custom_function_result.data.*.item'], action_results=results)

    custom_function_results_item_1_0 = [item[0] for item in custom_function_results_data_1]

    phantom.comment(container=container, comment=custom_function_results_item_1_0)

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