Summary:	Penguin icons
Summary(pl):	Pingwinowe ikony
Name:		icons-penguins
Version:	1.0
Release:	1
License:	Freeware
Group:		X11/Amusements
Source0:	%{name}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Icons with penguins.

%description -l pl
Ikony z pingwinami w roli g³ównej.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/penguins

install icons/* $RPM_BUILD_ROOT%{_pixmapsdir}/penguins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_pixmapsdir}/penguins
