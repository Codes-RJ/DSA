cmake_minimum_required(VERSION 3.16)

project(dsa_cpp_curriculum VERSION 0.1.0 LANGUAGES CXX)

option(DSA_ENABLE_SANITIZERS "Enable AddressSanitizer and UndefinedBehaviorSanitizer" OFF)

add_library(dsa_examples INTERFACE)
target_include_directories(dsa_examples INTERFACE
    "${CMAKE_CURRENT_SOURCE_DIR}/examples/include"
)
target_compile_features(dsa_examples INTERFACE cxx_std_17)

if(MSVC)
    target_compile_options(dsa_examples INTERFACE /W4 /permissive-)
else()
    target_compile_options(dsa_examples INTERFACE
        -Wall -Wextra -Wpedantic -Wconversion -Wshadow
    )
endif()

if(DSA_ENABLE_SANITIZERS AND NOT MSVC)
    target_compile_options(dsa_examples INTERFACE
        -fsanitize=address,undefined -fno-omit-frame-pointer
    )
    target_link_options(dsa_examples INTERFACE
        -fsanitize=address,undefined -fno-omit-frame-pointer
    )
endif()

include(CTest)
if(BUILD_TESTING)
    add_executable(dsa_smoke_tests tests/smoke_tests.cpp)
    target_link_libraries(dsa_smoke_tests PRIVATE dsa_examples)
    add_test(NAME dsa_smoke_tests COMMAND dsa_smoke_tests)
endif()
