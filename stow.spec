Summary: Separate software packages manager
Name: stow
Version: 2.1.1
Release: 1
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

%build
%configure2_5x 
%make

%install
%makeinstall

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man8/stow.*
%{_usr}/lib/perl5/site_perl/
