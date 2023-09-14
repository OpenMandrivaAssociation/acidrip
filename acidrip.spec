Summary:	Simple GUI for MEncoder
Name:		acidrip
Version:	0.14
Release:	10
Source:		http://prdownloads.sourceforge.net/acidrip/%{name}-%{version}.tar.bz2
URL:		https://sourceforge.net/projects/acidrip/
License:	GPL
Group:		Video
Patch0:		%{name}-0.14-xvid_options.patch
Patch1:		%{name}-0.14-mencoder.patch
Patch2:		%{name}-0.14-gtk2.patch
BuildRequires:	mencoder
BuildRequires:	lsdvd
BuildRequires:	perl-Gtk2
BuildRequires:	perl-devel
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
%autosetup -p1

perl -p -i -e 's/mp3lame/copy/g' Makefile.PL

%build
perl Makefile.PL
%make_build
										
%install
%make_install INSTALLDIRS=vendor

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=AcidRip
Comment=Video ripping and conversion
Exec=%{name}
Icon=video_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Video;AudioVideo;AudioVideoEditing;GTK;
EOF

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING TODO
%{_bindir}/%{name}
%{perl_vendorlib}/AcidRip
%{_mandir}/man1/*
%{_datadir}/applications/mandriva*
