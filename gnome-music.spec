Summary:	Music player for GNOME
Summary(pl.UTF-8):	Odtwarzacz muzyki dla GNOME
Name:		gnome-music
Version:	40.1.1
Release:	1
License:	GPL v2 with GStreamer plugins exceptions
Group:		X11/Applications/Multimedia
Source0:	https://download.gnome.org/sources/gnome-music/40/%{name}-%{version}.tar.xz
# Source0-md5:	f69650654730665cf986d7cfbd342c1b
Patch0:		%{name}-deps.patch
URL:		https://wiki.gnome.org/Apps/Music
BuildRequires:	gettext-tools
BuildRequires:	gnome-online-accounts-devel >= 3.36.0
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	grilo-devel >= 0.3.13
BuildRequires:	gtk+3-devel >= 3.24.7
BuildRequires:	libdazzle-devel >= 3.28.0
BuildRequires:	libmediaart2-devel >= 1.9.1
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.44.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-pycairo-devel >= 1.14.0
BuildRequires:	python3-pygobject3-devel >= 3.36.1
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker3-devel >= 3.0.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gdk-pixbuf2 >= 2.0
Requires:	glib2 >= 2.0
Requires:	gnome-online-accounts >= 3.36.0
Requires:	gobject-introspection >= 1.36.0
Requires:	grilo >= 0.3.13
Requires:	grilo-plugins >= 0.3.12
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
Requires:	gtk+3 >= 3.24.7
Requires:	hicolor-icon-theme
Requires:	libdazzle >= 3.28.0
Requires:	libmediaart2 >= 1.9.1
Requires:	libnotify
Requires:	pango >= 1:1.44.0
Requires:	python3-dbus
Requires:	python3-pycairo >= 1.14.0
Requires:	python3-pygobject3 >= 3.36.1
Requires:	python3-requests
Requires:	tracker3-libs >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Music is a music player for GNOME.

%description -l pl.UTF-8
GNOME Music to odtwarzacz muzyki dla GNOME.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' gnome-music.in

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc LICENSE NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-music
%dir %{_libdir}/org.gnome.Music
%attr(755,root,root) %{_libdir}/org.gnome.Music/libgd.so
%attr(755,root,root) %{_libdir}/org.gnome.Music/libgfm-0.1.so
%dir %{_libdir}/org.gnome.Music/girepository-1.0
%{_libdir}/org.gnome.Music/girepository-1.0/Gd-1.0.typelib
%{_libdir}/org.gnome.Music/girepository-1.0/Gfm-0.1.typelib
%dir %{_libdir}/org.gnome.Music/pkgconfig
%{_libdir}/org.gnome.Music/pkgconfig/gfm-0.1.pc
%{_datadir}/glib-2.0/schemas/org.gnome.Music.gschema.xml
%{_datadir}/metainfo/org.gnome.Music.appdata.xml
%{_datadir}/org.gnome.Music
%{_desktopdir}/org.gnome.Music.desktop
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Music-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Music.svg
%{py3_sitedir}/gnomemusic
