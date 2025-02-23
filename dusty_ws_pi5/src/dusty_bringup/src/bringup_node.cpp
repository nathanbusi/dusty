#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

class BringupNode : public rclcpp::Node
{
public:
  BringupNode() : Node("bringup_node")
  {
    timer_ = this->create_wall_timer(
      1000ms, std::bind(&BringupNode::timer_callback, this));
  }

private:
  void timer_callback()
  {
    RCLCPP_INFO(this->get_logger(), "Bringup node is running...");
  }
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<BringupNode>());
  rclcpp::shutdown();
  return 0;
}
