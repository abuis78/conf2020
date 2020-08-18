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
            ["artifact:*.cef.serviceid", "!=", ""],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        DedupeListEntries(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2

    return

"""
Removes duplicates from list and keeps list order
"""
def DedupeListEntries(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('DedupeListEntries() called')
    
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.serviceid', 'artifact:*.id'])
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
    format_2(container=container)

    return

def Add_Pin_with_Service_Name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Add_Pin_with_Service_Name() called')

    formatted_data_1 = phantom.get_format_data(name='Format_Service_Name')

    phantom.pin(container=container, data=formatted_data_1, message="Service", pin_type="card", pin_style="red", name=None)

    return

def Format_Service_Name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Format_Service_Name() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "Get_Service:action_result.data.*.identifying_name",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Format_Service_Name")

    Build_link_for_check_data_pin(container=container)

    return

def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_2() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "DedupeListEntries:custom_function:new_list",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    Get_Service(container=container)

    return

def Get_Service(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Get_Service() called')

    # collect data for 'Get_Service' call
    formatted_data_1 = phantom.get_format_data(name='format_2')

    parameters = []
    
    # build parameters list for 'Get_Service' call
    parameters.append({
        'indexed_itsi_service_id': formatted_data_1,
    })

    phantom.act(action="get service", parameters=parameters, assets=['splunk itsi'], callback=Format_Service_Name, name="Get_Service")

    return

def Build_link_for_check_data_pin(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Build_link_for_check_data_pin() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"Service\"&_filter_data=\"{1}\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
        "Format_Service_Name:formatted_data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Build_link_for_check_data_pin")

    get_data_1(container=container)

    return

def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_data_1' call
    formatted_data_1 = phantom.get_format_data(name='Build_link_for_check_data_pin')

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
        Add_Pin_with_Service_Name(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2

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