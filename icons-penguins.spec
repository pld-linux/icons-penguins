Summary:	Penguin icons
Summary(pl.UTF-8):	Pingwinowe ikony
Name:		icons-penguins
Version:	1.0
Release:	1
License:	Freeware
Group:		X11/Amusements
Source0:	%{name}.tar.bz2
# Source0-md5:	32f0cd4a257ea21bf709b36ecaa9edd0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Icons with penguins.

%description -l pl.UTF-8
Ikony z pingwinami w roli głównej.

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
