Summary:	Music player for GNOME
Name:		gnome-music
Version:	3.14.2
Release:	1
License:	GPL v2 with exceptions
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-music/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	8bd303572780ae0861dddb00033f5a55
URL:		http://wiki.gnome.org/Apps/Music
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	grilo-devel >= 0.2.6
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libmediaart-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 3.3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	grilo-plugins
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
Requires:	gtk+3 >= 3.14.0
Requires:	hicolor-icon-theme
Requires:	libnotify
Requires:	python3-dbus
Requires:	python3-pycairo
Requires:	python3-pygobject3
Requires:	tracker-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Music is a music player for GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-music/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-music
%dir %{_libdir}/gnome-music
%dir %{_libdir}/gnome-music/girepository-1.0
%{_libdir}/gnome-music/girepository-1.0/Gd-1.0.typelib
%attr(755,root,root) %{_libdir}/gnome-music/libgd.so
%{_datadir}/appdata/gnome-music.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Music.gschema.xml
%{_datadir}/gnome-music
%{_desktopdir}/gnome-music.desktop
%{_iconsdir}/HighContrast/*/*/gnome-music.png
%{_iconsdir}/hicolor/*/*/gnome-music.png
%{_mandir}/man1/gnome-music.1*
%{py3_sitescriptdir}/gnomemusic
