%define debug_package %{nil}

Name:           kylin-nm
Version:        3.0.2
Release:        2
Summary:        Gui Applet tool for display and edit network simply
License:        GPL-3+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qtchooser
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtsvg-devel

Requires: NetworkManager
Requires: network-manager-applet

%description
 Kylin NM is a Applet tool for managing network settings simply.
 It has beautiful UI and very comfortable to use.
 It's better work together with UKUI.

%prep
%setup -q

%build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  kylin-nm.pro	
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/dbus-1/system.d/com.kylin.NetworkManager.qt.systemdbus.conf
%{_sysconfdir}/xdg/autostart/kylin-nm.desktop
%{_bindir}/kylin-nm
%{_datadir}/dbus-1/system-services/com.kylin.NetworkManager.qt.systemdbus.service

%changelog
* Tue Feb 2 2021 lvhan <lvhan@kylinos.cn> - 3.0.2-2
- update to upstream version 3.0.1-1

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.2-1
- update to upstream version 3.0.1-1+1026

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 1.2.4-1
- Init package for openEuler
