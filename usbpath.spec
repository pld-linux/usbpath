Summary:	Convert the physical locations of a USB device to/from its number
Summary(pl.UTF-8):	Konwersja między fizycznym położeniem urządzenia USB a jego numerem
Name:		usbpath
Version:	0.1
%define	snap	20071015
Release:	0.%{snap}.1
License:	GPL v2+
Group:		Libraries
# svn co http://svn.openmoko.org/trunk/src/host/usbpath/ usbpath
Source0:	%{name}-r6008.tar.xz
# Source0-md5:	a1c975de0c28b09f606e16605700ec2e
Patch0:		%{name}-shared.patch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusb-compat-devel >= 0.1
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
usbpath allows to convert the physical locations of a USB device
to/from its number.

%description -l pl.UTF-8
usbpath umożliwia konwersję między fizycznym położeniem urządzenia USB
a jego numerem.

%package devel
Summary:	Header files for usbpath library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki usbpath
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-compat-devel >= 0.1

%description devel
Header files for usbpath library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki usbpath.

%package static
Summary:	Static usbpath library
Summary(pl.UTF-8):	Statyczna biblioteka usbpath
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static usbpath library.

%description static -l pl.UTF-8
Statyczna biblioteka usbpath.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/lsusbpath
%attr(755,root,root) %{_bindir}/usbpath
%attr(755,root,root) %{_libdir}/libusbpath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusbpath.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libusbpath.so
%{_libdir}/libusbpath.la
%{_includedir}/usbpath.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libusbpath.a
