%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	DB2
Summary:	DBD::DB2 perl module
Summary(pl):	Modu³ perla DBD::DB2
Name:		perl-DBD-DB2
Version:	0.76
Release:	1
License:	IBM (see LICENSE)
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-DBI >= 0.93
BuildRequires:	rpm-perlprov >= 3.0.3-16
#BR: DB2 Software Developer's Kit v5.2
#or  DB2 Application Development Client v6 or later
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::DB2 is a Perl5 module which when used in conjunction with DBI
allows Perl5 to communicate with IBM's DB2 Universal Database.

%description -l pl
DBD::DB2 jest modu³em Perla, który w po³±czeniu z DBI pozwala
komunikowaæ siê z DB2 Universal Database firmy IBM z poziomu Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{?db2root:DB2_HOME="%{db2root}"; export DB2_HOME}
perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CAVEATS HISTORY LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
#%{perl_sitearch}/???
%{_mandir}/man3/*
