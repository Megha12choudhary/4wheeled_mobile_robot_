import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
     
    # This name has to match the robot name in the xacro file
    robotXacroName = "differential_drive_robot"
     
    # This is the name of our package, at the same time, this is the name of the 
    # folder that will be used to define the paths
    namePackage = "mobile_robot"
     
    # This is a relative path to the xacro file defining the model
    modelFileRelativePath = "model/robot.xacro"
     
    # This is a relative path to the gazebo world file
    worldFileRelativePath = "model/empty_world.world"
      
    # This is the absolute path to model
    pathModelFile = os.path.join(get_package_share_directory(namePackage), modelFileRelativePath)
     
    # This is the absolute path to the world model
    pathWorldFile = os.path.join(get_package_share_directory(namePackage), worldFileRelativePath)
    
    # Get the robot description from xacro model file
    robotDescription = xacro.process_file(pathModelFile).toxml()
     
    # This is the launch file from the gazebo_ros_package
    gazebo_ros_packageLaunch = PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'))
     
    # This is the launch description
    gazeboLaunch = IncludeLaunchDescription(gazebo_ros_packageLaunch, launch_arguments={'world': pathWorldFile}.items())
     
    # Here, we create a gazebo_ros_Node
    spawnModelNode = Node(package='gazebo_ros', executable='spawn_entity.py', arguments=['-topic', 'robot_description', '-entity', robotXacroName], output='screen')
     
    # Robot State Publisher Node
    nodeRobotStatePublisher = Node(
         package="robot_state_publisher",
         executable="robot_state_publisher",
         output="screen",
         parameters=[{'robot_description': robotDescription, 'use_sim_time': True}]
    )
     
    # Here we create an empty launch description object
    launchDescriptionObject = LaunchDescription()
     
    # We add gazeboLaunch
    launchDescriptionObject.add_action(gazeboLaunch)
     
    # We add the two nodes
    launchDescriptionObject.add_action(spawnModelNode)
    launchDescriptionObject.add_action(nodeRobotStatePublisher)
     
    return launchDescriptionObject



