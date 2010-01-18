%define		snap	20090629

Summary:	Libraries for building foreign function call interfaces
Summary(pl.UTF-8):	Biblioteki do tworzenia interfejsów wywołań obcych funkcji
Name:		ffcall
Version:	1.11
Release:	0.%{snap}.1
Epoch:		1
License:	GPL
Group:		Libraries
# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/libffcall co .
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	a5190885da8e701a012bb282bfb3c51b
Patch0:		%{name}-make-jN.patch
Patch1:		%{name}-sparcv9.patch
# https://savannah.gnu.org/bugs/index.php?22081
Patch2:		%{name}-sparc64.patch
URL:		http://savannah.gnu.org/projects/libffcall
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

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

%description -l pl.UTF-8
To jest zestaw czterech bibliotek, których można użyć do tworzenia
interfejsów wywołań obcych procedur we wbudowanych interpreterach.

Te cztery pakiety to:
- avcall - wywoływanie funkcji w C ze zmiennymi argumentami
- vacall - funkcje w C akceptujące prototypy ze zmiennymi argumentami
- trampoline - domknięcia jako funkcje C pierwszej klasy
- callback - domknięcia ze zmiennymi argumentami jako funkcje C
  pierwszej klasy (zagnieżdżalna kombinacja vacall i trampoline)

Ta wersja B zawiera trochę małych zmian w konfiguracji, dzięki którym
pliki instalują się we właściwych miejscach. A także kompiluje się pod
cygwinem i mingw32.

%package devel
Summary:	Development files for ffcall libraries
Summary(pl.UTF-8):	Pliki dla programistów używających bibliotek ffcall
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files for ffcall libraries: headers and static trampoline
and vacall libraries.

%description devel -l pl.UTF-8
Pliki dla programistów używających bibliotek ffcall: nagłówki i
statyczne biblioteki trampoline oraz vacall.

%package static
Summary:	Static versions of avcall and callback libraries
Summary(pl.UTF-8):	Statyczne wersje bibliotek avcall i callback
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static versions of avcall and callback libraries.

%description static -l pl.UTF-8
Statyczne wersje bibliotek avcall i callback.

%prep
%setup -q -n %{name}-%{snap}
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# don't need those since we have man pages
%{__rm} $RPM_BUILD_ROOT%{_datadir}/html/*.html

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libavcall.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavcall.so.?
%attr(755,root,root) %{_libdir}/libcallback.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcallback.so.?

%files devel
%defattr(644,root,root,755)
%doc */*.html
%attr(755,root,root) %{_libdir}/libavcall.so
%attr(755,root,root) %{_libdir}/libcallback.so
%{_libdir}/libavcall.la
%{_libdir}/libcallback.la
%{_libdir}/libtrampoline.a
%{_libdir}/libvacall.a
%{_includedir}/*.h
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libavcall.a
%{_libdir}/libcallback.a
