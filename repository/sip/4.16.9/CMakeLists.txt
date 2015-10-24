CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(sip_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(make_args)
set(config_common --bindir=${CMAKE_INSTALL_PREFIX}
                  --destdir=${CMAKE_INSTALL_PREFIX}/Lib/site-packages
                  --incdir=${CMAKE_INSTALL_PREFIX}/include
                  --sipdir=${CMAKE_INSTALL_PREFIX}/sip
    )

if("${CMAKE_SYSTEM_NAME}" MATCHES "Linux")
    set(make_cmd make)
    set(config_cmd "--platform ???" ${config_common})
    set(src_ext tag.gz)
    set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})
    
elseif("${CMAKE_SYSTEM_NAME}" MATCHES "Windows")
    set(make_cmd nmake)
    set(config_cmd "--platform win32-msvc2010" ${config_common})
    set(src_ext zip)
endif()


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${make_cmd} install ${make_args})
else()
    set(install_cmd "")
endif()

rez_set_archive(
    url_sip sip/sip-${sip_version}.${src_ext}
    https://riverbankcomputing.com/software/sip/download
)

ExternalProject_add(
    sip
    URL ${url_sip}
    PREFIX sip
    INSTALL_COMMAND "${install_cmd}"
    CONFIGURE_COMMAND python ./configure.py ${configuree_args}
    BUILD_COMMAND ${make_cmd} ${make_args}
    BUILD_IN_SOURCE 1
)

