Summary: Separate software packages manager
Name: stow
Version: 2.4.1
Release: 1
License: GPLv3
Group: System/Configuration/Packaging
Source0: https://ftp.gnu.org/gnu/stow/%{name}-%{version}.tar.gz
URL: https://www.gnu.org/software/stow/
BuildArch: noarch

BuildRequires:  perl-Test-Output
%description
GNU Stow is a program for managing the installation of software packages,
keeping them separate (/usr/local/stow/emacs vs. /usr/local/stow/perl, for
example) while making them appear to e installed in the same place
(/usr/local).


%prep
%setup -q

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --with-pmdir=%{_usr}/share/perl5/vendor_perl/ && make

%install
%make_install
cd $RPM_BUILD_ROOT/usr/share/doc/stow/
rm -f ChangeLog* README.md INSTALL.md version.texi
rm -rf manual-split manual-single.html

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog NEWS README.md THANKS TODO
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man8/stow.*
%{_usr}/share/perl5/vendor_perl/


%changelog
* Tue Feb 18 2025 Christian Olsson <chrols@chrols.se> 2.4.1-1
- version update 2.4.1

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

