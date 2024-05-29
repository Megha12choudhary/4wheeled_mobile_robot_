cmake_minimum_required(VERSION 3.8)
project(mobile_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
# Uncomment the following section to add further dependencies manually.
# find_package(<dependency> REQUIRED)

# Install directories
install(
   DIRECTORY launch model
   DESTINATION share/${PROJECT_NAME})

# Build testing
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # The following line skips the linter which checks for copyrights.
  # Comment out the line when a copyright and license are added to all source files.
  set(ament_cmake_copyright_FOUND TRUE)
  # The following line skips cpplint (only works in a git repo).
  # Comment out the line when this package is in a git repo and when
  # a copyright and license are added to all source files.
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

