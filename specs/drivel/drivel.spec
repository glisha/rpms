# $Id$
# Authority: dag
# Upstream: Todd Kulesza <todd@dropline.net>

Summary: LiveJournal client for GNOME
Name: drivel
Version: 0.90.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.dropline.net/drivel/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/drivel/drivel-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gtk2 >= 2.0.0, curl >= 7.10.0

%description
Drivel is an advanced LiveJournal client for the GNOME desktop.  While 
maintaining a full set of features, it had been designed with usability 
in mind, and presents an elegant user interface.

%prep
%setup

%build
%configure \
        --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/drivel/

%changelog
* Mon May 24 2004 Dag Wieers <dag@wieers.com> - 0.90.0-1
- Updated to release 0.90.0.

* Thu Mar 25 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Initial package. (using DAR)
