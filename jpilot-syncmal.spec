Summary:	SyncMAL plugin for J-PILOT
Name:		jpilot-syncmal
Epoch:		1
Version:	0.80
Release:	12
License:	MPL
Group:		Communications
Url:		http://jasonday.home.att.net/code/syncmal/syncmal.html
Source0:	http://jasonday.home.att.net/code/syncmal/%{name}-%{version}.tar.gz
Patch0:		jpilot-syncmal-0.80-lib64.patch
# disables GTK+ 1.x test in configure.in, as it trips up autoreconf
# and we're not building against GTK+ 1.x anyway - AdamW 2007/07
Patch1:		jpilot-syncmal-0.80-disable_gtk1.patch
Patch2:		jpilot-syncmal-0.80-libtool_fixes.diff
Patch3:		jpilot-syncmal-0.80-automake1.13.patch

BuildRequires:	jpilot-devel >= 0.99.6 
BuildRequires:	libmal-devel >= 0.44
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pilot-link)
Requires:	jpilot >= 0.99.6 
Requires:	malsync

%description
SyncMAL is an interface to the command line tool malsync, a program
that synchronizes a PDA with a MAL server such as AvantGo.

See AvantGo's homepage <http://avantgo.com/> for more information on
AvantGo and MAL.

%prep

%setup -q
%apply_patches

# needed by autoreconf
cp MPL-1_0.txt COPYING
touch NEWS
touch AUTHORS

# needed by patch0
AUTOMAKE="automake --add-missing" autoreconf

%build
%configure \
	--disable-static \
	--enable-gtk2

%make 

%install
# this ridiculous buildsystem seems immune to sensible patching.
# it only installs stuff in libdir, so let's just set that here.
# - AdamW 2007/07
%makeinstall libdir=%{buildroot}%{_libdir}/jpilot/plugins

%files
%doc ChangeLog MPL-1_0.txt TODO
%{_libdir}/jpilot/plugins/libsyncmal.so

