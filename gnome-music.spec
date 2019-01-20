Summary:	Music player for GNOME
Summary(pl.UTF-8):	Odtwarzacz muzyki dla GNOME
Name:		gnome-music
Version:	3.30.2
Release:	1
License:	GPL v2 with exceptions
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-music/3.30/%{name}-%{version}.tar.xz
# Source0-md5:	2f12c025cf5d2ca9a22704ba491f50aa
URL:		http://wiki.gnome.org/Apps/Music
BuildRequires:	gettext-tools
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	grilo-devel >= 0.3.4
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libmediaart2-devel >= 1.9.1
BuildRequires:	meson
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-pycairo-devel >= 1.14.0
BuildRequires:	python3-pygobject3-devel >= 3.22
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 2.0.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	grilo >= 0.3.4
Requires:	grilo-plugins >= 0.3.1
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
Requires:	gtk+3 >= 3.20.0
Requires:	hicolor-icon-theme
Requires:	libmediaart2 >= 1.9.1
Requires:	libnotify
Requires:	python3-dbus
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.22
Requires:	python3-requests
Requires:	tracker-libs >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Music is a music player for GNOME.

%description -l pl.UTF-8
GNOME Music to odtwarzacz muzyki dla GNOME.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,/usr/bin/python3,' gnome-music.in

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang org.gnome.Music --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f org.gnome.Music.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-music
%dir %{_libdir}/org.gnome.Music
%dir %{_libdir}/org.gnome.Music/girepository-1.0
%{_libdir}/org.gnome.Music/girepository-1.0/Gd-1.0.typelib
%attr(755,root,root) %{_libdir}/org.gnome.Music/libgd.so
%{_datadir}/metainfo/org.gnome.Music.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Music.gschema.xml
%{_datadir}/org.gnome.Music
%{_desktopdir}/org.gnome.Music.desktop
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Music-symbolic.svg
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Music.png
%{py3_sitedir}/gnomemusic
