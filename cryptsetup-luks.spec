Summary: A utility for setting up encrypted filesystems
Name: cryptsetup-luks
Version: 1.1.3
Release: 1
License: GPLv2
Group: Applications/System
URL: http://code.google.com/p/cryptsetup/downloads/list
Source: http://cryptsetup.googlecode.com/files/cryptsetup-%{version}.tar.bz2
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(popt)
BuildRequires: gettext
BuildRequires: cvs
BuildRequires: pkgconfig(e2p)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(devmapper)
BuildRequires: pkgconfig(libgpg-error)
Patch0: cryptsetup-maemo.patch
Patch1: crypt_keyslot_by_passphrase.patch


%description
This package contains cryptsetup, a utility for setting up
encrypted filesystems using Device Mapper and the dm-crypt target.


%package devel
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(uuid)
Requires: pkgconfig(devmapper)
Requires: pkgconfig(libgpg-error)
Summary: Headers and libraries for using encrypted filesystems


%description devel
The cryptsetup-luks-devel package contain libraries and header files
used for writing code that makes use of encrypted filesystems.


%package doc
Group: Documentation
Summary: Documentation for %{name}

%description doc
%{summary}.


%prep
%setup -q -n cryptsetup-%{version}
%patch0 -p1
%patch1 -p1
autoreconf -vfi
iconv -f latin1 -t utf8 ChangeLog > ChangeLog.new
mv -f ChangeLog.new ChangeLog


%build
%configure --disable-libdevmapper
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf  $RPM_BUILD_ROOT/%{_libdir}/*.la $RPM_BUILD_ROOT/%{_libdir}/cryptsetup

%find_lang cryptsetup

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f cryptsetup.lang
%defattr(-,root,root,-)
%{_sbindir}/cryptsetup
%{_libdir}/libcryptsetup.so.*


%files doc
%defattr(-,root,root,-)
%doc COPYING ChangeLog AUTHORS TODO
%{_mandir}/man8/cryptsetup.8.gz


%files devel
%defattr(-,root,root,-)
%{_includedir}/libcryptsetup.h
%{_libdir}/libcryptsetup.so
%{_libdir}/pkgconfig/libcryptsetup.pc
