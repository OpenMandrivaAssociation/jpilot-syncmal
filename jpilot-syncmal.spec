Summary:	SyncMAL plugin for J-PILOT
Name:		jpilot-syncmal
Version:	0.80
Release:	%mkrel 9
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
