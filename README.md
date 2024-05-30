Simulation of 4 wheeled mobile robot using ros2 humble and gazebo  and showed the movement of mbile robot in gazebo using teleop_twist_keyboard.
steps:
mkdir -p ros2_ws/src
cd ros2_ws/
git clone
cd...

cd ros2_ws/
colcon build --packages-select <packagename>

source ~/ros2_ws/install/setup.bash
ros2 launch <packagename> gazebo_model.launch.py


To use teleop twist
ros2 run teleop_twist_keyboard teleop_twist_keyboard.py
