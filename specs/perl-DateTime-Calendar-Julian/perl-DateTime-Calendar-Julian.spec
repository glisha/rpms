# $Id$
# Authority: dries
# Upstream: Eugene van der Pijll <pijll$gmx,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Calendar-Julian

Summary: Dates in the Julian calendar
Name: perl-DateTime-Calendar-Julian
Version: 0.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Calendar-Julian/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Calendar-Julian-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a companion module to DateTime.pm. It implements the Julian
calendar. It supports everything that DateTime.pm supports and more:
about one day per century more, to be precise.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Calendar/
%{perl_vendorlib}/DateTime/Calendar/Julian.pm

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
