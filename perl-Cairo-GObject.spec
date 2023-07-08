%define	modname	Cairo-GObject
%define	modver	1.005
%define _disable_ld_no_undefined 1
%define _disable_lto 1

# keep only versionated requires:
%global __requires_exclude ^perl\\(Cairo\\)$
%global __requires_exclude ^perl\\(Glib\\)$

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
BuildRequires:	gcc

%description
Integrate Cairo into the Glib type system.

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor CC=gcc LD=gcc
%make_build CC=gcc LD=gcc

%install
%make_install

%files
%doc LICENSE META.json META.yml NEWS README examples
%{_mandir}/man3/*
%{perl_vendorarch}/*
