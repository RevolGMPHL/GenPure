import json
import os
import sched
import time

base_path = os.path.abspath(os.path.dirname(__file__))


def delete_file(file_path):
    if not os.path.exists(file_path):
        return
    try:
        os.remove(file_path)
        print(f"Delete file success: {file_path}")
    except Exception as e:
        print(f"ERROR: delete file failed: file path: {file_path}, exception: {e}")


def schedule_delete_file(file_path):
    if not os.path.exists(file_path):
        return
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(60 * 60, 1, delete_file, kwargs={'file_path': file_path})


def get_setting_from_env_or_json(setting_name: str) -> str:
    setting_value = os.getenv(setting_name)
    if setting_value is not None and len(str(setting_value)) > 0:
        return setting_value
    try:
        setting_path = os.path.join(base_path, '..', '..')
        print(f'find setting in path {setting_path}')
        env_file_path = os.path.join(setting_path, 'env.json')
        if os.path.exists(env_file_path):
            with open(env_file_path) as f:
                env = json.load(f)
                if setting_name in env:
                    return env[setting_name]
                else:
                    print(f'Can not find env: {setting_name} from env file: {env_file_path}')
        else:
            print(f'Can not find env file: {env_file_path}')
    except:
        pass
    print(f'Can not get env: {setting_name}')
    return ''
