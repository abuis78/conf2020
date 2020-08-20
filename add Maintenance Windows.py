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
    formatted_data_1 = phantom.get_format_data(name='entity_ID')

    parameters = []
    
    # build parameters list for 'add_maintenance_window_1' call
    parameters.append({
        'title': "Bluber",
        'comment': "Phantom hast started Maintenance Windows",
        'end_time': "",
        'object_ids': formatted_data_1,
        'start_time': "",
        'object_type': "entity",
        'relative_end_time': 300,
        'relative_start_time': "",
    })

    phantom.act(action="add maintenance window", parameters=parameters, assets=['splunk itsi'], callback=Maintenance_ID, name="add_maintenance_window_1")

    return

def pin_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('pin_1() called')

    formatted_data_1 = phantom.get_format_data(name='Maintenance_title')
    formatted_data_2 = phantom.get_format_data(name='Maintenance_ID')

    phantom.pin(container=container, data=formatted_data_2, message=formatted_data_1, name=None)

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
    phantom.custom_function(custom_function='community/list_deduplicate', parameters=parameters, name='cf_community_list_deduplicate_1', callback=entity_ID)

    return

def entity_ID(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('entity_ID() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "cf_community_list_deduplicate_1:custom_function_result.data.*.item",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="entity_ID")

    add_maintenance_window_1(container=container)

    return

def Maintenance_ID(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Maintenance_ID() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "add_maintenance_window_1:action_result.data.*._key",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Maintenance_ID")

    Maintenance_title(container=container)

    return

def Maintenance_title(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Maintenance_title() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "add_maintenance_window_1:action_result.parameter.title",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Maintenance_title")

    pin_1(container=container)

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