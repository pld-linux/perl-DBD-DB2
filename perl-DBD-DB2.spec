#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	DBD
%define		pnam	DB2
Summary:	DBD::DB2 - database driver for DB2 UDB
Summary(pl.UTF-8):	DBD::DB2 - sterownik bazy danych DB2
Name:		perl-DBD-DB2
Version:	0.80
Release:	1
License:	distributable (see LICENSE)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7391c071dd1e7f3e8953077d0fe084f6
URL:		http://search.cpan.org/dist/DBD-DB2/
BuildRequires:	perl-DBI >= 0.93
BuildRequires:	rpm-perlprov >= 4.1-13
#BR: DB2 Software Developer's Kit v5.2
#or  DB2 Application Development Client v6 or later
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::DB2 is a Perl module which when used in conjunction with DBI
allows Perl to communicate with IBM's DB2 Universal Database.

%description -l pl.UTF-8
DBD::DB2 jest modułem Perla, który w połączeniu z DBI pozwala
komunikować się z DB2 Universal Database firmy IBM z poziomu Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{?db2root:DB2_HOME="%{db2root}"; export DB2_HOME}
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CAVEATS HISTORY LICENSE README
#%%{perl_vendorarch}/???
%{_mandir}/man3/*
