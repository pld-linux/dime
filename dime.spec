Summary:	DIME - DXF Import, manipulation and Export library
Summary(pl.UTF-8):   DIME - biblioteka do manipulacji plikami w formacie DXF
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
BuildRequires:	gcc-c++
BuildRequires:	tetex-dvips
BuildRequires:	tetex-fonts-ams
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-makeindex
BuildRequires:	tetex-metafont
BuildRequires:	tetex-tex-misc
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

%description -l pl.UTF-8
Dime jest biblioteką klas C++ służącą odczytywaniu, tworzeniu,
modyfikacji i zachowywaniu danych w plikach DXF. Nazwa jest skrótem od
pierwszych liter: słów DXF Import, Manipulation, and Export library.
Format pliku DXF pochodzi z AutoCAD-a, obecnie jest jednak bardzo
popularny.

Bibliotek obsługuje głównie następujące funkcje:
- ładowanie plików DXF do hierarchii obiektu dime zawierającej dane
  DXF
- budowanie hierarchii obiektów dime od zera
- ekstrakcja danych geometrycznych z hierarchii obiektów dime
- manipulacja hierarchią obiektów dime
- przegląd hierarchii obiektów dime podczas wykonywania różnych zadań
- zachowywanie obiektów hierarchii dime w postaci plików zgodnych z
  formatem DXF Oryginalnym celem dime było importowanie i eksportowanie
  plików DXF. Dlatego zaimplementowano specjalne techniki zarządzania
  pamięcią, dzięki którym można znacznie zwiększyć wydajność.

%package devel
Summary:	DIME - development files
Summary(pl.UTF-8):   DIME - część dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Dime development files.

%description devel -l pl.UTF-8
Pliki dime przeznaczone dla programistów.

%package documentation
Summary:	DIME doc
Summary(pl.UTF-8):   DIME - dokumentacja
Group:		Documentation

%description documentation
Dime documentation.

%description documentation -l pl.UTF-8
Dokumentacja dime.

%prep
%setup -q
%setup -q -D -b1

%build
%{__make} -C build \
	CC="%{__cxx}" \
	OPT="%{rpmcflags}"

%{__make} -C docs/latex refman.ps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-documentation-%{version}/{latex,html}

cp -rp include/* $RPM_BUILD_ROOT%{_includedir}
install build/libdime.a $RPM_BUILD_ROOT%{_libdir}
cp -rp docs/latex/*.tex $RPM_BUILD_ROOT%{_docdir}/%{name}-documentation-%{version}/latex
cp -rp docs/latex/*.sty $RPM_BUILD_ROOT%{_docdir}/%{name}-documentation-%{version}/latex

cp -rp docs/latex/* $RPM_BUILD_ROOT%{_docdir}/%{name}-documentation-%{version}/html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%{_libdir}/libdime.a

%files devel
%defattr(644,root,root,755)
%doc docs/latex/refman.ps ChangeLog README TODO
%{_includedir}/dime

%files documentation
%defattr(644,root,root,755)
#%doc docs/html/* docs/latex/*.tex docs/latex/*.sty
%dir %{_docdir}/%{name}-documentation-%{version}
%{_docdir}/%{name}-documentation-%{version}/latex
%{_docdir}/%{name}-documentation-%{version}/html
