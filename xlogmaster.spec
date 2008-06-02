%define name	xlogmaster
%define version	1.6.0
%define release	%mkrel 12

Summary:	Quick & easy monitoring of logfiles and devices
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.gnu.org/xlogmaster/%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}-extra.tar.bz2
Source2:	%{name}-icons.tar.bz2
Patch0:		%{name}-gcc3.2.fix.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libgtk+-devel
License:	GPL
URL:		http://www.gnu.org/software/xlogmaster/
Group:		Monitoring

%description
The Xlogmaster is a program that allows easy and flexible monitoring of
all logfiles and devices that allow being read via cat (like the /proc
devices). It allows you to set a lot of events based on certain activities
in the monitored logfiles/devices and should prove very helpful for almost
anyone.

%prep

%setup -q -T -b 0 -n %{name}-%{version}
%setup -q -T -D -a 1
%patch0 -p1

%build
%configure	--with-xlogmaster-home=%{_sysconfdir} \
		--with-xlogmaster-lib=%{_datadir}/xlogmaster \
		--with-xlogmaster-db=%{_localstatedir}/lib/xlogmaster \
		--disable-gtkrc

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall XLM_LIB=%{buildroot}%{_datadir}/xlogmaster XLM_DB=%{buildroot}%{_localstatedir}/lib/xlogmaster

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Icon=%{name}
Categories=System;Monitor;
Name=Xlogmaster
Comment=Logfile viewer
EOF

#cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
#[Desktop Entry]
#Type=Application
#Exec=%{name} -terse##
#Categories=Documentation/Websites#
#Name=Xlogmaster Homepage#
#Exec=www-browser %{url}
#EOF

install -d ${RPM_BUILD_ROOT}{%{_miconsdir},%{_liconsdir}}
tar -xOjf %{SOURCE2} icons/16x16.png > ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
tar -xOjf %{SOURCE2} icons/32x32.png > ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
tar -xOjf %{SOURCE2} icons/48x48.png > ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

%post
%{update_menus}
%__install_info %{_infodir}/xlogmaster.info.* %{_infodir}/dir

%preun
if [ $1 = 0 ]; then
    %__install_info --delete %{_infodir}/xlogmaster.info.* %{_infodir}/dir
fi

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING NEWS README TODO doc/old-tutorial.txt.gz %{name}-%{version}-extra/*.html
%{_bindir}/*
%dir %{_datadir}/xlogmaster
%{_datadir}/xlogmaster/*
%dir %{_localstatedir}/lib/xlogmaster
%{_localstatedir}/lib/xlogmaster/*
%{_mandir}/man1/xlogmaster.1*
%{_infodir}/xlogmaster.info*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

