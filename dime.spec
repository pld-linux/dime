Summary:	DIME - DXF Import, manipulation and Export library
Summary(pl.UTF-8):	DIME - biblioteka do manipulacji plikami w formacie DXF
Name:		dime
Version:	0.9.1
Release:	5
License:	GPL v2
Group:		Libraries
# original source (no lonver available): ftp://ftp.sim.no/pub/dime/
# now available at https://github.com/coin3d/dime, last tagged version is 0.9.1
Source0:	%{name}-%{version}-src.tar.bz2
# Source0-md5:	142af240cd35508d606917a38164c759
Source1:	%{name}-%{version}-doc.tar.bz2
# Source1-md5:	994706320ce7d222a1597913ba0cbee0
Patch0:		%{name}-c++.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-doc.patch
URL:		https://github.com/coin3d/dime
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	rpm-build >= 4.6
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
  formatem DXF

Pierwotnym celem dime było importowanie i eksportowanie plików DXF.
Dlatego zaimplementowano specjalne techniki zarządzania pamięcią,
dzięki którym można znacznie zwiększyć wydajność.

%package devel
Summary:	Header files for DIME
Summary(pl.UTF-8):	Pliki nagłówkowe DIME
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for DIME.

%description devel -l pl.UTF-8
Pliki nagłówkowe DIME.

%package static
Summary:	Static DIME library
Summary(pl.UTF-8):	Statyczna biblioteka DIME
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static DIME library.

%description static -l pl.UTF-8
Statyczna biblioteka DIME.

%package apidocs
Summary:	API documentation for DIME library
Summary(pl.UTF-8):	Dokumentacja API biblioteki DIME
Group:		Documentation
Obsoletes:	dime-documentation < 0.9.1-5
BuildArch:	noarch

%description apidocs
API documentation for DIME library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki DIME.

%prep
%setup -q -b1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} -C build libdime.la \
	CC="%{__cxx}" \
	OPT="%{rpmcxxflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -pr include/* $RPM_BUILD_ROOT%{_includedir}
libtool --mode=install install build/libdime.la $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libdime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdime.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdime.so
%{_libdir}/libdime.la
%{_includedir}/dime

%files static
%defattr(644,root,root,755)
%{_libdir}/libdime.a

%files apidocs
%defattr(644,root,root,755)
%doc docs/html/*
