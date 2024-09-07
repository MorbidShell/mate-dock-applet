Name:		mate-dock-applet	
Version:	21.10.0
Release:	1%{?dist}
Summary:	An application dock applet for the MATE panel

Group:		Unspecified
License:	GPLv3
URL:		https://github.com/ubuntu-mate/mate-dock-applet
Source0:	https://github.com/ubuntu-mate/mate-dock-applet/releases/tag/V%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python3-cairo
BuildRequires:	glib2-devel
BuildRequires:	python3-imaging
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
Requires:	python3
Requires:	python3-imaging
Requires:	python3-cairo

%if 0%{?fedora} >= 25
    %define with_gtk3 --with-gtk3
%endif

%description
The applet works with both GTK2 and GTK3 versions of MATE and allows you to:

* Place a dock on any MATE panel, of any size, on any side of the
  desktop you desire.
* Pin and unpin apps to the dock
* Rearrange application icons on the dock
* Launch apps by clicking on their icons in the dock
* Minimize/unminimize running app windows by clicking the app's dock icon
* Detect changes in the current icon theme and update the dock accordingly
* Use an indicator by each app to show when it is running
* Optionally, use multiple indicators for each window an app has open
* Use either a light or dark indicator that it can always be seen no matter
  what colour the panel is, or turn indicators off altogether
* Change the colour of MATE panels to the dominant colour (i.e. the most
  common colour) of the desktop wallpaper. The colour can be applied to
  all panels or just the panel containing the dock.


%prep
%setup -q
aclocal
automake --add-missing
autoreconf

%build
%configure %{?with_gtk3}
make %{?_smp_mflags}


%install
%make_install


%files
%{_datadir}/mate-panel/applets/org.mate.panel.DockApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.DockAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.dock.gschema.xml
%{_libdir}/mate-applets/mate-dock-applet
%license COPYING
%doc AUTHORS INSTALL ChangeLog NEWS README
