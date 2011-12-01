# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-decorator
Version:        3.0.1
Release:        3.1%{?dist}
Summary:        Module to simplify usage of decorators

Group:          Development/Languages
License:        BSD
URL:            http://www.phyast.pitt.edu/~micheles/python/documentation.html
Source0:        http://pypi.python.org/packages/source/d/decorator/decorator-%{version}.tar.gz
Patch0:         decorator-3.0.1-doctest.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel
BuildRequires:  python-nose

%description
The aim of the decorator module is to simplify the usage of decorators for
the average programmer, and to popularize decorators usage giving examples
of useful decorators, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a decorator factory called decorator.

%prep
%setup -q -n decorator-%{version}
%patch0 -p1 -b .doctest
chmod a-x *.txt *.py
%{__sed} -i 's/\r//' README.txt

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%check
# Until we get the python-multiprocessing backport packaged
%if 0%{?fedora} >= 11 || 0%{?rhel} > 5
nosetests --with-doctest
%endif

%files
%defattr(-,root,root,-)
%doc *.txt
%{python_sitelib}/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.0.1-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> - 3.0.1-2
- Only run the test suite on Fedora 11, which has Py2.6 and the multiprocessing
  module.  We can disable this once the compat module is packaged for F10 and
  below.

* Thu May 21 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 3.0.1-1
- Update to upstream release 3.0.1.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2
- Enable tests via nose

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2.0-2
- Rebuild for Python 2.6

* Thu Dec 20 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.0-1
- Initial Fedora Build
