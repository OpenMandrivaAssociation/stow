Summary: Separate software packages manager
Name: stow
Version: 2.2.0
Release: 2
License: GPL
Group: System/Configuration/Packaging
Source0: ftp://ftp.gnu.org/gnu/stow/%{name}-%{version}.tar.gz
# (blino) from upstream CVS
Patch0: stow-1.3.3-root_foo.patch.bz2
URL: https://www.gnu.org/software/stow/
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


%changelog
* Thu May 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.2.0-1
+ Revision: 795287
- version update 2.2.0

* Thu Dec 08 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.1.1-1
+ Revision: 738769
- version update 2.1.1

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.3.3-6mdv2010.0
+ Revision: 434137
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.3.3-5mdv2009.0
+ Revision: 261206
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.3.3-4mdv2009.0
+ Revision: 253568
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.3.3-2mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - use std info-install macros
    - kill re-definition of %%buildroot on Pixel's request
    - import stow

