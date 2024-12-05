# Copyright 2020 ros2_control Development Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from launch import LaunchDescription

from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch.actions import ExecuteProcess, OpaqueFunction

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterFile
from ament_index_python.packages import get_package_share_directory
import os

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

DEFAULT_CONFIG_PATH = \
    f'{os.environ["ROBOT_CONFIG_PATH"]}/example_package/example_config.yaml'

def launch_setup(context, *args, **kwargs):
    # Get URDF via xacro
    namespace_ = LaunchConfiguration("namespace").perform(context)

    default_config = DEFAULT_CONFIG_PATH \
        if os.path.exists(DEFAULT_CONFIG_PATH) else os.path.join(
            get_package_share_directory('gary_example_package'),
            'config',
            'example_config.yaml'
            )

    config_path_list = []
    config_path_list.append(default_config)
    config_path_list.append(f'{os.environ["ROBOT_CONFIG_PATH"]}/general.config.yaml')

    print(YELLOW + "List of loaded parameters" + RESET)
    for path in config_path_list:
        if not os.path.exists(path):
            print(RED + "Non-existent " + path + " file!" + RESET)
        else:
            print("- " + path)

    print(RED + "L, do you know, gods of death who love apple have red hands?" + RESET)


    status_node = Node(
        package="gary_example_package",
        executable="example_engine",
        namespace=namespace_,
        parameters=config_path_list,
        output="both",
        respawn=True,
        respawn_attempts=3,
        respawn_delay=5.0,
        respawn_attempt_timeout=20.0,
        respawn_longterm_delay=60.0,
    )

    nodes = [
        status_node,
    ]

    return nodes


def generate_launch_description():
    ns_arg = DeclareLaunchArgument(
        "namespace",
        default_value="gary/example/",
        description="define namespace",
    )

    return LaunchDescription(
        [ns_arg,
         OpaqueFunction(function=launch_setup),
         ])
