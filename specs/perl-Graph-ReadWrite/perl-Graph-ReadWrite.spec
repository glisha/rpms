# $Id$
# Authority: dries
# Upstream: Neil Bowers <neil$bowers,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graph-ReadWrite

Summary: Graph file format readers and writers
Name: perl-Graph-ReadWrite
Version: 2.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graph-ReadWrite/

Source: http://www.cpan.org/modules/by-module/Graph/Graph-ReadWrite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a collection of perl classes for reading and writing
directed graphs in a variety of file formats. The graphs are
represented in Perl using Jarkko Hietaniemi's Graph classes.

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
%doc README ChangeLog
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Graph/
%{perl_vendorlib}/Graph/*.pm
%{perl_vendorlib}/Graph/Reader/
%{perl_vendorlib}/Graph/Writer/

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.00-1
- Updated to release 2.00.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.
