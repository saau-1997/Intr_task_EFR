from launch import LaunchDescription
import launch_ros.actions 

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='turtlesim',
            namespace= "turtlesim1", 
            executable='turtlesim_node',
        ),
        launch_ros.actions.Node(
            package='turtlesim', 
            namespace= "turtlesim1", 
            prefix = "xterm -e", #open a new terminal an run the node there
            executable='turtle_teleop_key'
        ),
    ])
