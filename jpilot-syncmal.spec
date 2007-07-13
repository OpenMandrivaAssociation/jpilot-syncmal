%define version 0.80
%define release %mkrel 1
%define url http://jasonday.home.att.net/code/syncmal

Name:		jpilot-syncmal
Summary:	SyncMAL plugin for J-PILOT
Version:	%{version}
Release:	%{release}
Epoch:		1
Source:		%{url}/%{name}-%{version}.tar.gz
Source1:	malsync.tar.bz2
Patch0:		jpilot-syncmal-0.80-lib64.patch
Group:		Communications
BuildRoot:	%_tmppath/%name-%version-%release-root
License:	GPL
BuildRequires:	gtk2-devel jpilot_plugin-devel >= 0.99.6 
BuildRequires:	pilot-link-devel >= 0.11.8 chrpath
Url:		%{url}/syncmal.html

%description
SyncMAL is an interface to the command line tool malsync, a program that
synchronizes a PDA with a MAL server such as AvantGo.

See AvantGo's homepage <http://avantgo.com/> for more information on AvantGo
and MAL.

%prep

%setup -q -n %{name}-%{version} -a 1
%patch0 -p1 -b .lib64

%build
%if %_lib == lib64
  %define conf_args enable_libsuffix=64
%endif

%configure --with-mal-source=./mal %conf_args --enable-gtk2

%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
./libtool --finish %{buildroot}%{_libdir}/jpilot/plugins/
chrpath -d %{buildroot}%{_libdir}/jpilot/plugins/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog MPL-1_0.txt TODO
%_libdir/jpilot/plugins/*

