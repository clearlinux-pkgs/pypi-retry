#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-retry
Version  : 0.9.2
Release  : 33
URL      : https://files.pythonhosted.org/packages/9d/72/75d0b85443fbc8d9f38d08d2b1b67cc184ce35280e4a3813cda2f445f3a4/retry-0.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/72/75d0b85443fbc8d9f38d08d2b1b67cc184ce35280e4a3813cda2f445f3a4/retry-0.9.2.tar.gz
Summary  : Easy to use retry decorator.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-retry-license = %{version}-%{release}
Requires: pypi-retry-python = %{version}-%{release}
Requires: pypi-retry-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(decorator)
BuildRequires : pypi(mock)
BuildRequires : pypi(pbr)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=====

%package license
Summary: license components for the pypi-retry package.
Group: Default

%description license
license components for the pypi-retry package.


%package python
Summary: python components for the pypi-retry package.
Group: Default
Requires: pypi-retry-python3 = %{version}-%{release}

%description python
python components for the pypi-retry package.


%package python3
Summary: python3 components for the pypi-retry package.
Group: Default
Requires: python3-core
Provides: pypi(retry)
Requires: pypi(decorator)
Requires: pypi(py)

%description python3
python3 components for the pypi-retry package.


%prep
%setup -q -n retry-0.9.2
cd %{_builddir}/retry-0.9.2
pushd ..
cp -a retry-0.9.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656404870
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-retry
cp %{_builddir}/retry-0.9.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-retry/77d262d28e2406c31b036afa6548c5fd23ff860f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-retry/77d262d28e2406c31b036afa6548c5fd23ff860f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
