# $Id: hackedbox.spec,v 1.9 2004/02/23 12:36:00 dude Exp $

Summary: The bastard son of Blackbox, a small and fast Window Manager
Name: hackedbox
Version: 0.8.3
Release: 1
License: GPL
Group: User Interface/Desktops
Source0: http://scrudgeware.org/downloads/hackedbox/hackedbox-%{version}.tar.gz
Source1: hackedbox.desktop
URL: http://scrudgeware.org/projects/Hackedbox
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel, libstdc++-devel, gcc-c++, perl

%description
Hackedbox is a stripped down version of Blackbox - The X11 Window Manager.
The toolbar and Slit have been removed. The goal of Hackedbox is to be a
small "feature-set" window manager, with no bloat. There are no plans to
add any functionality, only bugfixes and speed enhancements whenever possible.


%prep
%setup


%build
# Work around NLS problem
export LANG="en_US" LC_ALL="en_US"
%configure
%{__make} %{?_smp_mflags}


%install
rm -rf %{buildroot}
%makeinstall
#rm -rf %{buildroot}%{_mandir}/??_??

# Install Session file
%{__mkdir_p} %{buildroot}/etc/X11/gdm/Sessions
%{__cat} > %{buildroot}/etc/X11/gdm/Sessions/Hackedbox << EOF
#!/bin/sh
exec /etc/X11/xdm/Xsession %{name}
EOF

# Replace the /usr/local stuff
%{__perl} -pi -e 's|/local||g' %{buildroot}%{_datadir}/%{name}/menu

# Install the desktop entry
%{__install} -m 644 -D %{SOURCE1} \
    %{buildroot}%{_datadir}/xsessions/%{name}.desktop


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README TODO
%attr(755, root, root) /etc/X11/gdm/Sessions/Hackedbox
%{_bindir}/*
%config(noreplace) %{_datadir}/%{name}/menu
%{_datadir}/%{name}/backgrounds
%{_datadir}/%{name}/keys
%{_datadir}/%{name}/nls
%{_datadir}/%{name}/styles
%{_datadir}/xsessions/%{name}
%{_mandir}/man1/*


%changelog
* Mon Feb 23 2004 Matthias Saou <http://freshrpms.net/> - 0.8.2-3
- Apply the same nls workaround as for blackbox.
- Add the xsessions desktop file for recent gdm/kdm.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> - 0.8.2-2
- Rebuild for Fedora Core 1.
- Added the (currently mandatory) without nls conditional build.

* Sat Apr 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.2.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Jan  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.1.

* Mon Nov  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.0.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.3.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

