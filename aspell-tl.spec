Summary:	Tagalog dictionary for aspell
Summary(pl):	S³ownik tagalski dla aspella
Name:		aspell-tl
Version:	0.02
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/tl/aspell5-tl-%{version}-%{subv}.tar.bz2
# Source0-md5:	126437909424021a553055b1b96fdf73
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tagalog dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik tagalski (lista s³ów) dla aspella.

%prep
%setup -q -n aspell5-tl-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
