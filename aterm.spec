%define tar_version 1.0.1

%define Summary An rxvt-based terminal emulator for X11

Summary:	%{Summary}
Name:		aterm
Version:	1.0.1
Release:	9
URL:		http://aterm.sourceforge.net
Source0:	ftp://ftp.afterstep.org/apps/aterm/%{name}-%{tar_version}.tar.bz2
License:	GPLv2+
Group:		Terminals

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xt)

%description
Aterm is a colour vt102 terminal emulator based on rxvt 2.4.8 intended as an 
xterm replacement for users who do not require features such as Tektronix 4014 
emulation and toolkit style configurability

%prep
%setup -q -n %{name}-%{tar_version}

%build
%configure2_5x --enable-fading --enable-background-image
%make

%install
rm -Rf $RPM_BUILD_ROOT

%makeinstall mandir=$RPM_BUILD_ROOT/%{_mandir}/man1/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name} -name Terminal
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Terminals;TerminalEmulator;System;
EOF

%clean
rm -fr $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root,0755)
%doc INSTALL ChangeLog doc/README.* %{name}.lsm README.configure 
%doc doc/FAQ doc/ChangeLog.rxvt
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/*


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.0.1-8mdv2011.0
+ Revision: 635067
- BR xt
- rebuild
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2011.0
+ Revision: 616628
- the mass rebuild of 2010.0 packages

* Fri May 15 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0.1-6mdv2010.0
+ Revision: 376275
- Fix license (GPLv2+) and URL
- Use configure2_5x
- Comestic changes for specfile policy

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.0.1-5mdv2009.0
+ Revision: 218439
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.1-5mdv2008.1
+ Revision: 140690
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Thu Aug 02 2007 Funda Wang <fwang@mandriva.org> 1.0.1-5mdv2008.0
+ Revision: 58135
- Kill patch, merged upstream
- New version 1.0.1


* Tue Jan 30 2007 Olivier Blin <oblin@mandriva.com> 1.0-5mdv2007.0
+ Revision: 115297
- really remove xvt alternative
- cosmetics
- remove debian-style menu entry
- fix XDG menu comment
- fix typo in menu entry (#25265 continued)
- Import aterm

* Thu Sep 07 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.0-4mdv2007.0
- Fix XDG menu ( bug #25265)

* Tue Aug 01 2006 Lenny Cartier <lenny@mandriva.com> 1.0-3mdv2007.0
- xdg

* Fri Nov 04 2005 Michael Scherer <misc@mandriva.org> 1.0-2mdk
- mkrel
- fix debug output by commenting the line ( patch0, bug 18194 )

* Wed Jul 06 2005 Michael Scherer <misc@mandriva.org> 1.0-1mdk
- New release 1.00

* Sat Jun 18 2005 Olivier Blin <oblin@mandriva.com> 1.0-0.beta4.1mdk
- beta4

* Sat Jun 04 2005 Michael Scherer <misc@mandriva.org> 1.0-0.beta3.1mdk
- beta3
- remove patch0

* Sat Mar 12 2005 Michael Scherer <misc@mandrake.org> 1.0-0.beta2.2mdk
- remove alternatives

* Fri Jan 21 2005 Michael Scherer <misc@mandrake.org> 1.0-0.beta2.1mdk
- 1.0.beta2
- use macro

* Wed Jan 12 2005 Michael Scherer <misc@mandrake.org> 1.0-0.beta1.1mdk
- 1.0.beta1

* Sat May 22 2004 Michael Scherer <misc@mandrake.org> 0.4.2-5mdk 
- fix #1496, add doc

* Tue Apr 20 2004 Michael Scherer <misc@mandrake.org> 0.4.2-4mdk 
- Rebuild

