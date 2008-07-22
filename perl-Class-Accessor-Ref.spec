%define real_name Class-Accessor-Ref

Summary:	Class-Accessor-Ref module for perl 
Name:		perl-%{real_name}
Version:	0.05
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAL/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl-Class-Accessor
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is an extension of Class::Accessor that allows taking a reference
of members of an object. This is typically useful when your class
implementation uses a third-party module that expects an in/out parameter
in its interface.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes examples
%{perl_vendorlib}/Class/Accessor/Ref.pm
%{_mandir}/*/*


