Summary:	Simple GUI for MEncoder
Name:		acidrip
Version:	0.14
Release:	9
Source:		http://prdownloads.sourceforge.net/acidrip/%{name}-%{version}.tar.bz2
URL:		http://untrepid.com/acidrip
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

perl -p -i -e 's/mp3lame/copy/g' Makefile.PL

%build
perl Makefile.PL
%make
										
%install
rm -rf %{buildroot}

%makeinstall_std INSTALLDIRS=vendor

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

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif
		
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING TODO
%{_bindir}/%{name}
%{perl_vendorlib}/AcidRip
%{_mandir}/man1/*
%{_datadir}/applications/mandriva*


%changelog
* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.14-8mdv2010.0
+ Revision: 423862
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.14-7mdv2009.0
+ Revision: 218436
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.14-7mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jul 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.14-7mdv2008.0
+ Revision: 56365
- provide Gtk2 patch

* Mon Jul 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.14-6mdv2008.0
+ Revision: 52453
- provide patch 0 (default xvid options)
- provide patch 1 (mencoder new crop syntax)
- drop old menu style
- remove X-MandrivaLinux from desktop file
- Import acidrip



* Wed Aug  2 2006 Götz Waschk <waschk@mandriva.org> 0.14-5mdv2007.0
- xdg menu

* Tue Jun 27 2006 Lenny Cartier <lenny@mandriva.com> 0.14-4mdv2007.0
- rebuild

* Fri Feb 17 2006 Götz Waschk <waschk@mandriva.org> 0.14-3mdk
- fix installation

* Tue Nov 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.14-2mdk
- fix provides

* Mon Nov 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.14-1mdk
- fix URL
- new version

* Tue Jan 27 2004 Götz Waschk <waschk@linux-mandrake.com> 0.12-1mdk
- new version

* Tue Nov 11 2003 Götz Waschk <waschk@linux-mandrake.com> 0.11-1mdk
- this one needs perl-Gtk2
- new version

* Wed Jul 16 2003 Götz Waschk <waschk@linux-mandrake.com> 0.9-3mdk
- fix buildrequires again

* Tue Jul 15 2003 Götz Waschk <waschk@linux-mandrake.com> 0.9-2mdk
- fix buildrequires

* Mon Jun 2 2003 Austin Acton <aacton@yorku.ca> 0.9-1mdk
- 0.9

* Fri May 30 2003 Austin Acton <aacton@yorku.ca> 0.8-1mdk
- initial package
