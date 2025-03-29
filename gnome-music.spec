Summary:	Music player for GNOME
Summary(pl.UTF-8):	Odtwarzacz muzyki dla GNOME
Name:		gnome-music
Version:	47.1
Release:	4
License:	GPL v2 with GStreamer plugins exceptions
Group:		X11/Applications/Multimedia
Source0:	https://download.gnome.org/sources/gnome-music/47/%{name}-%{version}.tar.xz
# Source0-md5:	a0fb61a60e2c67e21e1a69b8183ac155
Patch0:		%{name}-deps.patch
Patch1:		%{name}-no-update.patch
URL:		https://apps.gnome.org/Music/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.67.1
BuildRequires:	gnome-online-accounts-devel >= 3.36.0
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	grilo-devel >= 0.3.13
BuildRequires:	gtk4-devel >= 4.10.0
BuildRequires:	libadwaita-devel >= 1.5
BuildRequires:	libmediaart2-devel >= 1.9.1
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.44.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-pycairo-devel >= 1.14.0
BuildRequires:	python3-pygobject3-devel >= 3.47.0
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker3-devel >= 3.0.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.67.1
Requires(post,postun):	gtk-update-icon-cache
Requires:	gdk-pixbuf2 >= 2.0
Requires:	glib2 >= 1:2.67.1
Requires:	gnome-online-accounts >= 3.36.0
Requires:	gobject-introspection >= 1.36.0
Requires:	grilo >= 0.3.13
Requires:	grilo-plugins >= 0.3.12
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
Requires:	gtk4 >= 4.10.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.5
Requires:	libmediaart2 >= 1.9.1
Requires:	libnotify
Requires:	pango >= 1:1.44.0
Requires:	python3-dbus
Requires:	python3-pycairo >= 1.14.0
Requires:	python3-pygobject3 >= 3.47.0
Requires:	python3-requests
Requires:	tracker3-libs >= 3.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Music is a music player for GNOME.

%description -l pl.UTF-8
GNOME Music to odtwarzacz muzyki dla GNOME.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' gnome-music.in

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%{_datadir}/glib-2.0/schemas/org.gnome.Music.gschema.xml
%{_datadir}/metainfo/org.gnome.Music.appdata.xml
%{_datadir}/org.gnome.Music
%{_desktopdir}/org.gnome.Music.desktop
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Music-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Music.svg
%{py3_sitescriptdir}/gnomemusic
