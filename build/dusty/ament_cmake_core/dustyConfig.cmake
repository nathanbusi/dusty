# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_dusty_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED dusty_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(dusty_FOUND FALSE)
  elseif(NOT dusty_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(dusty_FOUND FALSE)
  endif()
  return()
endif()
set(_dusty_CONFIG_INCLUDED TRUE)

# output package information
if(NOT dusty_FIND_QUIETLY)
  message(STATUS "Found dusty: 0.0.0 (${dusty_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'dusty' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${dusty_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(dusty_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${dusty_DIR}/${_extra}")
endforeach()
