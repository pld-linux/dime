Summary:	DIME - DXF Import, manipulation and Export library.
Summary(pl):	DIME - biblioteka do manipulacji plikami w formacie DXF.
Name:		dime
Version:	0.9.1
Release:	3
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.sim.no/pub/dime/%name-%version-src.tar.bz2
Source1:	ftp://ftp.sim.no/pub/dime/%name-%version-doc.tar.bz2
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
Dime jest bibliotek± klas C++ s≥uø±c± odczytywaniu, tworzeniu,
modyfikacji i zachowywaniu danych w plikach DXF. Nazwa jest skrÛtem od
pierwszych liter: s≥Ûw DXF Import, Manipulation, and Export library.
Format pliku DXF pochodzi z AutoCAD-a, obecnie jest jednak bardzo
popularny.

Bibliotek obs≥uguje g≥Ûwnie nastÍpuj±ce funkcje:
- ≥adowanie plikÛw DXF do hierarchii obiektu dime zawieraj±cej dane
  DXF
- budowanie hierarchii obiektÛw dime od zera
- ekstrakcja danych geometrycznych z hierarchii obiektÛw dime
- manipulacja hierarchi± obiektÛw dime
- przegl±d hierarchii obiektÛw dime podczas wykonywania rÛønych zadaÒ
- zachowywanie obiektÛw hierarchii dime w postaci plikÛw zgodnych z
  formatem DXF Oryginalnym celem dime by≥o importowanie i eksportowanie
  plikÛw DXF. Dlatego zaimplementowano specjalne techniki zarz±dzania
  pamiÍci±, dziÍki ktÛrym moøna znacznie zwiÍkszyÊ wydajno∂Ê.

%package devel
Summary:	DIME devel
Summary(pl):	DIME - czÍ∂Ê dla programistÛw
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel

%description -l pl devel

%package documentation
Summary:	DIME doc
Summary(pl):	DIME - dokumentacja
Group:		Documentation
Group(de):	Dokumentation
Group(es):	DocumentaciÛn
Group(pl):	Dokumentacja

%description documentation

%description -l pl documentation

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
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install -d $RPM_BUILD_ROOT/%{datadir}/doc/%name-documentation-%version/{latex,html}

cp -rp include/* $RPM_BUILD_ROOT%{_includedir}
install build/libdime.a $RPM_BUILD_ROOT%{_libdir}
cp -rp docs/latex/*.tex $RPM_BUILD_ROOT/%{datadir}/doc/%name-documentation-%version/latex
cp -rp docs/latex/*.sty $RPM_BUILD_ROOT/%{datadir}/doc/%name-documentation-%version/latex

cp -rp docs/latex/*  $RPM_BUILD_ROOT/%{datadir}/doc/%name-documentation-%version/html

gzip -9nf README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(644,root,root) %{_libdir}/libdime.a

%files devel
%defattr(644,root,root,755)
%doc docs/latex/refman.ps ChangeLog.gz README.gz TODO.gz
%{_includedir}/dime/

%files documentation
%defattr(644,root,root,755)
#%doc docs/html/* docs/latex/*.tex docs/latex/*.sty
%attr(644,root,root) /%{datadir}/doc/%name-documentation-%version/latex
%attr(644,root,root) /%{datadir}/doc/%name-documentation-%version/html
