Summary:	DIME - DXF Import, manipulation and Export library
Summary(pl):	DIME - biblioteka do manipulacji plikami w formacie DXF
Name:		dime
Version:	0.9.1
Release:	3
License:	GPL
Group:		Libraries
# Old site:	ftp://ftp.sim.no/pub/dime/
# New site(?):	http://download.berlios.de/cad2octree/
Source0:	%{name}-%{version}-src.tar.bz2
# Source0-md5:	142af240cd35508d606917a38164c759
Source1:	%{name}-%{version}-doc.tar.bz2
# Source1-md5:	994706320ce7d222a1597913ba0cbee0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dime is a C++ class library for reading, constructing, manipulating,
and writing DXF file data. The name is an acronym for DXF Import,
Manipulation, and Export library. The DXF file format originates from
AutoCAD, but is now in widespread use.

The focus of the library is primarily on the following items:

- loading DXF files into a dime object hierarchy containing the DXF
  data
- building dime object hierarchies from scratch
- extracting geometry data from dime object hierarchies
- manipulating dime object hierarchies
- traversing the dime object hierarchies while performing various
  tasks
- saving dime object hierarchies as files conforming to the DXF file
  format

The intended purpose of dime was on importing and exporting DXF files.
For this kind of usage, special memory management techniques has been
implemented, that can be used to boost the performance significantly.

%description -l pl
Dime jest bibliotek± klas C++ s³u¿±c± odczytywaniu, tworzeniu,
modyfikacji i zachowywaniu danych w plikach DXF. Nazwa jest skrótem od
pierwszych liter: s³ów DXF Import, Manipulation, and Export library.
Format pliku DXF pochodzi z AutoCAD-a, obecnie jest jednak bardzo
popularny.

Bibliotek obs³uguje g³ównie nastêpuj±ce funkcje:
- ³adowanie plików DXF do hierarchii obiektu dime zawieraj±cej dane
  DXF
- budowanie hierarchii obiektów dime od zera
- ekstrakcja danych geometrycznych z hierarchii obiektów dime
- manipulacja hierarchi± obiektów dime
- przegl±d hierarchii obiektów dime podczas wykonywania ró¿nych zadañ
- zachowywanie obiektów hierarchii dime w postaci plików zgodnych z
  formatem DXF Oryginalnym celem dime by³o importowanie i eksportowanie
  plików DXF. Dlatego zaimplementowano specjalne techniki zarz±dzania
  pamiêci±, dziêki którym mo¿na znacznie zwiêkszyæ wydajno¶æ.

%package devel
Summary:	DIME devel
Summary(pl):	DIME - czê¶æ dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Dime developement files.

%description devel -l pl
Pliki developerskie do dime.

%package documentation
Summary:	DIME doc
Summary(pl):	DIME - dokumentacja
Group:		Documentation

%description documentation
Dime documentation.

%description documentation -l pl
Dokumentacja dime.

%prep
%setup -q
%setup -q -D -b1

%build
cd build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"
cd ../docs/latex
%{__make} refman.ps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT%{datadir}/doc/%{name}-documentation-%{version}/{latex,html}

cp -rp include/* $RPM_BUILD_ROOT%{_includedir}
install build/libdime.a $RPM_BUILD_ROOT%{_libdir}
cp -rp docs/latex/*.tex $RPM_BUILD_ROOT%{datadir}/doc/%{name}-documentation-%{version}/latex
cp -rp docs/latex/*.sty $RPM_BUILD_ROOT%{datadir}/doc/%{name}-documentation-%{version}/latex

cp -rp docs/latex/* $RPM_BUILD_ROOT%{datadir}/doc/%{name}-documentation-%{version}/html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(644,root,root) %{_libdir}/libdime.a

%files devel
%defattr(644,root,root,755)
%doc docs/latex/refman.ps ChangeLog.gz README.gz TODO.gz
%{_includedir}/dime/

%files documentation
%defattr(644,root,root,755)
#%doc docs/html/* docs/latex/*.tex docs/latex/*.sty
%attr(644,root,root) /%{datadir}/doc/%{name}-documentation-%{version}/latex
%attr(644,root,root) /%{datadir}/doc/%{name}-documentation-%{version}/html
