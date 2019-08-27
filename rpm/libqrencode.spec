Name:           libqrencode
Version:        4.0.2
Release:        4%{?dist}
Summary:        Generate QR 2D barcodes
License:        LGPLv2+
URL:            http://fukuchi.org/works/qrencode/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  gcc
## For ARM 64 support (RHBZ 926414)
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  libtool
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:  libqrencode.so.4


%description
The libqrencode package contains libraries for developing
applications that use qrencode.

%package        devel
Summary:        QR Code encoding library - Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libqrencode-devel package contains libraries and header files for developing
applications that use libqrencode.



%prep
%setup -q -n %{name}-%{version}/libqrencode

%build
./autogen.sh
%configure --without-tools
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libqrencode.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/libqrencode.so.4
%{_libdir}/libqrencode.so.4.*


%files devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc


