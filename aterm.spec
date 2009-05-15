%define tar_version 1.0.1

%define Summary An rxvt-based terminal emulator for X11

Summary:	%{Summary}
Name:		aterm
Version:	1.0.1
Release:	%mkrel 6
URL:		http://aterm.sourceforge.net
Source0:	ftp://ftp.afterstep.org/apps/aterm/%{name}-%{tar_version}.tar.bz2
License:	GPLv2+
Group:		Terminals

BuildRequires:	X11-devel
BuildRequires:	xpm-devel
BuildRoot:	%_tmppath/%name-%version-%release-root

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
