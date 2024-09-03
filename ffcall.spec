Summary:	Libraries for building foreign function call interfaces
Summary(pl.UTF-8):	Biblioteki do tworzenia interfejsów wywołań obcych funkcji
Name:		ffcall
Version:	2.5
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/libffcall/libffcall-%{version}.tar.gz
# Source0-md5:	4471b9d2342857125d2bbeee47dca66f
Patch0:		%{name}-make-jN.patch
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
%setup -q -n libffcall-%{version}
%patch0 -p1

%build
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for dependency generator and debuginfo extraction to work
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

# don't need those since we have man pages
%{__rm} $RPM_BUILD_ROOT%{_datadir}/html/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS PLATFORMS README
%attr(755,root,root) %{_libdir}/libavcall.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavcall.so.1
%attr(755,root,root) %{_libdir}/libcallback.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcallback.so.1
%attr(755,root,root) %{_libdir}/libffcall.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libffcall.so.0
%attr(755,root,root) %{_libdir}/libtrampoline.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtrampoline.so.1

%files devel
%defattr(644,root,root,755)
%doc */*.html
%attr(755,root,root) %{_libdir}/libavcall.so
%attr(755,root,root) %{_libdir}/libcallback.so
%attr(755,root,root) %{_libdir}/libffcall.so
%attr(755,root,root) %{_libdir}/libtrampoline.so
%{_libdir}/libavcall.la
%{_libdir}/libcallback.la
%{_libdir}/libffcall.la
%{_libdir}/libtrampoline.la
%{_libdir}/libvacall.a
%{_includedir}/avcall.h
%{_includedir}/callback.h
%{_includedir}/ffcall-*.h
%{_includedir}/trampoline*.h
%{_includedir}/vacall*.h
%{_mandir}/man3/avcall.3*
%{_mandir}/man3/callback.3*
%{_mandir}/man3/trampoline*.3*
%{_mandir}/man3/vacall.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libavcall.a
%{_libdir}/libcallback.a
%{_libdir}/libffcall.a
%{_libdir}/libtrampoline.a
