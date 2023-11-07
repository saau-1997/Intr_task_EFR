This is a modification to the turtlesim package. 
The aim is to run a turtlesim window which makes the turtle move by the arrow keys and makes the background color
change when hitting the border of the canvas. The color shall depend on the side you hit the border, with the 
following configuration:
  ● Red color when hitting the top side
  ● Green color when hitting the right side
  ● Orange color when hitting the bottom side
  ● Blue color when hitting the left side
__________________________________________________________________________________________________________________________________
Prerequisites to run the simulation:
  ● ROS 2 installation: https://docs.ros.org/en/iron/Installation.html
  ● colcon installation: https://docs.ros.org/en/iron/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html
  ● git installation: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
  ● rosdep installation: https://docs.ros.org/en/iron/Tutorials/Intermediate/Rosdep.html
__________________________________________________________________________________________________________________________________
Procedure to run the simulation:

1. Open a new terminal
2. Source the setup files
  source /opt/ros/iron/setup.bash
5. Create a new directory e.g. new_workspace
  mkdir new_workspace
6. Navigate to the new_workspace directory
  cd new_workspace/
7. Create the source directory i.e. src
  mkdir src
8. Navigate to the src directory
  cd src/
9. Clone this repository
  git clone https://github.com/saau-1997/Intr_task_EFR/
10. Go back to the new_workspace directory
  cd ..
11. Resolve ros2 dependencies
  rosdep install -i --from-path src --rosdistro iron -y
12. Build the workspace with colcon
  colcon build --packages-select turtlesim
13. Source the overlay environment
  source install/local_setup.bash
14. Launch the turtlesim_node and turtle_teleop_key nodes
  ros2 launch src/Intr_task_EFR/turtlesim/launch/bkgcolor.launch.py
__________________________________________________________________________________________________________________________________


Two windows will open:
1. Elbflorace - Intro Task: Where the turtle is shown in a white canvas
2. turtle_teleop_key: new terminal which reads from keyboard.

IMPORTANT: Be sure to be able to see both windows simultaneously and that the new terminal turtle_teleop_key is the active one. 
Now the turtle can be controled using the keyboard as stated in the new terminal.
