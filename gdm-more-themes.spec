%define	name	gdm-more-themes
%define	version 0.5
%define	release	%mkrel 4

Name:		%{name} 
Summary:	More themes for GDM
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://gnome-look.org/
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
Requires:	gdm-220
BuildArch:	noarch

%description
More themes for GDM taken from http://gnome-look.org and http://art.gnome.org

The themes included:
Crystal for Gnome - http://gnome-look.org/content/show.php?content=16332
SolarSys - http://gnome-look.org/content/show.php?content=27642
SolarSys Earth - http://gnome-look.org/content/show.php?content=28854
SolarSys Saturn - http://gnome-look.org/content/show.php?content=31709
SolarSys Mars - http://gnome-look.org/content/show.php?content=31482
Login and die -  http://gnome-look.org/content/show.php?content=13676
Core GL - http://gnome-look.org/content/show.php?content=30319
Iurana - http://gnome-look.org/content/show.php?content=16623
garGANTuan - http://gnome-look.org/content/show.php?content=28685
titan - http://gnome-look.org/content/show.php?content=17415
Crop Circles - http://art.gnome.org/themes/gdm_greeter/543
Celtic_WXGA - http://art.gnome.org/themes/gdm_greeter/1132 (widescreen)
BlueSwirl - http://gnome-look.org/content/show.php?content=30846
Raven Theme - http://gnome-look.org/content/show.php?content=31301
Insectz - http://art.gnome.org/themes/gdm_greeter/1152
GNU/Linux - http://gnome-look.org/content/show.php?content=13388
LiNsta - http://gnome-look.org/content/show.php?content=31267
Avio-GDM - http://www.gnome-look.org/content/show.php?content=37395
Relaxing - http://www.gnome-look.org/content/show.php?content=37589

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/gdm/themes/
cp -r * $RPM_BUILD_ROOT/usr/share/gdm/themes/
rm -f $RPM_BUILD_ROOT/usr/share/gdm/themes/README
# Fix all perms
for a in `find $RPM_BUILD_ROOT/usr/share/gdm/themes/ -type f` ; do chmod 644 "$a";done
for a in `find $RPM_BUILD_ROOT/usr/share/gdm/themes/ -type d` ; do chmod 755 "$a";done

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README
/usr/share/gdm/themes/*




%changelog
* Fri Aug 06 2010 Götz Waschk <waschk@mandriva.org> 0.5-4mdv2011.0
+ Revision: 566867
- depend on gdm-220 (bug #60506)

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2010.0
+ Revision: 429188
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2mdv2008.1-current
+ Revision: 140735
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 04 2007 Eskild Hustvedt <eskild@mandriva.org> 0.5-2mdv2007.0
+ Revision: 104277
- Fixed the permissions on the relaxing theme
- Import gdm-more-themes

* Sun Aug 20 2006 Eskild Hustvedt <eskild@mandriva.org> 0.5-1mdv2007.0
- Added Avio-GDM and Relaxing

* Fri Dec 16 2005 Eskild Hustvedt <eskild@mandriva.org> 0.4-1mdk
- Added SolarSys Mars, SolarSys Saturn and LiNsta

* Thu Nov 17 2005 Eskild Hustvedt <eskild@mandriva.org> 0.3-1mdk
- Added the BlueSwirl, Raven, Insectz and GNU/Linux themes.

* Sat Oct 29 2005 Eskild Hustvedt <eskild@mandriva.org> 0.2-2mdk
- Remove lila themes
- Really add the Tux Mania theme

* Fri Oct 28 2005 Eskild Hustvedt <eskild@mandriva.org> 0.2-1mdk
- Added Crop circles and Celtic_WXGA themes.

* Sun Oct 23 2005 Eskild Hustvedt <eskild@mandrake.org> 0.1-1mdk
- Initial Mandriva Linux package

