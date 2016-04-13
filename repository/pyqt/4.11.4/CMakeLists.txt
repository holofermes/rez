CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(pyqt_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(make_args VERBOSE=1)
set(config_common --verbose
                  --confirm-license
                  --bindir=${CMAKE_INSTALL_PREFIX}
                  --destdir=${CMAKE_INSTALL_PREFIX}/Lib/site-packages
                  --sipdir=${CMAKE_INSTALL_PREFIX}/sip/PyQt
                  --sip-incdir=$ENV{REZ_SIP_ROOT}/Include
                  --enable=QtCore
                  --enable=QtDesigner
                  --enable=QtGui
                  --enable=QtHelp
                  --enable=QtMultimedia
                  --enable=QtMultimediaWidgets
                  --enable=QtNetwork
                  --enable=QtOpenGL
                  --enable=QtPrintSupport
                  --enable=QtQml
                  --enable=QtQuick
                  --enable=QtQuickWidgets
                  --enable=QtSensors
                  --enable=QtSerialPort
                  --enable=QtSql
                  --enable=QtSvg
                  --enable=QtWebChannel
                  --enable=QtWebEngineWidgets
                  --enable=QtWebKit
                  --enable=QtWebKitWidgets
                  --enable=QtWebSockets
                  --enable=QtWidgets
                  --enable=QtWinExtras
                  --enable=QtXml
                  --enable=QtXmlPatterns
    )

if("${CMAKE_SYSTEM_NAME}" MATCHES "Linux")
    set(make_cmd make)
    set(config_cmd "--spec ???" ${config_common})
    set(src_ext tag.gz)
    set(src_name x11-gpl)
    set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})
    
elseif("${CMAKE_SYSTEM_NAME}" MATCHES "Windows")
    set(make_cmd nmake)
    set(config_cmd "--spec win64-msvc2010" ${config_common})
    set(src_ext zip)
    set(src_name win-gpl)
endif()


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${make_cmd} install ${make_args})
else()
    set(install_cmd "")
endif()

rez_set_archive(
    url_pyqt pyqt/PyQt-${src_name}-${pyqt_version}.${src_ext}
    https://riverbankcomputing.com/software/pyqt/download
)

ExternalProject_add(
    pyqt
    URL ${url_pyqt}
    PREFIX pyqt
    INSTALL_COMMAND "${install_cmd}"
    CONFIGURE_COMMAND python ./configure.py ${configuree_args}
    BUILD_COMMAND ${make_cmd} ${make_args}
    BUILD_IN_SOURCE 1
)

