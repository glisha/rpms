# $Id$

# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define real_name Pod-Coverage
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Checks if the documentation of a module is comprehensive
Name: perl-Pod-Coverage
Version: 0.17
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Coverage/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Coverage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-Module-Build

%description
Checks if the documentation of a module is comprehensive.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{_bindir}/*
%{perl_vendorarch}/Pod/Coverage.pm
%{perl_vendorarch}/Pod/Coverage/*
%{perl_vendorarch}/auto/Pod/Coverage/*

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Updated to release 0.17.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
