set(NAME unit_tests)

file(GLOB SOURCES
        "*.h"
        "*.cpp"
)

add_executable(${NAME} ${SOURCES})

if(${TARGET_PLATFORM} STREQUAL "x86" AND ${CMAKE_BUILD_TYPE} STREQUAL "Debug")
	include(../../../CodeCoverage.cmake)

	find_program( LCOV_PATH lcov )
	if(LCOV_PATH)
		message("lcov found! Creating coverage target...")
		append_coverage_compiler_flags()
		setup_target_for_coverage(
			NAME ${NAME}_coverage                    # New target name
			EXECUTABLE ${NAME} -j ${PROCESSOR_COUNT} # Executable in PROJECT_BINARY_DIR
			DEPENDENCIES ${NAME}                     # Dependencies to build first
		)
	endif() # LCOV_PATH
endif()

target_link_libraries(${NAME}
	libs
	core
	gtest
	gtest_main
)

target_format_sources(${NAME} "${SOURCES}")