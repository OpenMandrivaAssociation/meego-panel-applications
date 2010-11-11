Name: meego-panel-applications
Summary: Applications panel for MeeGo
Group: Graphical desktop/Other 
Version: 0.2.5
License: LGPL 2.1
URL: http://www.meego.com
Release: %mkrel 2
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: mutter-meego
BuildRequires: clutter-devel
BuildRequires: gtk2-devel
BuildRequires: gnome-menus-devel
BuildRequires: nbtk-devel
BuildRequires: meego-panel-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: mx-devel
Obsoletes: moblin-panel-applications <= 0.0.5

%description
MeeGo applications panel

%prep
%setup -q 

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
%{_datadir}/mutter-meego/panels/meego-panel-applications.desktop
