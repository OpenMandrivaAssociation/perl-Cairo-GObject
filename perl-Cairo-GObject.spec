%define	modname	Cairo-GObject
%define	modver	1.004

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	4

Summary:	Integrate Cairo into the Glib type system
License:	LGPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Cairo/%{modname}-%{modver}.tar.gz

BuildRequires:	perl(Cairo) >= 1.80.0
BuildRequires:	perl(ExtUtils::Depends) >= 0.200.0
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::PkgConfig) >= 1.0.0
BuildRequires:	perl(Glib) >= 1.224.0
BuildRequires:	perl-devel
BuildRequires:	cairo-devel

%description
Integrate Cairo into the Glib type system.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
#make test

%install
%makeinstall_std

%files
%doc LICENSE META.json META.yml MYMETA.yml NEWS README examples
%{_mandir}/man3/*
%{perl_vendorlib}/*
