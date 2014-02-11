Summary:	An rxvt-based terminal emulator for X11
Name:		aterm
Version:	1.0.1
Release:	10
License:	GPLv2+
Group:		Terminals
Url:		http://aterm.sourceforge.net
Source0:	ftp://ftp.afterstep.org/apps/aterm/%{name}-%{version}.tar.bz2
Patch0:		aterm-1.0.1-no-strip.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xt)

%description
Aterm is a colour vt102 terminal emulator based on rxvt 2.4.8 intended as an 
xterm replacement for users who do not require features such as Tektronix 4014 
emulation and toolkit style configurability

%files
%doc ChangeLog doc/README.* %{name}.lsm README.configure
%doc doc/FAQ doc/ChangeLog.rxvt
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--enable-fading \
	--enable-background-image
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=An rxvt-based terminal emulator for X11
Exec=%{name} -name Terminal
Icon=%{name}
Terminal=false
Type=Application
Categories=TerminalEmulator;System;
EOF

