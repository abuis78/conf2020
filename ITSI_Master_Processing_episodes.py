"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'playbook_conf2020_conf2020_Notable_clean_up_1' block
    playbook_conf2020_conf2020_Notable_clean_up_1(container=container)

    return

def playbook_conf2020_conf2020_Add_SNOW_Information_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Add_SNOW_Information_1() called')
    
    # call playbook "conf2020/Add SNOW Information", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Add SNOW Information", container=container, name="playbook_conf2020_conf2020_Add_SNOW_Information_1", callback=playbook_conf2020_conf2020_Add_entity_information_1)

    return

def playbook_conf2020_conf2020_Notable_clean_up_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Notable_clean_up_1() called')
    
    # call playbook "conf2020/Notable_clean_up", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Notable_clean_up", container=container, name="playbook_conf2020_conf2020_Notable_clean_up_1", callback=playbook_conf2020_conf2020_Add_SNOW_Information_1)

    return

def playbook_conf2020_conf2020_Add_entity_information_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Add_entity_information_1() called')
    
    # call playbook "conf2020/Add entity information", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Add entity information", container=container, name="playbook_conf2020_conf2020_Add_entity_information_1", callback=playbook_conf2020_conf2020_Get_Service_information_1)

    return

def playbook_conf2020_conf2020_Get_Service_information_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Get_Service_information_1() called')
    
    # call playbook "conf2020/Get Service information", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Get Service information", container=container, name="playbook_conf2020_conf2020_Get_Service_information_1", callback=playbook_conf2020_conf2020_Restart_Service_1)

    return

def playbook_conf2020_conf2020_Restart_Service_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_conf2020_Restart_Service_1() called')
    
    # call playbook "conf2020/Restart Service", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Restart Service", container=container, name="playbook_conf2020_conf2020_Restart_Service_1", callback=playbook_conf2020_Close_SNOW_Ticket_1)

    return

def playbook_conf2020_Close_SNOW_Ticket_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_Close_SNOW_Ticket_1() called')
    
    # call playbook "conf2020/Close SNOW Ticket", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Close SNOW Ticket", container=container, name="playbook_conf2020_Close_SNOW_Ticket_1")

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