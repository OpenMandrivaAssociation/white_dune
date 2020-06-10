Name:		white_dune
Summary:	A graphical VRML97 editor and animation tool
Version:	1.874
Release:	1
Source:		ftp://ftp.ourproject.org/pub/wdune/wdune-%{version}.tar.bz2
Patch0:		wdune-1.874-compile.patch
Group:		Graphics
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	motif-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	jdk-current
BuildRequires:	autoconf
BuildRequires:	fonts-ttf-bitstream-vera
URL:		http://wdune.ourproject.org/
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	GPLv2+
# Default editors for external bits as passed to
# configure below
Suggests:	imagemagick
Suggests:	falkon
Suggests:	krita
Suggests:	kwrite
Suggests:	kwave
Suggests:	kdenlive

%description
The dune program is a graphical VRML97 editor and animation tool.
VRML97 (Virtual Reality Modelling Language) is the ISO standard for
displaying 3D data over the web. It has support for animation, realtime
interaction and multimedia (image, movie, sound). VRML97 can be written
by popular programs like maya, catia, 3D Studio MAX, cinema4D and others.
Dune can read VRML97 files, display and let the user change the
scenegraph/fields. Some documentation how to use dune is included.
Beside some support for the VRML200x style nurbs node, dune has only a few
3D Modelling features. For artistic work, the usage of a static 3D modeller
with VRML97 export features is recommended. Examples for free/lowcost static
3D modellers available under Linux are sced, ppmodeler or ac3d.
Dune can load and store x3d (next generation VRML xml format) files,
if configured to work with the nist.gov x3d translators.
Advanced features of dune like the usage of 3Drevelator shutterglases with
the commercial Linux XIG X11 Server (DX/platium) require recompilation of
the source package.

%prep
%autosetup -p1 -n wdune-%{version}
# We patch configure.in for gomp vs. omp
autoconf
. %{_sysconfdir}/profile.d/90java.sh
%configure --with-optimization \
	--without-usrlocalinclude \
	--with-imageconverter=%{_bindir}/convert \
	--with-wwwbrowser=%{_bindir}/falkon \
	--with-imageeditor=%{_bindir}/krita \
	--with-imageeditor4kids=%{_bindir}/krita \
	--with-x11-editor=%{_bindir}/kwrite \
	--with-soundeditor=%{_bindir}/kwave \
	--with-movieeditor=%{_bindir}/kdenlive

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -s -m 755 bin/dune %{buildroot}%{_bindir}/dune
install -m 644 man/dune.1 %{buildroot}%{_mandir}/man1/dune.1

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=White Dune
Comment=A graphical VRML97 editor and animation tool
Exec=%{_bindir}/dune
Icon=graphics_section
Terminal=false
Type=Application
Categories=Graphics;3DGraphics;
EOF

%files
%defattr(-,root,root)
%doc docs
%{_bindir}/dune
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
