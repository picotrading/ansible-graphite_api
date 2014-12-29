%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

Name:           python-flask-cache
Version:        0.13.1
Release:        1%{?dist}
Summary:        Adds cache support to your Flask application

Group:          Development/Languages
License:        BSD
URL:            http://github.com/thadeusb/flask-cache
Source0:        https://pypi.python.org/packages/source/F/Flask-Cache/Flask-Cache-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-flask

%description
Adds cache support to your Flask application.


%prep
%setup -q -n Flask-Cache-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE CHANGES
%{python_sitelib}/*


%changelog
* Mon Dec 29 2014 Jiri Tyr <jiri.tyr@gmail.com> 0.13.1-1
- Initial package
