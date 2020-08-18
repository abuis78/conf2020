"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'playbook_conf2020_Notable_clean_up_1' block
    playbook_conf2020_Notable_clean_up_1(container=container)

    return

def playbook_itsi_itsi_itsi_create_hud_snow_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_itsi_itsi_itsi_create_hud_snow_1() called')
    
    # call playbook "itsi/itsi_create_hud_snow", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="itsi/itsi_create_hud_snow", container=container, name="playbook_itsi_itsi_itsi_create_hud_snow_1", callback=playbook_itsi_itsi_ITSI_Pin_Information_V2_1)

    return

def playbook_conf2020_Notable_clean_up_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_conf2020_Notable_clean_up_1() called')
    
    # call playbook "conf2020/Notable_clean_up", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="conf2020/Notable_clean_up", container=container, name="playbook_conf2020_Notable_clean_up_1", callback=playbook_itsi_itsi_itsi_create_hud_snow_1)

    return

def playbook_itsi_itsi_ITSI_Pin_Information_V2_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_itsi_itsi_ITSI_Pin_Information_V2_1() called')
    
    # call playbook "itsi/ITSI_Pin_Information_V2", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="itsi/ITSI_Pin_Information_V2", container=container, name="playbook_itsi_itsi_ITSI_Pin_Information_V2_1", callback=playbook_itsi_itsi_ITSI_Pin_Service_information_1)

    return

def playbook_itsi_itsi_ITSI_Pin_Service_information_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_itsi_itsi_ITSI_Pin_Service_information_1() called')
    
    # call playbook "itsi/ITSI_Pin_Service_information", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="itsi/ITSI_Pin_Service_information", container=container, name="playbook_itsi_itsi_ITSI_Pin_Service_information_1", callback=playbook_itsi_itsi_ITSI_start_NGINX_1)

    return

def playbook_itsi_itsi_ITSI_start_NGINX_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_itsi_itsi_ITSI_start_NGINX_1() called')
    
    # call playbook "itsi/ITSI_start_NGINX", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="itsi/ITSI_start_NGINX", container=container, name="playbook_itsi_itsi_ITSI_start_NGINX_1", callback=playbook_itsi_itsi_ITSI_close_episode_snow_1)

    return

def playbook_itsi_itsi_ITSI_close_episode_snow_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_itsi_itsi_ITSI_close_episode_snow_1() called')
    
    # call playbook "itsi/ITSI_close_episode_snow", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="itsi/ITSI_close_episode_snow", container=container, name="playbook_itsi_itsi_ITSI_close_episode_snow_1")

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