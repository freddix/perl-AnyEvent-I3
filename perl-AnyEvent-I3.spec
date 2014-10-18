%include	/usr/lib/rpm/macros.perl

%define		pdir	AnyEvent
%define		pnam	I3

Summary:	Communicate with the i3 window manager
Name:		perl-AnyEvent-I3
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSTPLBG/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a282c832cee131e3c53dc5891a99a149
URL:		http://search.cpan.org/dist/common-sense/
BuildRequires:	perl-JSON-XS
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module connects to the i3 window manager using the UNIX socket
based IPC interface it provides (if enabled in the configuration
file). You can then subscribe to events or send messages and receive
their replies.

%prep
%setup -qn %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%dir %{perl_vendorlib}/common
%{perl_vendorlib}/common/*.pm
%{_mandir}/man3/common::sense.3pm*

