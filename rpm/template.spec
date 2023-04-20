%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-python-qt-binding
Version:        1.2.3
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS python_qt_binding package

License:        BSD
URL:            http://ros.org/wiki/python_qt_binding
Source0:        %{name}-%{version}.tar.gz

Requires:       clang
Requires:       python3-devel
Requires:       python3-pyside2-devel
Requires:       python3-shiboken2-devel
Requires:       ros-iron-ros-workspace
BuildRequires:  clang
BuildRequires:  python3-devel
BuildRequires:  python3-pyside2-devel
BuildRequires:  python3-shiboken2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-pytest
BuildRequires:  ros-iron-ament-lint-auto
BuildRequires:  ros-iron-ament-lint-common
%endif

%description
This stack provides Python bindings for Qt. There are two providers: pyside and
pyqt. PySide2 is available under the GPL, LGPL and a commercial license. PyQt is
released under the GPL. Both the bindings and tools to build bindings are
included from each available provider. For PySide, it is called
&quot;Shiboken&quot;. For PyQt, this is called &quot;SIP&quot;. Also provided is
adapter code to make the user's Python code independent of which binding
provider was actually used which makes it very easy to switch between these.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Apr 20 2023 Shane Loretz <sloretz@openrobotics.org> - 1.2.3-2
- Autogenerated by Bloom

* Tue Apr 11 2023 Shane Loretz <sloretz@openrobotics.org> - 1.2.3-1
- Autogenerated by Bloom

* Tue Mar 28 2023 Shane Loretz <sloretz@openrobotics.org> - 1.2.2-5
- Autogenerated by Bloom

* Mon Mar 27 2023 Shane Loretz <sloretz@openrobotics.org> - 1.2.2-4
- Autogenerated by Bloom

* Mon Mar 27 2023 Shane Loretz <sloretz@openrobotics.org> - 1.2.2-3
- Autogenerated by Bloom

* Tue Mar 21 2023 Shane Loretz <sloretz@openrobotics.org> - 1.2.2-2
- Autogenerated by Bloom

