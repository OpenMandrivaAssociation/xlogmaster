%define name	xlogmaster
%define oversion	1.6.0
%define version	1.6.2
%define release	1

Summary:	Quick & easy monitoring of logfiles and devices
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libgtk+-devel
License:	GPLv2+
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

%build
%configure	--with-xlogmaster-home=%{_sysconfdir} \
		--with-xlogmaster-lib=%{_datadir}/xlogmaster \
		--with-xlogmaster-db=%{_localstatedir}/lib/xlogmaster \
		--disable-gtkrc

%make

%install
rm -rf %{buildroot}

%makeinstall XLM_LIB=%{buildroot}%{_datadir}/%{name} XLM_DB=%{buildroot}%{_localstatedir}/lib/%{name}

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Icon=%{name}
Categories=System;Monitor;
Name=%{name}
Comment=Logfile viewer
EOF

install -d %{buildroot}{%{_miconsdir},%{_liconsdir}}
tar -xOjf %{SOURCE1} icons/16x16.png > %{buildroot}%{_miconsdir}/%{name}.png
tar -xOjf %{SOURCE1} icons/32x32.png > %{buildroot}%{_iconsdir}/%{name}.png
tar -xOjf %{SOURCE1} icons/48x48.png > %{buildroot}%{_liconsdir}/%{name}.png

%post
%if %mdkversion < 200900
%{update_menus}
%endif
%__install_info %{_infodir}/%{name}.info.* %{_infodir}/dir

%preun
if [ $1 = 0 ]; then
    %__install_info --delete %{_infodir}/%{name}.info.* %{_infodir}/dir
fi

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README TODO 
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{_localstatedir}/lib/%{name}
%{_localstatedir}/lib/%{name}/*
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}.info*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop

