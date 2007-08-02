%define tar_version 1.0.1

%define Summary An rxvt-based terminal emulator for X11

Summary:	%{Summary}
Name:		aterm
Version: 1.0.1
Release:    %mkrel 5
Url:		http://download.sourceforge.net/aterm/
Source0:	ftp://ftp.afterstep.org/apps/aterm/%{name}-%{tar_version}.tar.bz2
Patch0:     aterm-1.0.0-no_debug_output.patch 
License:	GPL
Group:		Terminals
BuildRequires:	XFree86-devel xpm-devel
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
Aterm is a colour vt102 terminal emulator based on rxvt 2.4.8 intended as an 
xterm replacement for users who do not require features such as Tektronix 4014 
emulation and toolkit style configurability

%prep
%setup -q -n %{name}-%{tar_version}
#patch0

%build
%configure --enable-fading --enable-background-image
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

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,0755)
%doc INSTALL ChangeLog doc/README.* %{name}.lsm README.configure 
%doc doc/FAQ doc/ChangeLog.rxvt
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/*
