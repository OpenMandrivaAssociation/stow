%define name stow
%define version 1.3.3
%define release %mkrel 2

Summary: Separate software packages manager
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Configuration/Packaging
Source0: ftp://ftp.gnu.org/gnu/stow/%{name}-%{version}.tar.bz2
# (blino) from upstream CVS
Patch0: stow-1.3.3-root_foo.patch.bz2
URL: http://www.gnu.org/software/stow/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

%description
GNU Stow is a program for managing the installation of software packages,
keeping them separate (/usr/local/stow/emacs vs. /usr/local/stow/perl, for
example) while making them appear to e installed in the same place
(/usr/local).

%prep
%setup -q
%patch0 -p1 -b .root_foo

%build
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post
%_install_info %name

%postun
%_remove_install_info %name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man8/stow.*

