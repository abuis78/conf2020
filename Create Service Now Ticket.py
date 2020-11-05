"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'format_3' block
    format_3(container=container)

    return

def create_ticket_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('create_ticket_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'create_ticket_1' call
    formatted_data_1 = phantom.get_format_data(name='description')
    formatted_data_2 = phantom.get_format_data(name='Short_description')

    parameters = []
    
    # build parameters list for 'create_ticket_1' call
    parameters.append({
        'table': "incident",
        'fields': "{ \"caller_id\": \"phantom\" }",
        'vault_id': "",
        'description': formatted_data_1,
        'short_description': formatted_data_2,
    })

    phantom.act(action="create ticket", parameters=parameters, assets=['servicenow'], callback=update_episode_1, name="create_ticket_1")

    return

def Short_description(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Short_description() called')
    
    template = """New Ticket - Phantom ID: {0}"""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Short_description")

    description(container=container)

    return

def description(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('description() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "container:name",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="description")

    create_ticket_1(container=container)

    return

def pin_snow_ticket_id(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('pin_snow_ticket_id() called')

    formatted_data_1 = phantom.get_format_data(name='format_6')

    phantom.pin(container=container, data=formatted_data_1, message="snow_id", name=None)
    format_7(container=container)

    return

def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_1() called')

    # collect data for 'get_data_1' call
    formatted_data_1 = phantom.get_format_data(name='format_3')

    parameters = []
    
    # build parameters list for 'get_data_1' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], callback=decision_1, name="get_data_1")

    return

def format_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_3() called')
    
    template = """/rest/container_pin?_filter_container={0}&_filter_message=\"snow_id\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_3")

    get_data_1(container=container)

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_1() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["get_data_1:action_result.data.*.response_body.count", "==", 0],
        ])

    # call connected blocks if condition 1 matched
    if matched:
        Short_description(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # call connected blocks for 'else' condition 2
    get_pin_1(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def add_comment_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_2() called')

    formatted_data_1 = phantom.get_format_data(name='format_5')

    phantom.comment(container=container, comment=formatted_data_1)

    return

def get_pin_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_pin_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    id_value = container.get('id', None)

    # collect data for 'get_pin_1' call

    parameters = []
    
    # build parameters list for 'get_pin_1' call
    parameters.append({
        'query': "message=snow_id",
        'container_id': id_value,
    })

    phantom.act(action="get pin", parameters=parameters, assets=['phantom utilities'], callback=format_5, name="get_pin_1")

    return

def format_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_5() called')
    
    template = """%%
{0}
%%"""

    # parameter list for template variable replacement
    parameters = [
        "get_pin_1:action_result.data.*.data",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_5")

    add_comment_2(container=container)

    return

def format_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_6() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "create_ticket_1:action_result.summary.created_ticket_id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_6")

    pin_snow_ticket_id(container=container)

    return

def Pin_snow_inc(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Pin_snow_inc() called')

    formatted_data_1 = phantom.get_format_data(name='format_7')

    phantom.pin(container=container, data=formatted_data_1, message="snow inc", name=None)
    format_9(container=container)

    return

def format_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_7() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "create_ticket_1:action_result.data.*.number",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_7")

    Pin_snow_inc(container=container)

    return

def add_episode_ticket_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_episode_ticket_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    source_data_identifier_value = container.get('source_data_identifier', None)

    # collect data for 'add_episode_ticket_1' call
    results_data_1 = phantom.collect2(container=container, datapath=['create_ticket_1:action_result.data.*.number', 'create_ticket_1:action_result.parameter.context.artifact_id'], action_results=results)
    formatted_data_1 = phantom.get_format_data(name='format_8')

    parameters = []
    
    # build parameters list for 'add_episode_ticket_1' call
    for results_item_1 in results_data_1:
        parameters.append({
            'ticket_id': results_item_1[0],
            'ticket_url': formatted_data_1,
            'itsi_group_id': source_data_identifier_value,
            'ticket_system': "Service Now",
            # context (artifact id) is added to associate results with the artifact
            'context': {'artifact_id': results_item_1[1]},
        })

    phantom.act(action="add episode ticket", parameters=parameters, assets=['splunk itsi'], callback=format_6, name="add_episode_ticket_1")

    return

def parse_url_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('parse_url_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'parse_url_1' call
    results_data_1 = phantom.collect2(container=container, datapath=['create_ticket_1:action_result.data.*.sys_domain.link', 'create_ticket_1:action_result.parameter.context.artifact_id'], action_results=results)

    parameters = []
    
    # build parameters list for 'parse_url_1' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'url_to_parse': results_item_1[0],
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="parse url", parameters=parameters, assets=['phantom utilities'], callback=format_8, name="parse_url_1", parent_action=action)

    return

def format_8(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_8() called')
    
    template = """{0}://{1}/incident.do?sysparm_query=number={2}"""

    # parameter list for template variable replacement
    parameters = [
        "parse_url_1:action_result.data.*.scheme",
        "parse_url_1:action_result.data.*.netloc",
        "create_ticket_1:action_result.data.*.number",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_8")

    add_episode_ticket_1(container=container)

    return

def format_9(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_9() called')
    
    template = """{{\"state\":\"2\"}}"""

    # parameter list for template variable replacement
    parameters = [
        "create_ticket_1:action_result.data.*.caller_id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_9")

    update_ticket_1(container=container)

    return

def update_ticket_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_ticket_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'update_ticket_1' call
    results_data_1 = phantom.collect2(container=container, datapath=['create_ticket_1:action_result.data.*.number', 'create_ticket_1:action_result.parameter.context.artifact_id'], action_results=results)
    formatted_data_1 = phantom.get_format_data(name='format_9')

    parameters = []
    
    # build parameters list for 'update_ticket_1' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'id': results_item_1[0],
                'table': "incident",
                'fields': formatted_data_1,
                'vault_id': "",
                'is_sys_id': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act(action="update ticket", parameters=parameters, assets=['servicenow'], name="update_ticket_1")

    return

def update_episode_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_episode_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    source_data_identifier_value = container.get('source_data_identifier', None)

    # collect data for 'update_episode_1' call

    parameters = []
    
    # build parameters list for 'update_episode_1' call
    parameters.append({
        'owner': "admin",
        'status': "In Progress",
        'severity': "Medium",
        'itsi_group_id': source_data_identifier_value,
    })

    phantom.act(action="update episode", parameters=parameters, assets=['splunk itsi'], callback=parse_url_1, name="update_episode_1", parent_action=action)

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