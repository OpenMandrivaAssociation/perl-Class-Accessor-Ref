%define upstream_name    Class-Accessor-Ref
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Class-Accessor-Ref module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildArch:	noarch

%description
This is an extension of Class::Accessor that allows taking a reference
of members of an object. This is typically useful when your class
implementation uses a third-party module that expects an in/out parameter
in its interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes examples
%{perl_vendorlib}/Class/Accessor/Ref.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 680779
- mass rebuild

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 402278
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.05-3mdv2009.0
+ Revision: 241172
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2008.0
+ Revision: 46613
- update to new version 0.05


* Fri Dec 01 2006 Oden Eriksson <oeriksson@mandriva.com> 0.03-2mdv2007.0
+ Revision: 89737
- Import perl-Class-Accessor-Ref

* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Fix BuildRequires
- Fix Souce url
- %%mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdk
- initial Mandriva package

