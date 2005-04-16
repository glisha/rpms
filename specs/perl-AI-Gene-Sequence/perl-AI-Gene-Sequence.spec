# $Id$
# Authority: dries
# Upstream: Alex Gough <alex$earth,li>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-Gene-Sequence

Summary: Gene sequences
Name: perl-AI-Gene-Sequence
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-Gene-Sequence/

Source: http://search.cpan.org/CPAN/authors/id/A/AJ/AJGOUGH/AI-Gene-Sequence-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl module which you can use for gene sequences.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/AI/Gene/AI/Gene/Sequence.pm
%{perl_vendorlib}/AI/Gene/AI/Gene/Simple.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
