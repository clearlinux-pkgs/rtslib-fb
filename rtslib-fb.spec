#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rtslib-fb
Version  : 2.1.66
Release  : 31
URL      : https://files.pythonhosted.org/packages/15/33/879f9e2e97c1cfca0f0d67985769b6ee566ca37abf7c4333d99e9794a1cb/rtslib-fb-2.1.66.tar.gz
Source0  : https://files.pythonhosted.org/packages/15/33/879f9e2e97c1cfca0f0d67985769b6ee566ca37abf7c4333d99e9794a1cb/rtslib-fb-2.1.66.tar.gz
Summary  : API for Linux kernel SCSI target (aka LIO)
Group    : Development/Tools
License  : Apache-2.0
Requires: rtslib-fb-bin
Requires: rtslib-fb-python3
Requires: rtslib-fb-python
Requires: pyudev
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
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
Requires: rtslib-fb-python3

%description python
python components for the rtslib-fb package.


%package python3
Summary: python3 components for the rtslib-fb package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rtslib-fb package.


%prep
%setup -q -n rtslib-fb-2.1.66

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532379257
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
