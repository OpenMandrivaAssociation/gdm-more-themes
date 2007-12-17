%define	name	gdm-more-themes
%define	version 0.5
%define rel	2
%define	release	%mkrel %rel

Name:		%{name} 
Summary:	More themes for GDM
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://gnome-look.org/
Group:		Graphical desktop/GNOME
License:	GPL
Requires:	gdm
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


