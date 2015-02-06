Summary:	Quick & easy monitoring of logfiles and devices
Name:		xlogmaster
Version:	1.6.2
Release:	3
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
Patch0:		xlogmaster-1.6.2-workaround-pointer-to-int-casting.patch
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
%setup -q -a1
%patch0 -p1 -b .cast~

%build
%configure	--with-xlogmaster-home=%{_sysconfdir} \
		--with-xlogmaster-lib=%{_datadir}/xlogmaster \
		--with-xlogmaster-db=%{_localstatedir}/lib/xlogmaster \
		--disable-gtkrc

%make

%install
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

install -m644 icons/16x16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 icons/32x32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 icons/48x48.png -D %{buildroot}%{_liconsdir}/%{name}.png



%files
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


%changelog
* Fri Jan 13 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1.6.2-1
+ Revision: 760690
- workaround casting from pointer to int breaking build on 64 bit (P0)
- don't redefine name, version & release
- use %%_install_info macros
- drop legacy rpm stuff
- drop conditional scripts for ancient releases
- install icons a bit nicer.. ;)

  + Johnny A. Solbu <solbu@mandriva.org>
    - Remove obsolete html docs.
    - New version
    - Spec cleanup
    - Don't ship COPYING, as the license doesn't require it.
    - Replaced $$RPM_BUILD_ROOT with %%{buildroot}
    - Removed %%mkrel
    - Removed broken patch.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix summary-ended-with-dot
    - auto convert menu to XDG
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import xlogmaster

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Fri Jul 16 2004 Michael Scherer <misc@mandrake.org> 1.6.0-12mdk 
- rebuild for new gcc

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com 1.6.0-11mdk
- rebuild

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 1.6.0-10mdk
- rebuild

* Sat Nov 23 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.6.0-9mdk
- fix missing files

* Thu Nov 14 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.6.0-8mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- gcc-3.2 compilation fixes
	- Cleanups
	- s/Copyright/License/ - Do not use obsolete Copyright tag
	- Removed redundant PreReq
	- Added missing BuildRequires
	- Moved xlogmaster-lib files into a more appropriate place(make rpmlint happy)

* Thu Oct 24 2002 Maxim Heijndijk <cchq@wanadoo.nl> 1.6.0-7mdk
- Rebuilt for Mandrake 9.0 / MandrakeClub.
- Added BuildRequires for gcc 2.96.
- Fixed bindir.
- Fixed datbase dir.
- Fixed manfile permissions.
- Removed gtkrc files.

* Sat Oct 12 2002 Maxim Heijndijk <cchq@wanadoo.nl> 1.6.0-6
- Fixed Group.

* Mon Oct 07 2002 Maxim Heijndijk <cchq@wanadoo.nl> 1.6.0-5
- Rebuilt for MandrakeClub.

* Mon May 07 2001 Maxim Heijndijk <cchq@wanadoo.nl> 1.6.0-4
- Rebuild with glibc-2.2.2.
- More docs.

* Wed Aug 23 2000 Maxim Heijndijk <cchq@wanadoo.nl> 1.6.0-3
- Added menuentryfile
- Bzipping/stripping now handled by spec-helper
- Manpages to %%{_mandir}

* Tue Jun 20 2000 Maxim Heijndijk <cchq@wanadoo.nl> 1.6.0-2
- Made package relocatable
- bzipped source
- bzipped manpage

* Fri Apr 02 1999 Arne Coucheron <arneco@online.no> [1.6.0-1]
- corrected source url
- requires GTK+ >= 1.2.1
- sound, script and database files moved to /usr/lib/xlogmaster
- strip the binary

* Wed Aug 26 1998 Arne Coucheron <arneco@online.no> [1.4.3-1]
- installing the info file

* Mon Jul 27 1998 Arne Coucheron <arneco@online.no> [1.4.1-1]
- first release
