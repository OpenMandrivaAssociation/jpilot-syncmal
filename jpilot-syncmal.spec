%define name	jpilot-syncmal
%define version 0.80
%define release %mkrel 3

Name:		%{name}
Summary:	SyncMAL plugin for J-PILOT
Version:	%{version}
Release:	%{release}
Epoch:		1
Source:		http://jasonday.home.att.net/code/syncmal/%{name}-%{version}.tar.gz
Patch0:		jpilot-syncmal-0.80-lib64.patch
# disables GTK+ 1.x test in configure.in, as it trips up autoreconf
# and we're not building against GTK+ 1.x anyway - AdamW 2007/07
Patch1:		jpilot-syncmal-0.80-disable_gtk1.patch
Group:		Communications
BuildRoot:	%_tmppath/%name-%version-%release-root
License:	MPL
BuildRequires:	gtk2-devel 
BuildRequires:	jpilot_plugin-devel >= 0.99.6 
BuildRequires:	pilot-link-devel >= 0.11.8 
BuildRequires:	chrpath
BuildRequires:	libmal-devel >= 0.44
BuildRequires:	autoconf
Requires:	malsync
Url:		http://jasonday.home.att.net/code/syncmal/syncmal.html

%description
SyncMAL is an interface to the command line tool malsync, a program
that synchronizes a PDA with a MAL server such as AvantGo.

See AvantGo's homepage <http://avantgo.com/> for more information on
AvantGo and MAL.

%prep

%setup -q
%patch0 -p1 -b .lib64
%patch1 -p1 -b .gtk1

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
rm -rf $RPM_BUILD_ROOT

# this ridiculous buildsystem seems immune to sensible patching.
# it only installs stuff in libdir, so let's just set that here.
# - AdamW 2007/07
make libdir=%{buildroot}%{_libdir}/jpilot/plugins install

./libtool --finish %{buildroot}%{_libdir}/jpilot/plugins/
chrpath -d %{buildroot}%{_libdir}/jpilot/plugins/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog MPL-1_0.txt TODO
%_libdir/jpilot/plugins/*
