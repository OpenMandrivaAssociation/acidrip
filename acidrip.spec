%define name	acidrip
%define version	0.14
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Simple GUI for MEncoder
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/acidrip/%{name}-%{version}.tar.bz2
URL:		http://untrepid.com/acidrip
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	mencoder
BuildRequires:  lsdvd
BuildRequires:  perl-Gtk2
BuildRequires:  perl-devel
Requires:	lsdvd
Requires:	mencoder
Requires:	perl-Gtk2
Provides:	perl(AcidRip::acidrip) perl(AcidRip::DVDInfo)
Provides:	perl(AcidRip::interface) perl(AcidRip::signals)
Provides:	perl(AcidRip::messages)
BuildArch:	noarch

%description
AcidRip is a Gtk::Perl application for ripping and encoding DVD's. It neatly
wraps MPlayer and MEncoder, which I think is pretty handy, seeing as MPlayer
is by far the best bit of video playing kit around for Linux. As well as
creating a simple Graphical Interface for those scared of getting down and
dirty with MEncoders command line interface, It also automates the process in
a number of ways:
    * Parses DVD into contents tree
    * Finds longest title
    * Calculate video bitrate for given filesize
    * Finds black bands and crops them
    * Gives suggestions for improved performance
    * Other stuff!

%prep
%setup -q
perl -p -i -e 's/mp3lame/copy/g' Makefile.PL

%build
perl Makefile.PL
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std INSTALLDIRS=vendor

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="video_section.png" needs="x11" title="AcidRip" longtitle="Video ripping and conversion" section="Multimedia/Video" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=AcidRip
Comment=Video ripping and conversion
Exec=%{name}
Icon=video_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;Video;AudioVideo;AudioVideoEditing;GTK;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING TODO
%{_bindir}/%name
%{perl_vendorlib}/AcidRip
%{_mandir}/man1/*
%_datadir/applications/mandriva*
%{_menudir}/%name
