import os
import dotenv

root_path = os.path.abspath(os.path.dirname(__file__)).split('extensions')[0]


def init_dotenv():
    env_path = os.path.join(root_path, '.env')
    if os.path.exists(env_path):
        dotenv.load_dotenv(env_path)
