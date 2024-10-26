%define	modname	Cairo-GObject
%define _disable_ld_no_undefined 1
%define _disable_lto 1

# keep only versioned requires:
%global __requires_exclude ^perl\\(Cairo\\)$
%global __requires_exclude ^perl\\(Glib\\)$

Name:		perl-%{modname}
Version:	1.005
Release:	1

Summary:	Integrate Cairo into the Glib type system
License:	LGPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Cairo/%{modname}-%{version}.tar.gz

BuildRequires:	perl(Cairo)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib)
BuildRequires:	perl-devel
BuildRequires:	cairo-devel
BuildRequires:	gcc

%description
Integrate Cairo into the Glib type system.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc LICENSE META.json META.yml NEWS README examples
%{_mandir}/man3/*
%{perl_vendorarch}/*
