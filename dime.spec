Summary:	DIME - DXF Import, manipulation and Export library.
Summary(pl):	DIME - biblioteka do manipulacji plikami w formacie DXF.
Name:		dime
Version:	0.9.1
Release:	1
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	ftp://ftp.sim.no/pub/dime/%name-%version-src.tar.bz2
Source1:	ftp://ftp.sim.no/pub/dime/%name-%version-doc.tar.bz2
#Patch:
Buildroot: /tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description
Dime is a C++ class library for reading, constructing, manipulating, and
writing DXF file data.
The name is an acronym for DXF Import, Manipulation, and Export library.
The DXF file format originates from AutoCAD, but is now in widespread use.

The focus of the library is primarily on the following items:

- loading DXF files into a dime object hierarchy containing the DXF data
- building dime object hierarchies from scratch
- extracting geometry data from dime object hierarchies
- manipulating dime object hierarchies
- traversing the dime object hierarchies while performing various tasks
- saving dime object hierarchies as files conforming to the DXF file format

The intended purpose of dime was on importing and exporting DXF files.
For this kind of usage, special memory management techniques has been
implemented, that can be used to boost the performance significantly.

%description -l pl

%package devel
Summary:	DIME devel
Summary(pl):	DIME devel
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description devel
%description -l pl devel

%package documentation
Summary:	DEME doc
Summary(pl):	DIME doc
Group:		Documentation/Libraries
Group(pl):	Dokumentacja/Biblioteki

%description documentation
%description -l pl documentation

%prep
%setup -q
%setup -q -D -b1

%build
cd build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
cd ../docs/latex
make refman.ps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install -d $RPM_BUILD_ROOT/%{datadir}/doc/%name-documentation-%version/{latex,html}

cp -rp include/* $RPM_BUILD_ROOT%{_includedir}
install -s build/libdime.a $RPM_BUILD_ROOT%{_libdir}
cp -rp docs/latex/*.tex $RPM_BUILD_ROOT/%{datadir}/doc/%name-documentation-%version/latex
cp -rp docs/latex/*.sty $RPM_BUILD_ROOT/%{datadir}/doc/%name-documentation-%version/latex

cp -rp docs/latex/*  $RPM_BUILD_ROOT/%{datadir}/doc/%name-documentation-%version/html

bzip2 -9 README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc
%attr(644,root,root) %{_libdir}/libdime.a

%files devel
%defattr(644, root, root, 755)
%doc docs/latex/refman.ps ChangeLog.bz2 README.bz2 TODO.bz2
%{_includedir}/dime/

%files documentation
%defattr(644,root,root,755)
#%doc docs/html/* docs/latex/*.tex docs/latex/*.sty
%attr(644,root,root) /%{datadir}/doc/%name-documentation-%version/latex
%attr(644,root,root) /%{datadir}/doc/%name-documentation-%version/html
