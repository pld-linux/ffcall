Summary:	Libraries for building foreign function call interfaces
Summary(pl):	Biblioteki do tworzenia interfejsów wywo³añ obcych funkcji
Name:		ffcall
Version:	1.10
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.santafe.edu/pub/gnu/%{name}-%{version}.tar.gz
# Source0-md5:	2db95007e901f3bc2ae7e5a9fe9ebea4
URL:		http://www.haible.de/bruno/packages-ffcall.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:
- avcall - calling C functions with variable arguments
- vacall - C functions accepting variable argument prototypes
- trampoline - closures as first-class C functions
- callback - closures with variable arguments as first-class C
  functions (a reentrant combination of vacall and trampoline)

This version B includes some minor configuration changes so that files
are installed in the proper place. Also it compiles on cygwin and
mingw32.

%description -l pl
To jest zestaw czterech bibliotek, których mo¿na u¿yæ do tworzenia
interfejsów wywo³añ obcych procedur we wbudowanych interpreterach.

Te cztery pakiety to:
- avcall - wywo³ywanie funkcji w C ze zmiennymi argumentami
- vacall - funkcje w C akceptuj±ce prototypy ze zmiennymi argumentami
- trampoline - domkniêcia jako funkcje C pierwszej klasy
- callback - domkniêcia ze zmiennymi argumentami jako funkcje C
  pierwszej klasy (zagnie¿d¿alna kombinacja vacall i trampoline)

Ta wersja B zawiera trochê ma³ych zmian w konfiguracji, dziêki którym
pliki instaluj± siê we w³a¶ciwych miejscach. A tak¿e kompiluje siê pod
cygwinem i mingw32.

%package devel
Summary:	Development files for ffcall libraries
Summary(pl):	Pliki dla programistów u¿ywaj±cych bibliotek ffcall
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files for ffcall libraries: headers and static trampoline
and vacall libraries.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych bibliotek ffcall: nag³ówki i
statyczne biblioteki trampoline oraz vacall.

%package static
Summary:	Static versions of avcall and callback libraries
Summary(pl):	Statyczne wersje bibliotek avcall i callback
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static versions of avcall and callback libraries.

%description static -l pl
Statyczne wersje bibliotek avcall i callback.

%prep
%setup -q

%build
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -r $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc */*.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/libtrampoline.a
%{_libdir}/libvacall.a
%{_includedir}/*
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libavcall.a
%{_libdir}/libcallback.a
