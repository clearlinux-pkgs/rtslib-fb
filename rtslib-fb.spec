#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rtslib-fb
Version  : 2.1.69
Release  : 34
URL      : https://files.pythonhosted.org/packages/fc/1a/77a26207bdad13cc39b93d874b3a1b04e5a0b0332fb716e4d654537bacdb/rtslib-fb-2.1.69.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/1a/77a26207bdad13cc39b93d874b3a1b04e5a0b0332fb716e4d654537bacdb/rtslib-fb-2.1.69.tar.gz
Summary  : API for Linux kernel SCSI target (aka LIO)
Group    : Development/Tools
License  : Apache-2.0
Requires: rtslib-fb-bin = %{version}-%{release}
Requires: rtslib-fb-python = %{version}-%{release}
Requires: rtslib-fb-python3 = %{version}-%{release}
Requires: pyudev
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
rtslib-fb
=========
A Python object API for managing the Linux LIO kernel target
------------------------------------------------------------
rtslib-fb is an object-based Python library for configuring the LIO
generic SCSI target, present in 3.x Linux kernel versions.

%package bin
Summary: bin components for the rtslib-fb package.
Group: Binaries

%description bin
bin components for the rtslib-fb package.


%package python
Summary: python components for the rtslib-fb package.
Group: Default
Requires: rtslib-fb-python3 = %{version}-%{release}

%description python
python components for the rtslib-fb package.


%package python3
Summary: python3 components for the rtslib-fb package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rtslib-fb package.


%prep
%setup -q -n rtslib-fb-2.1.69

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552072752
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/targetctl

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
