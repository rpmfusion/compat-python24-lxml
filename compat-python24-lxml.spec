%define compat_python %{_bindir}/python2.4
%{!?python_sitearch: %define python_sitearch %(%{compat_python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           compat-python24-lxml
Version:        2.0.5
Release:        2%{?dist}
Summary:        ElementTree-like Python bindings for libxml2 and libxslt

Group:          Development/Libraries
License:        BSD
URL:            http://codespeak.net/lxml/
Source0:        http://codespeak.net/lxml/lxml-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  compat-python24-devel
BuildRequires:  libxslt-devel
BuildRequires:  compat-python24-setuptools-devel

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.

%prep
%setup -q -n lxml-%{version}

chmod a-x doc/rest2html.py

%build
CFLAGS="%{optflags}" %{compat_python} setup.py build

%install
rm -rf %{buildroot}
%{compat_python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt doc/
%{python_sitearch}/*

%changelog
* Sun Aug 10 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 2.0.5-2
- rebuild for RPM Fusion

* Mon May 26 2008 Jonathan Steffan <jonathansteffan a gmail.com> 2.0.5-1
- Update to 2.0.5

* Thu Mar 27 2008 Jonathan Steffan <jonathansteffan a gmail.com> 1.3.6-2
- Make a compat-python24 package,
  based on 1.3.6-1 from Fedora 8
