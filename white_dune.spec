%define patch	14

Name:		white_dune
Summary:	A graphical VRML97 editor and animation tool
Version:	0.28
Release:	%mkrel 1.pl%{patch}.2
Source:		http://129.69.35.12/dune/%{name}-%{version}pl%{patch}.tar.gz
Patch0:		white_dune_missing_includes.patch
Group:		Graphics
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	xlsfonts
BuildRequires:	lesstif-devel
BuildRequires:	mesaglu-devel
BuildRequires:	libxi-devel
BuildRequires:	libxmu-devel
URL:		http://www.csv.ica.uni-stuttgart.de/vrml/dune
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	GPLv2+

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
rm -rf %{buildroot}
%setup -q -n %{name}-%{version}pl%{patch}
%patch0 -p 1

%build
%configure --with-optimization --with-buginlesstif

rm Makefile
cd src && make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -s -m 755 bin/dune %{buildroot}%{_bindir}/dune
install -m 644 man/dune.1 %{buildroot}%{_mandir}/man1/dune.1


#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A graphical VRML97 editor and animation tool
Exec=%{_bindir}/dune
Icon=graphics_section
Terminal=false
Type=Application
Categories=Graphics;3DGraphics;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs
%{_bindir}/dune
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
