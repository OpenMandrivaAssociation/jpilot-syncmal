Summary:	SyncMAL plugin for J-PILOT
Name:		jpilot-syncmal
Version:	0.80
Release:	%mkrel 12
Epoch:		1
License:	MPL
Group:		Communications
URL:		http://jasonday.home.att.net/code/syncmal/syncmal.html
Source:		http://jasonday.home.att.net/code/syncmal/%{name}-%{version}.tar.gz
Patch0:		jpilot-syncmal-0.80-lib64.patch
# disables GTK+ 1.x test in configure.in, as it trips up autoreconf
# and we're not building against GTK+ 1.x anyway - AdamW 2007/07
Patch1:		jpilot-syncmal-0.80-disable_gtk1.patch
Patch2:		jpilot-syncmal-0.80-libtool_fixes.diff
BuildRequires:	gtk2-devel 
BuildRequires:	jpilot-devel >= 0.99.6 
BuildRequires:	pilot-link-devel >= 0.11.8 
BuildRequires:	libmal-devel >= 0.44
BuildRequires:	autoconf
Requires:	malsync
Requires:	jpilot >= 0.99.6 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SyncMAL is an interface to the command line tool malsync, a program
that synchronizes a PDA with a MAL server such as AvantGo.

See AvantGo's homepage <http://avantgo.com/> for more information on
AvantGo and MAL.

%prep

%setup -q
%patch0 -p1 -b .lib64
%patch1 -p1 -b .gtk1
%patch2 -p0 -b .libtool_fixes

%build

# needed by autoreconf
cp MPL-1_0.txt COPYING
touch NEWS
touch AUTHORS

# needed by patch0
AUTOMAKE="automake --add-missing" autoreconf

%configure --enable-gtk2

%make 

%install
rm -rf %{buildroot}

# this ridiculous buildsystem seems immune to sensible patching.
# it only installs stuff in libdir, so let's just set that here.
# - AdamW 2007/07
%makeinstall libdir=%{buildroot}%{_libdir}/jpilot/plugins

# cleanup
rm -f %{buildroot}%{_libdir}/jpilot/plugins/*.*a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog MPL-1_0.txt TODO
%{_libdir}/jpilot/plugins/libsyncmal.so


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.80-10mdv2011.0
+ Revision: 665833
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.80-9mdv2011.0
+ Revision: 606109
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.80-8mdv2010.1
+ Revision: 523089
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:0.80-7mdv2010.0
+ Revision: 425469
- rebuild

* Mon Nov 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.80-6mdv2009.1
+ Revision: 301750
- added some libtool fixes
- fix deps

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1:0.80-4mdv2008.1
+ Revision: 150421
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Sep 17 2007 Olivier Blin <oblin@mandriva.com> 1:0.80-3mdv2008.0
+ Revision: 89129
- rebuild because of package loss

* Wed Jul 25 2007 Adam Williamson <awilliamson@mandriva.org> 1:0.80-2mdv2008.0
+ Revision: 55601
- okay, let's handle x86-64 a different way
- update patch0 to fix pilot-link test too
- add patch1 to disable GTK+ 1.x test which is stopping autoreconf working
- rework patch
- update buildrequires
- no need to include malsync source any more
- correct license
- spec clean
- drop patch1 (equivalent merged upstream)
- rediff patch0
- new release 0.80


* Tue Sep 05 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.72.1-5mdv2007.0
- Patch1: fix build with pilot-link 0.12

* Sat Jul 01 2006 Stefan van der Eijk <stefan@mandriva.org> 1:0.72.1-4
- update from Cris B <cris@beebgames.com>
   - switch to gtk2

* Thu Mar 30 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1:0.72.1-3mdk
- use package libtool script

* Wed May 04 2005 Stew Benedict <sbenedict@mandriva.com> 1:0.72.1-2mdk
- fix 64bit build (P0, configure args)

* Thu Dec 18 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.72.1-1mdk
- 0.72.1

